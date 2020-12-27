import React from "react"

function TodoCheckBox(props) {
    const completedStyle = {
        fontStyle: "italic",
        color: "#cdcdcd",
        textDecoration: "line-through"
    }
    return (
        <div>
            <input
                type="checkbox"
                checked={props.item.is_complete}
                onChange={() => props.handleChange(props.item.id)}
            />
            <label style={props.item.is_complete ? completedStyle : null}>{props.item.text}</label>
            <br />
        </div >
    )
}

export default TodoCheckBox