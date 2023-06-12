import { writable } from 'svelte/store';

export type Editing = {
	id: number;
	callback: (id: number) => void;
} | null;

export const editing = writable<Editing>(null);
