<script lang="ts">
	import type { Hero as HeroType } from '../types/heroes';
	import { tweened } from 'svelte/motion';
	import DynamicHeroPoster from './DynamicHeroPoster.svelte';
	import { editing } from '../scripts/editing';
	import { selectedId } from '../scripts/selectedHeroStore';
	import { flags } from '../scripts/showFlag';
	import { isMuted } from '../scripts/helpers';
	import { selectedIds } from '../scripts/selectedIds';
	import { input } from '../scripts/input';

	export let hero: HeroType;
	export let pointerEvents = true;

	const coords = tweened({ x: 0, y: 0 }, { duration: 0 });
	let showPoster = false;

	const hoverDynamicPoster = (node: HTMLDivElement, props: { enabled: boolean }) => {
		let { enabled } = props;

		function handleMouseenter(_e: MouseEvent) {
			if (!enabled) return;

			const bounds = node.getBoundingClientRect();

			coords.set({
				x: bounds.x - 40 + bounds.width / 2,
				y: bounds.y - 56 + bounds.height / 2
			});
			showPoster = true;
			node.addEventListener('mouseout', handleMouseout);
		}

		function handleMouseout(_e: MouseEvent) {
			if (!enabled) return;

			coords.set({ x: 0, y: 0 });
			showPoster = false;
			node.removeEventListener('mouseout', handleMouseout);
		}

		node.addEventListener('mouseenter', handleMouseenter);
		return {
			update: (props: { enabled: boolean }) => {
				enabled = props.enabled;
				if (!enabled) {
					coords.set({ x: 0, y: 0 });
					showPoster = false;
					node.removeEventListener('mouseenter', handleMouseenter);
					node.removeEventListener('mouseout', handleMouseout);
				}

				if (enabled) {
					node.addEventListener('mouseenter', handleMouseenter);
				}
			},
			destroy: () => {
				node.removeEventListener('mouseenter', handleMouseenter);
			}
		};
	};
</script>

<div
	use:hoverDynamicPoster={{ enabled: pointerEvents }}
	on:mousedown={() => {
		$editing?.callback(hero.id);
		$selectedId = hero.id;
	}}
	class="transition-filter relative flex h-full w-full cursor-pointer overflow-hidden {isMuted(
		$flags,
		$selectedIds,
		$input,
		hero
	)
		? 'opacity-30 grayscale'
		: ''}"
>
	<div class="pointer-events-none absolute -left-[12.5%] h-full w-[125%]">
		<img
			src={`/heroes/images/${hero.lowercase_name}/avatar.jpg`}
			alt="name"
			class="h-full object-fill"
		/>
	</div>
</div>

{#if showPoster}
	<div
		style="translate: {$coords.x}px {$coords.y}px;"
		class="pointer-events-none absolute left-0 top-0 z-50 h-28 w-20"
	>
		<DynamicHeroPoster {hero} border={true} />
	</div>
{/if}

<style>
	div {
		user-select: none;
	}

	.transition-filter {
		transition-property: opacity filter;
		transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
		transition-duration: 150ms;
	}
</style>
