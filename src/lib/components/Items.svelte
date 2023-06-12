<script lang="ts">
	import { toLower } from '../scripts/helpers';
	import type { Percentage, TreeChoice } from '../types/heroes';

	export let items: {
		name: string;
		winrate: Percentage;
	}[];

	let show = false;
</script>

<div class="relative">
	<img
		on:mouseenter={() => (show = true)}
		on:mouseleave={() => (show = false)}
		src="/items.svg"
		alt="tree"
		class="ml-2 h-10 w-10"
	/>

	{#if show}
		<div
			class="pointer-events-none absolute bottom-12 left-7 z-50 flex -translate-x-1/2 flex-col gap-1 rounded-lg bg-slate-700/90 px-4 py-2 text-xs"
		>
			{#each items as item}
				<div class="flex items-center justify-between gap-4">
					<div class="flex min-w-max items-center gap-2">
						<img src="/items/{toLower(item.name)}.jpg" alt={item.name} class="h-7" />
						<span class="flex-nowrap whitespace-nowrap">{item.name}</span>
					</div>
					<span class="whitespace-nowrap">{item.winrate}</span>
				</div>
			{/each}
		</div>
	{/if}
</div>
