<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	import type { Hero as HeroType } from '$lib/types/heroes';
	import { tweened } from 'svelte/motion';
	import DynamicHero from './DynamicHero.svelte';
	const dispatch = createEventDispatcher();

	export let hero: HeroType;
	export let pointerEvents = true;

	const coords = tweened({ x: 0, y: 0 }, { duration: 0 });
	let showPoster = false;

	const handleDrag = (node: HTMLDivElement) => {
		let globalDX = 0;
		let globalDY = 0;

		function handleMousedown(_e: MouseEvent) {
			globalDX = 0;
			globalDY = 0;
			window.addEventListener('mousemove', handleMousemove);
			//window.dispatchEvent(new CustomEvent('herodragstart', { detail: { x: e.clientX, y: e.clientY } }));
			window.addEventListener('mouseup', handleMouseup);
		}

		function handleMousemove(e: MouseEvent) {
			globalDX += e.movementX;
			globalDY += e.movementY;
			if (Math.abs(globalDX) > 5 || Math.abs(globalDY) > 5) {
				window.dispatchEvent(new CustomEvent('herodragstart', { detail: { x: e.clientX, y: e.clientY } }));
				window.removeEventListener('mousemove', handleMousemove);
				return;
			}
		}

		function handleMouseup(e: MouseEvent) {
			window.dispatchEvent(new CustomEvent('herodragend', { detail: { x: e.clientX, y: e.clientY } }));
			window.removeEventListener('mousemove', handleMousemove);
			window.removeEventListener('mouseup', handleMouseup);
		}

		node.addEventListener('mousedown', handleMousedown);
		return {
			update: () => {},
			destroy: () => {}
		};
	};

	const hoverDynamicPoster = (node: HTMLDivElement, props: { enabled: boolean }) => {
		let { enabled } = props;

		function handleMouseenter(e: MouseEvent) {
			if (!enabled) return;

			const bounds = node.getBoundingClientRect();

			coords.set({ x: bounds.x - 40 + bounds.width / 2, y: bounds.y - 56 + bounds.height / 2 });
			showPoster = true;
			node.addEventListener('mouseout', handleMouseout);
		}

		function handleMouseout(e: MouseEvent) {
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
			destroy: () => {}
		};
	};
</script>

<div
	use:handleDrag
	use:hoverDynamicPoster={{ enabled: pointerEvents }}
	on:mousedown={() => dispatch('selected', hero.id)}
	class="relative flex h-14 w-8 cursor-pointer overflow-hidden {!pointerEvents ? 'pointer-events-none' : ''}"
>
	<div class="pointer-events-none absolute -left-[4px] h-full w-[125%]">
		<img src={`/heroes/images/${hero.lowercase_name}.jpg`} alt="name" class="h-full object-fill" />
	</div>
</div>

{#if showPoster}
	<div style="translate: {$coords.x}px {$coords.y}px;" class="pointer-events-none absolute left-0 top-0 z-50">
		<DynamicHero {hero} border={true} />
	</div>
{/if}

<style>
	div {
		user-select: none;
	}
</style>
