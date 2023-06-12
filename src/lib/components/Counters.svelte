<script lang="ts">
	import { getKeys, isMuted } from '../scripts/helpers';
	import { heroes } from '../scripts/heroes';
	import { input } from '../scripts/input';
	import { selectedIds } from '../scripts/selectedIds';
	import { flags } from '../scripts/showFlag';
	import HeroPoster from './HeroPoster.svelte';
</script>

<div class="flex h-full overflow-x-hidden text-gray-200">
	<div class="flex flex-col">
		<span> Лучший контр-пик </span>
		<div class="flex w-full gap-2 overflow-y-auto">
			{#each getKeys($selectedIds.enemy) as i}
				<div class={`${i}` === '4' ? 'w-12' : 'w-16'}>
					{#if $selectedIds.enemy[i] !== -1}
						<div class="flex h-min flex-col gap-2">
							{#each $heroes[$selectedIds.enemy[i]].counters as counter}
								{#if !isMuted($flags, $selectedIds, $input, $heroes[counter.id])}
									<div class="relative h-[60px] w-10">
										<HeroPoster
											hero={$heroes[counter.id]}
											pointerEvents={false}
										/>
										<div
											class="pointer-events-none absolute top-3/4 z-10 flex w-full justify-center
                                                 bg-black/70 text-xs font-bold {counter.disadvantage.includes(
												'-'
											)
												? 'text-red-500'
												: 'text-green-400'}"
										>
											{counter.disadvantage}
										</div>
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
