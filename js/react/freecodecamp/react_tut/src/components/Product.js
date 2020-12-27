import React from "react"

class Product extends React.Component {
  render() {
    return (
      <div>
        <h3>{this.props.name}</h3>
        <p style={{ padding: 10 }}>{this.props.price}</p>
        <p style={{ padding: 10 }}>{this.props.desc}</p>
      </div>
    );
  }
}

export default Product