import logo from "./logo.svg";
import "./App.css";
//import AppHeader from "./components/AppHeader";
import Cricket from "./component/Click";

function App() {
  return (
    <div>
      <Cricket target={200} totalOvers={10}/>
      <br></br>
    </div>
  );
}

export default App;