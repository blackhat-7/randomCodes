import React from "react";
import todoList from "../Data/todoList";
import TodoCheckBox from "./TodoCheckBox";

class Content extends React.Component {
  constructor() {
    super();
    this.state = {
      todos: todoList,
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(id) {
    this.setState((prevState) => {
      const updatedTodos = prevState.todos.map((item) => {
        const newItem = JSON.parse(JSON.stringify(item));
        if (item.id === id) {
          newItem.is_complete = !item.is_complete;
        }
        return newItem;
      });
      return {
        todos: updatedTodos,
      };
    });
  }

  render() {
    const todoComponents = this.state.todos.map((item) => {
      return (
        <TodoCheckBox
          key={item.id}
          item={item}
          handleChange={this.handleChange}
        />
      );
    });
    return <div>{todoComponents}</div>;
  }
}

export default Content;

