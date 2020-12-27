import React from "react";

class Content2 extends React.Component {
  constructor() {
    super();
    this.state = {};
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    const { name, value } = event.target;
    this.setState({
      [name]: value,
    });
  }

  render() {
    return (
      <form>
        <input
          type="text"
          name="firstname"
          placeholder="FirstName"
          value={this.state.firstname}
          onChange={this.handleChange}
        />
        <input
          type="text"
          name="lastname"
          placeholder="LastName"
          value={this.state.lastname}
          onChange={this.handleChange}
        />
        <h1>
          {this.state.firstname} {this.state.lastname}
        </h1>
      </form>
    );
  }
}

export default Content2;
