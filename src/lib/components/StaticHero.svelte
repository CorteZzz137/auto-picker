<script lang="ts">
	import drag from '$lib/actions/draggable';
	import { createEventDispatcher } from 'svelte';
	import { tweened } from 'svelte/motion';
	import type { Hero as HeroType } from '$lib/types/heroes';
	const dispatch = createEventDispatcher();

	export let hero: HeroType;
	export let pointerEvents = true;
	let video: HTMLVideoElement;

	const coords = tweened(
		{ x: 0, y: 0 },
		{
			duration: 100
		}
	);

	const handleDrag = (node: HTMLDivElement) => {
		let globalDX = 0;
		let globalDY = 0;

		function handleMousedown(e: MouseEvent) {
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
</script>

<!-- svelte-ignore a11y-mouse-events-have-key-events -->
<!-- svelte-ignore a11y-click-events-have-key-events -->
<div
	use:handleDrag
	on:mousedown={() => dispatch('selected', hero.id)}
	style="translate: {$coords.x}px {$coords.y}px;"
	class="group relative flex h-14 w-8 overflow-hidden rounded-sm duration-75 hover:z-40 hover:cursor-pointer hover:overflow-visible {!pointerEvents
		? 'pointer-events-none'
		: ''}"
>
	<div class="pointer-events-none absolute -left-[4px] h-full w-[125%]">
		<div class="relative h-full border-black object-fill group-hover:scale-[200%] group-hover:border">
			<img src={`/heroes/images/${hero.lowercase_name}.jpg`} alt="name" class="h-full object-fill" />
			<h1
				class="absolute left-0 bottom-0 mx-auto hidden w-full flex-wrap items-center justify-center bg-black/70 py-[2px] px-0.5 text-[0.27rem] uppercase leading-[0.27rem] text-slate-200 group-hover:flex"
			>
				<span class="w-full translate-y-[1px] text-center">{hero.name}</span>
			</h1>
		</div>
	</div>
</div>

<style>
	div {
		user-select: none;
	}
</style>
