import { writable } from 'svelte/store';

export type SelectedIds = {
	allied: {
		0: number;
		1: number;
		2: number;
		3: number;
		4: number;
	};
	enemy: {
		0: number;
		1: number;
		2: number;
		3: number;
		4: number;
	};
};

export const selectedIds = writable<SelectedIds>({
	allied: {
		0: -1,
		1: -1,
		2: -1,
		3: -1,
		4: -1
	},
	enemy: {
		0: -1,
		1: -1,
		2: -1,
		3: -1,
		4: -1
	}
});
