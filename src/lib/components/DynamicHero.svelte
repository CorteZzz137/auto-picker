<script lang="ts">
	import type { Hero as HeroType } from '$lib/types/heroes';

	export let hero: HeroType;
	export let border = true;
	//export let pointerEvents = true;
	// let video: HTMLVideoElement;
</script>

<div class="group relative flex h-28 w-20">
	<div class="pointer-events-none absolute h-full w-full">
		<div class="relative h-full border-black object-fill {border ? 'border' : ''}">
			<img src={`/heroes/images/${hero.lowercase_name}.jpg`} alt="name" class="h-full object-fill" />
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
