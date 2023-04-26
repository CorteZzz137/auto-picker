<script lang="ts">
	import type { Hero } from '$lib/types/heroes';
	import { createEventDispatcher } from 'svelte';
	import { editing } from '$lib/scripts/editing';
	import { heroes } from '$lib/scripts/heroes';
	import VideoHero from './VideoHero.svelte';
	import { selectedIds } from '$lib/scripts/selectedIds';

	export let id: number;
	let hero: Hero | null = null;
</script>

<button
	on:click={() => {
		$editing =
			!$editing || $editing.id !== id
				? {
						id,
						callback: (idHero) => {
							if ($selectedIds.has(idHero)) return;
							if (hero && $selectedIds.has(hero.id)) $selectedIds.delete(hero.id);
							hero = $heroes[idHero];
							$editing = null;
							$selectedIds.add(idHero);
							$selectedIds = $selectedIds;
						}
				  }
				: null;
	}}
	class="group relative flex h-24 w-16 cursor-pointer bg-transparent group-hover:border-8"
>
	{#if hero}
		<VideoHero {hero} />
	{/if}
	{#if ($editing === null || $editing.id !== id) && !hero}
		<div class="absolute flex h-full w-full items-center justify-center border-4 border-white">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 24 24"
				stroke-width="3"
				stroke="currentColor"
				class="h-10 w-10 transition-transform group-hover:h-16 group-hover:w-16"
			>
				<path d="M12 6v12m6-6H6" />
			</svg>
		</div>
	{:else if $editing && $editing.id === id}
		<div
			class="absolute z-10 flex h-24 w-16 cursor-pointer items-center justify-center bg-transparent ring-4 ring-inset ring-green-400 group-hover:ring-8"
		/>
	{/if}
</button>
