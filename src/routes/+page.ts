import { heroes } from '$lib/scripts/heroes';
import type { Hero } from '$lib/types/heroes';
import type { PageLoad } from './$types';

export const prerender = true;

export const load: PageLoad = async ({ fetch }) => {
	const res = await fetch('/heroes.json');
	const heroesData: Hero[] = await res.json();
	heroes.update(() => heroesData);
};
