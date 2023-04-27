<script>
	import { getKeys, isMuted } from '$lib/scripts/helpers';
	import { heroes } from '$lib/scripts/heroes';
	import { selectedIds } from '$lib/scripts/selectedIds';
	import { flags } from '$lib/scripts/showFlag';
	import EmptyHeroSlot from './EmptyHeroSlot.svelte';
	import StaticHero from './StaticHero.svelte';
</script>

<div class="flex h-full w-min flex-col justify-between gap-2 border border-dashed border-white p-2">
	<div class="flex flex-col">
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
	<div class="flex h-full overflow-x-hidden text-gray-200">
		<div class="flex flex-col ">
			<span> Лучший контр-пик </span>
			<div class="flex w-full gap-2 overflow-y-auto">
				{#each getKeys($selectedIds.enemy) as i}
					<div class={i === '4' ? 'w-12' : 'w-16'}>
						{#if $selectedIds.enemy[i] !== -1}
							<div class="flex h-min flex-col gap-2">
								{#each $heroes[$selectedIds.enemy[i]].counters as counter}
									{#if !isMuted($flags, $selectedIds, $heroes[counter.id])}
										<div class="relative h-[60px] w-10">
											<StaticHero hero={$heroes[counter.id]} pointerEvents={false} />
											<span
												class="pointer-events-none absolute left-0 top-0 z-10 text-sm {counter.disadvantage.includes(
													'-'
												)
													? 'text-red-400'
													: 'text-green-400'}"
											>
												{counter.disadvantage}
											</span>
										</div>
									{/if}
								{/each}
							</div>
						{/if}
					</div>
				{/each}
			</div>
		</div>
	</div>
</div>
