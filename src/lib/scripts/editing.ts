import { writable } from 'svelte/store';

export const editing = writable<{ id: number; callback: (id: number) => void } | null>(null);
