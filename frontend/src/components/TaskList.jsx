/* eslint-disable react/prop-types */
import TaskItem from "./TaskItem";
const TaskList = ({ tasks }) => {
  return (
    <div className="task-list">
      <h1>Task List</h1>
      {tasks.map((task) => (
        <TaskItem key={task.id} task={task} />
      ))}
    </div>
  );
};

export default TaskList;
