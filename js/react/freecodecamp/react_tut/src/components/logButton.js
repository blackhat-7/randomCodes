import React from "react"

class LogButton extends React.Component {
  render() {
    return (
      <button onClick={this.props.toggle}>{this.props.log ? "Log Out" : "Log In"}</button >
    );
  }
}



export default LogButton