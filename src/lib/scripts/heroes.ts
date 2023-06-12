import type { Hero } from '../types/heroes';
import { writable } from 'svelte/store';

export const heroes = writable<Hero[]>([]);
