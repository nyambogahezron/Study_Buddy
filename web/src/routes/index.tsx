import App from '../App.tsx';
import Home from '../pages/Home.tsx';
import Register from '../pages/Register.tsx';
import Login from '../pages/Login.tsx';
import CreateRoom from '../pages/CreateRoom.tsx';
import EditUser from '../pages/EditUser.tsx';
import Activity from '../pages/Activity.tsx';
import Profile from '../pages/Profile.tsx';
import Room from '../pages/Room.tsx';
import ErrorPage from '../pages/error-page.tsx';

import { createBrowserRouter } from 'react-router-dom';

export const router = createBrowserRouter([
  {
    path: '/',
    errorElement: <ErrorPage />,
    element: <App />,
    children: [
      {
        path: '/',
        element: <Home />,
      },
      {
        path: '/create-room',
        element: <CreateRoom />,
      },
      {
        path: '/edit-user',
        element: <EditUser />,
      },
      {
        path: '/activity',
        element: <Activity />,
      },
      {},
    ],
  },
  {
    path: '/login',
    element: <Login />,
  },
  {
    path: 'register',
    element: <Register />,
  },
  {
    path: '/profile',
    element: <Profile />,
  },
  {
    path: '/room/:id',
    element: <Room />,
  },
]);
