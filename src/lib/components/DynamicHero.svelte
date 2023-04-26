<script lang="ts">
	import type { Hero as HeroType } from '$lib/types/heroes';
	import { tick } from 'svelte';
	import VideoHero from './VideoHero.svelte';

	export let hero: HeroType;
	export let border = true;
</script>

<div class="group pointer-events-none relative flex h-28 w-20">
	<div class="absolute h-full w-full">
		<div class="relative h-full border-black object-fill {border ? 'border-2' : ''}">
			<VideoHero {hero} />
			<h1
				class="absolute left-0 bottom-0 mx-auto flex w-full flex-wrap items-center justify-center bg-black/70 py-1 px-1 text-[0.54rem] uppercase leading-[0.6rem] text-slate-200"
			>
				<span class="w-full translate-y-0.5 text-center">{hero.name}</span>
			</h1>
		</div>
	</div>
</div>

<style>
	div {
		user-select: none;
	}
</style>
