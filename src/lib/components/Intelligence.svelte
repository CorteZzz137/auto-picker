<script lang="ts">
	import Hero from '$lib/components/StaticHero.svelte';
	import type { Hero as HeroType } from '$lib/types/heroes';

	export let heroes: HeroType[];
	export let pointerEvents = true;
	export let onlyCarry = false;
	export let onlySupport = false;
</script>

<div class="flex flex-col gap-2">
	<div class="flex items-center gap-1">
		<img src="/intelligence.png" alt="" class="w-4 select-none" />
		<span class="flex text-sm uppercase leading-3 text-slate-200">Intelligence</span>
	</div>
	<div class="flex flex-row flex-wrap gap-1">
		{#each heroes as hero}
			{#if hero.attribute === 'intelligence'}
				<Hero {hero} {pointerEvents} on:dragstart on:selected {onlyCarry} {onlySupport} />
			{/if}
		{/each}
	</div>
</div>
