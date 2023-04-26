import { writable } from 'svelte/store';
import type { IntRange } from './helpers';
import { heroes } from './heroes';

export type Role = IntRange<0, 4>;
export type Marks = IntRange<0, 256>;

export let rolesId = {
	Carry: 2,
	Support: 1
} as const;

export let marksId = {
	Melee: 128,
	Ranged: 64,
	Disabler: 32,
	Durable: 16,
	Escape: 8,
	Initiator: 4,
	Nuker: 2,
	Pusher: 1
} as const;

export const flags = writable<{
	role: IntRange<0, 4>;
	marks: IntRange<0, 256>;
}>({
	role: 0,
	marks: 0
});
