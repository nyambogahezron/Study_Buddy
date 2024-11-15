import { create } from 'zustand';
import { User } from '../types';

type UserStore = {
  user: User | null;
  logout: () => void;
  setUser: (user: User) => void;
};

export const useUserStore = create<UserStore>((set) => ({
  user: {
    id: 1,
    username: 'john',
    name: 'John Doe',
    email: 'john@gmail.com',
  },
  logout: () => set({ user: null }),
  setUser: (user: User) => set({ user }),
}));
