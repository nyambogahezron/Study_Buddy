import { useUserStore } from '../store/useUserStore';
import { User } from '../types';

export default function StartSession(user: User | null) {
  const setUser = useUserStore((state) => state.setUser);

  if (!user) {
    return null;
  }
  localStorage.setItem('user', JSON.stringify(user));
  setUser(user);
  return user;
}


export function EndSession() {
  const logout = useUserStore((state) => state.logout);
  localStorage.removeItem('user');
  logout();
}