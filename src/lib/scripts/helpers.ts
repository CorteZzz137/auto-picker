import type { Hero } from '../types/heroes';
import type { SelectedIds } from './selectedIds';
import { rolesId, type Flag, marksId } from './showFlag';

type Enumerate<N extends number, Acc extends number[] = []> = Acc['length'] extends N
	? Acc[number]
	: Enumerate<N, [...Acc, Acc['length']]>;

export type IntRange<F extends number, T extends number> = Exclude<Enumerate<T>, Enumerate<F>>;

export function capFirst<T extends string>(str: T): Capitalize<T> {
	return (str[0].toUpperCase() + str.slice(1, str.length)) as Capitalize<T>;
}

export const getKeys = <T extends object>(obj: T) => {
	return Object.keys(obj) as (keyof typeof obj)[];
};

export const hasId = (
	obj: {
		0: number | null;
		1: number | null;
		2: number | null;
		3: number | null;
		4: number | null;
	},
	id: number
) => {
	return getKeys(obj).reduce((prev, curr) => prev || obj[curr] === id, false);
};

export const isMuted = (flagss: Flag, ids: SelectedIds, input: string, hero: Hero) => {
	let flagRole = 0;
	let flagMark = 0;
	hero.roles.forEach((role) => {
		if (role === 'Carry' || role === 'Support') {
			flagRole |= rolesId[role];
		} else {
			flagMark |= marksId[role];
		}
	});
	return (
		(input.length !== 0 && !hero.name.toLowerCase().startsWith(input)) ||
		(flagRole & flagss.role) !== flagss.role ||
		(flagMark & flagss.marks) !== flagss.marks ||
		hasId(ids.allied, hero.id) ||
		hasId(ids.enemy, hero.id)
	);
};

export const toLower = (str: string) => {
	return str.toLowerCase().split(' ').join('_');
};
