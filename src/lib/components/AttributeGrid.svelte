<script lang="ts">
	import HeroPoster from './HeroPoster.svelte';
	import { heroes } from '../scripts/heroes';
	import type { Attribute } from '../types/heroes';

	export let attribute: Attribute;
</script>

<div class="flex flex-col gap-2">
	<div class="flex w-min items-center gap-1">
		<img src="/{attribute}.png" alt={attribute} class="w-4 select-none" />
		<span class="flex text-sm uppercase leading-3 text-slate-200">{attribute}</span>
	</div>
	<div class="flex flex-row flex-wrap gap-1">
		{#each $heroes as hero}
			{#if hero.attribute === attribute}
				<div class="h-14 w-8">
					<HeroPoster {hero} />
				</div>
			{/if}
		{/each}
	</div>
</div>
