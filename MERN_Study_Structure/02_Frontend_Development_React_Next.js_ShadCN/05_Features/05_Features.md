# Features:

## 📚 Curriculum Checklist
- [x] Task List with CRUD (Create, Update, Delete)
- [x] Drag & Drop Task Management (Using react-beautiful-dnd)
- [x] ShadCN Components (Dialog, Toast, Modal)
- [x] Local Storage for Data Persistence

## 📝 Detailed Notes

### 1. CRUD Task List (Create, Read, Update, Delete)
```tsx
interface Task { id: string; title: string; status: 'todo' | 'done'; }

const [tasks, setTasks] = useState<Task[]>([]);

// Create
const addTask = (title: string) =>
    setTasks(prev => [...prev, { id: crypto.randomUUID(), title, status: 'todo' }]);

// Update
const updateTask = (id: string, changes: Partial<Task>) =>
    setTasks(prev => prev.map(t => t.id === id ? { ...t, ...changes } : t));

// Delete
const deleteTask = (id: string) =>
    setTasks(prev => prev.filter(t => t.id !== id));
```

### 2. Drag & Drop (react-beautiful-dnd)
```tsx
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

const onDragEnd = (result) => {
    if (!result.destination) return;
    const newTasks = Array.from(tasks);
    const [moved] = newTasks.splice(result.source.index, 1);
    newTasks.splice(result.destination.index, 0, moved);
    setTasks(newTasks);
};

<DragDropContext onDragEnd={onDragEnd}>
    <Droppable droppableId="tasks">
        {(provided) => (
            <div {...provided.droppableProps} ref={provided.innerRef}>
                {tasks.map((task, i) => (
                    <Draggable key={task.id} draggableId={task.id} index={i}>
                        {(provided) => (
                            <div ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps}>
                                {task.title}
                            </div>
                        )}
                    </Draggable>
                ))}
                {provided.placeholder}
            </div>
        )}
    </Droppable>
</DragDropContext>
```

### 3. ShadCN Toast Notifications
```tsx
import { useToast } from '@/components/ui/use-toast';
const { toast } = useToast();

// On task creation
toast({ title: 'Task created!', description: 'Your task has been added.' });
// On error
toast({ title: 'Error', description: 'Something went wrong.', variant: 'destructive' });
```

### 4. Local Storage Persistence with useEffect
```tsx
// Load on mount
useEffect(() => {
    const saved = localStorage.getItem('tasks');
    if (saved) setTasks(JSON.parse(saved));
}, []);

// Save on every change
useEffect(() => {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}, [tasks]);
```

---

## 🎓 Important Interview Questions

### Q1: How does `react-beautiful-dnd` work?
It wraps list containers in `<Droppable>` and list items in `<Draggable>`. The `onDragEnd` callback gives you source and destination indices. You then reorder the array immutably using `splice`.

### Q2: Why use `crypto.randomUUID()` for task IDs?
It generates a globally unique ID without any library, avoiding key conflicts in React lists and database collisions.


## ❓ Questions & Doubts
- [ ]

---

[⬅️ Previous: Integrating Tailwind Material UI and ShadCN in React Nextjs](../../MERN_Study_Structure/02_Frontend_Development_React_N/04_Integrating_Tailwind_Material_UI_and_ShadCN_in_React_Nextjs/04_Integrating_Tailwind_Material_UI_and_ShadCN_in_React_Nextjs.md) | [🏠 Home](../../README.md) | [Next: Features ➡️](../../MERN_Study_Structure/02_Frontend_Development_React_N/06_Features/06_Features.md)