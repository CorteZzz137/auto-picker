import type { Hero } from '$lib/types/heroes';
import { writable } from 'svelte/store';

export const heroes = writable<Hero[]>([]);
