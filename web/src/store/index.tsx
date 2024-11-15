
// rooms data store and actions

import create from 'zustand';
import { Room } from '../types';

type RoomStore = {
  rooms: Room[];
  addRoom: (room: Room) => void;
  removeRoom: (roomId: number) => void;
};

export const useRoomStore = create<RoomStore>((set) => ({
  rooms: [],
  addRoom: (room) => set((state) => ({ rooms: [...state.rooms, room] })),
  removeRoom: (roomId) =>
    set((state) => ({
      rooms: state.rooms.filter((room) => room.id !== roomId),
    })),
});
