import MainLayout from './Layouts/mainLayout';
import { Outlet } from 'react-router-dom';

export default function App() {
  return (
    <>
      <MainLayout>
        <Outlet />
      </MainLayout>
    </>
  );
}
