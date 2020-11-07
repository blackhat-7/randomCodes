import React, { useState } from "react"
import Tweet from "./Tweet"
import "./App.css"

function App() {
  const [users, setUsers] = useState([
    { name: "Apple", message: "The all new Macbook Pro is available now" },
    { name: "Microsoft", message: "The all new Surface Pro is available now" },
    { name: "Oracle", message: "The all new Java is available now" },
    { name: "Samsung", message: "The all new Galaxy Note is available now" }
  ])

  return (
    <div className="App">
      {users.map(user => (
        <Tweet name={user.name} message={user.message} />
      ))}
    </div>
  );
}

export default App;