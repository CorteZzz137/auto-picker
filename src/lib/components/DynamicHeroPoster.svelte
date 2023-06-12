<script lang="ts">
	import type { Hero } from '../types/heroes';
	import VideoHero from './VideoHero.svelte';

	export let hero: Hero;
	export let border = true;
	export let bigPoster = false;
	export let namePos: 'top' | 'bottom' = 'bottom';
</script>

<div class="group pointer-events-none relative flex h-full w-full">
	<div class="absolute h-full w-full">
		<div class="relative h-full border-black object-fill {border ? 'border-2' : ''}">
			<VideoHero {hero} />
			<h1
				class="absolute {namePos == 'bottom'
					? 'bottom-0'
					: 'top-0'} left-0 mx-auto flex w-full flex-wrap items-center justify-center
				bg-black/50 px-1 {bigPoster
					? 'pb-1 text-[0.9rem] leading-[1.1rem]'
					: 'py-1 text-[0.54rem] leading-[0.6rem]'} uppercase text-slate-200"
			>
				<span class="w-full translate-y-0.5 text-center">{hero?.name}</span>
			</h1>
		</div>
	</div>
</div>

<style>
	div {
		user-select: none;
	}
</style>
