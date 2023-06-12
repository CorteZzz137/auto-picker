<script>
	import Counters from './Counters.svelte';
	import HeroSlot from './HeroSlot.svelte';
</script>

<div class="flex h-full w-min flex-col justify-between gap-2 p-2">
	<div class="flex flex-col">
		<span class="text-xl">Ваша команда</span>
		<div class="flex gap-2">
			{#each Array(5) as _hero, i}
				<HeroSlot id={i} />
			{/each}
		</div>
		<span class="text-xl">Вражеская команда</span>
		<div class="flex gap-2">
			{#each Array(5) as _hero, i}
				<HeroSlot id={i + 5} />
			{/each}
		</div>
	</div>
	<Counters />
</div>
