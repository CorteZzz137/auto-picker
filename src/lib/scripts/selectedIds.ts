import { writable } from 'svelte/store';

export const selectedIds = writable<Set<number>>(new Set<number>());
