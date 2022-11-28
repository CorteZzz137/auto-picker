<script lang="ts">
	import type { Hero as HeroType } from '$lib/types/heroes';
	import { tick } from 'svelte';

	export let hero: HeroType;
	export let border = true;

	//export let pointerEvents = true;
</script>

<div class="group pointer-events-none relative flex h-28 w-20">
	<div class="absolute h-full w-full">
		<div class="relative h-full border-black object-fill {border ? 'border-2' : ''}">
			<video
				poster="/heroes/images/{hero.lowercase_name}.jpg"
				src="/heroes/videos/{hero.lowercase_name}.webm"
				class="h-full object-fill"
				autoplay
				loop
			>
				<track kind="captions" />
			</video>
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
