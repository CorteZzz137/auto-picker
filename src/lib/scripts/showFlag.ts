import { writable } from 'svelte/store';
import type { IntRange } from './helpers';

export type Role = IntRange<0, 4>;
export type Marks = IntRange<0, 256>;

export let rolesId = {
	Carry: 1 << 1,
	Support: 1 << 0
} as const;

export let marksId = {
	Melee: 1 << 7,
	Ranged: 1 << 6,
	Disabler: 1 << 5,
	Durable: 1 << 4,
	Escape: 1 << 3,
	Initiator: 1 << 2,
	Nuker: 1 << 1,
	Pusher: 1 << 0
} as const;

export type Flag = {
	role: Role;
	marks: Marks;
};

export const flags = writable<Flag>({
	role: 0,
	marks: 0
});
