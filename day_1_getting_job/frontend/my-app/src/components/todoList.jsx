import { useEffect, useState } from "react";
import axios from "axios";

const TodoList = () => {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState("");
  const [status, setStatus] = useState("pending");

  // ✅ Fetch todos
  const fetchTodos = async () => {
    try {
      const token = localStorage.getItem("token");
      console.log("lll");
      console.log("Fetching todos with token:", token);
      const response = await axios.get(" http://localhost:3000/api/todos", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setTodos(response.data);
    } catch (error) {
      console.error("Error fetching todos:", error);
    }
  };

  // ✅ Add new todo (uses input instead of prompt)
  const addtodo = async () => {
    if (!newTodo.trim()) return;

    try {
      const token = localStorage.getItem("token");
        console.log("Adding todo with token:", token);
      const response = await axios.post(
        "http://localhost:3000/api/todos",
        { title: newTodo.trim(), status },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
        console.log("Todo added:", response.data);
      setTodos((prev) => [...prev, response.data]);
      setNewTodo("");
      setStatus("pending");
    } catch (error) {
      console.error("Error adding todo:", error);
    }
  };

  // ✅ Update todo
  const updateTodo = async (id) => {
    const updatedtitle = prompt("Enter updated todo:");
    if (!updatedtitle) return;

    try {
      const token = localStorage.getItem("token");
      const response = await axios.put(
        `http://localhost:3000/api/todos/${id}`,
        { title: updatedtitle },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setTodos((prev) =>
        prev.map((todo) => (todo._id === id ? response.data : todo))
      );
    } catch (error) {
      console.error("Error updating todo:", error);
    }
  };

  // ✅ Delete todo
  const deleteTodo = async (id) => {
    try {
      const token = localStorage.getItem("token");
      await axios.delete(`http://localhost:3000/api/todos/${id}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setTodos((prev) => prev.filter((todo) => todo._id !== id));
    } catch (error) {
      console.error("Error deleting todo:", error);
    }
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  return (
    <div className="max-w-xl mx-auto p-4">
      <h1 className="title-2xl font-bold mb-4">Todo List</h1>

      {/* New todo input */}
      <div className="flex space-x-2 mb-4">
        <input
          type="title"
          value={newTodo}
          onChange={(e) => setNewTodo(e.target.value)}
          placeholder="Enter new todo"
          className="border p-2 rounded w-full"
        />
        <select
          value={status}
          onChange={(e) => setStatus(e.target.value)}
          className="border p-2 rounded"
        >
          <option value="pending">Pending</option>
          <option value="in-progress">In Progress</option>
          <option value="completed">Completed</option>
        </select>
        <button
          onClick={addtodo}
          className="bg-blue-500 px-4 py-2 rounded title-white"
        >
          Add
        </button>
      </div>

      {/* Todo list */}
      <ul className="space-y-2">
        {todos.map((todo) => (
          <li
            key={todo._id}
            className="flex justify-between items-center border p-2 rounded"
          >
            <span>
              {todo.title}{" "}
              <span className="title-xs title-gray-500">({todo.status})</span>
            </span>
            <div className="space-x-2">
              <button
                onClick={() => updateTodo(todo._id)}
                className="bg-yellow-400 px-2 py-1 rounded title-white"
              >
                Edit
              </button>
              <button
                onClick={() => deleteTodo(todo._id)}
                className="bg-red-600 px-2 py-1 rounded title-white"
              >
                Delete
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoList;
