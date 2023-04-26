<script>
	import EmptyHeroSlot from './EmptyHeroSlot.svelte';
</script>

<div class="flex h-full w-min flex-col gap-2 border border-dashed border-white p-2">
	<span class="text-xl">Ваша команда</span>
	<div class="flex gap-2">
		{#each Array(5) as _hero, i}
			<EmptyHeroSlot id={i} />
		{/each}
	</div>
	<span class="text-xl">Вражеская команда</span>
	<div class="flex gap-2">
		{#each Array(5) as _hero, i}
			<EmptyHeroSlot id={i + 5} />
		{/each}
	</div>
</div>
