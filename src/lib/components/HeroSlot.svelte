<script lang="ts">
	import type { Hero } from '../types/heroes';
	import { editing } from '../scripts/editing';
	import { heroes } from '../scripts/heroes';
	import VideoHero from './VideoHero.svelte';
	import { selectedIds } from '../scripts/selectedIds';
	import { hasId } from '../scripts/helpers';

	export let id: number;
	let hero: Hero | null = null;

	const slotClick = (e: MouseEvent) => {
		if (!$editing || $editing.id !== id) {
			$editing = {
				id,
				callback: (idHero) => {
					if (hasId($selectedIds.enemy, idHero) || hasId($selectedIds.allied, idHero))
						return;
					if (hero && hasId($selectedIds.enemy, hero.id)) $selectedIds.enemy[id - 5] = -1;
					if (hero && hasId($selectedIds.allied, hero.id)) $selectedIds.allied[id] = -1;
					hero = $heroes[idHero];
					$editing = null;
					if (id > 4) $selectedIds.enemy[id - 5] = idHero;
					else $selectedIds.allied[id] = idHero;
					$selectedIds = $selectedIds;
				}
			};
			return;
		}
		$editing = null;
	};
</script>

<button
	on:contextmenu={() => {
		if (id > 4) $selectedIds.enemy[id - 5] = -1;
		else $selectedIds.allied[id] = -1;
		$selectedIds = $selectedIds;
		hero = null;
	}}
	on:click={slotClick}
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
			class="absolute z-10 flex h-24 w-16 cursor-pointer items-center justify-center
			bg-transparent ring-4 ring-inset ring-green-400 group-hover:ring-8"
		/>
	{/if}
</button>
