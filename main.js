const express = require("express");
const app = express();
require("dotenv").config();

const AWS = require("aws-sdk");
const cors = require("cors");
const path = require("path");

app.use(express.json());
app.use(cors());

app.use(function (req, res, next) {
  //allow cross origin requests
  res.setHeader(
    "Access-Control-Allow-Methods",
    "POST, PUT, OPTIONS, DELETE, GET"
  );
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  res.header("Access-Control-Allow-Credentials", true);
  next();
});

const port = process.env.PORT || 9876;

app.use(express.static(path.join(__dirname, "/app/dist")));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "/app/dist/index.html"));
});

app.get("/phone", (req, res) => {
  console.log("Message = " + req.query.message);
  console.log("Number = " + req.query.number);
  console.log("Subject = " + req.query.subject, "\n");

  var params = {
    Message: req.query.message,
    PhoneNumber: "+" + req.query.number,
    MessageAttributes: {
      "AWS.SNS.SMS.SenderID": {
        DataType: "String",
        StringValue: req.query.subject,
      },
    },
  };
  
  let sns = new AWS.SNS({ apiVersion: "2010-03-31" });

  sns.publish(params, (err, data) => {
    if (err) {
      res.end(JSON.stringify({ Error: err }));
    } else {
      res.end(JSON.stringify({ MessageID: data.MessageId }));
    }
  });
});

app.get("/mail", async (req, res) => {
  const email = process.env.FROM_EMAIL;
  const ses = new AWS.SES();

  console.log(email);

  try {
    const params = {
      Source: email,
      Destination: {
        ToAddresses: [
          email,
          "alexa.aiboost@gmail.com",
          "founder.aiboost@gmail.com",
        ],
      },
      Message: {
        Subject: { Charset: "UTF-8", Data: `alert from TalentShip` },
        Body: {
          Html: {
            Charset: "UTF-8",
            Data: `<h1>this is an alert from TalentShip </h1>`,
          },
        },
      },
    };
    
    await ses.sendEmail(params, (err, data) => {
      if (err) {
        res.end(JSON.stringify({ Error: err }));
      } else {
        res.end(JSON.stringify({ MessageID: data.MessageId }));
      }
    });
  } catch (error) {
    res.end(JSON.stringify({ Error: error }));
  }
});

app.listen(port, (success, error) => {
  if (error) {
    console.log("error occured", error);
  }
  console.log(`server is running on port = ${port}`);
});
