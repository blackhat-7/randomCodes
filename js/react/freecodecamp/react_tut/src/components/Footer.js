
import React from "react"
import LogButton from "./logButton";

class Footer extends React.Component {
  constructor() {
    super()
    this.state = {
      isLoggedIn: false
    }
    this.toggle = this.toggle.bind(this)
  }

  toggle() {
    this.setState(prevState => {
      return {
        isLoggedIn: !prevState.isLoggedIn
      }
    })
  }

  render() {
    return (
      <div>
        <LogButton toggle={this.toggle} log={this.state.isLoggedIn} />
        {console.log(this.state.isLoggedIn)}
        <h3> You are logged {this.state.isLoggedIn ? "In" : "Out"} </h3>
      </div>
    );
  }

}

export default Footer
