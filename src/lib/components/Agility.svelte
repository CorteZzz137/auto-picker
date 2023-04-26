<script lang="ts">
	import Hero from '$lib/components/StaticHero.svelte';
	import { heroes } from '$lib/scripts/heroes';

	export let pointerEvents = true;
</script>

<div class="flex flex-col gap-2">
	<div class="flex items-center gap-1">
		<img src="/agility.png" alt="" class="w-4 select-none" />
		<span class="flex text-sm uppercase leading-3 text-slate-200">Agility</span>
	</div>
	<div class="flex flex-row flex-wrap gap-1">
		{#each $heroes as hero}
			{#if hero.attribute === 'agility'}
				<div class="h-14 w-8">
					<Hero {hero} {pointerEvents} on:dragstart on:selected />
				</div>
			{/if}
		{/each}
	</div>
</div>
