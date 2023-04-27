<script lang="ts">
	import Hero from '$lib/components/StaticHero.svelte';
	import { heroes } from '$lib/scripts/heroes';

	export let pointerEvents = true;
</script>

<div class="flex flex-col gap-2">
	<div class="flex w-min items-center gap-1 border border-dashed border-white">
		<!-- <img src="/all.png" alt="" class="w-4 select-none" /> -->
		<span class="flex text-sm uppercase leading-3 text-slate-200">All</span>
	</div>
	<div class="flex flex-row flex-wrap gap-1">
		{#each $heroes as hero}
			{#if hero.attribute === 'all'}
				<div class="h-14 w-8">
					<Hero {hero} {pointerEvents} />
				</div>
			{/if}
		{/each}
	</div>
</div>
