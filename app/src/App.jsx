import { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <h1 class="text-3xl font-bold text-teal-700">Hello world!</h1>
    </div>
  );
}

export default App;
