const express = require("express");
const app = express();

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

app.listen(port, (success, error) => {
  if (error) {
    console.log("error occured", error);
  }
  console.log(`server is running on port = ${port}`);
});
