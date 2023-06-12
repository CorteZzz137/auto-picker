<script lang="ts">
	import { capFirst } from '../scripts/helpers';
	import { heroes } from '../scripts/heroes';
	import { selectedId } from '../scripts/selectedHeroStore';
	import type { Ability } from '../types/heroes';

	export let ability: Ability;
	export let invokerAbility = false;
	let show = false;
</script>

<img
	on:mouseenter={() => (show = true)}
	on:mouseleave={() => (show = false)}
	src="heroes/images/{$heroes[$selectedId].lowercase_name}/{ability.lowercase_name}.jpg"
	alt={ability.lowercase_name}
	class="h-10 w-10"
/>

{#if show}
	<div
		class="pointer-events-none fixed z-50 {invokerAbility
			? 'bottom-16'
			: 'bottom-44'} max-w-[480px] rounded-lg bg-slate-700/90 px-4 py-2 text-xs"
	>
		{#if ability.effects}
			<div class="flex flex-col text-gray-300">
				{#each ability.effects as effect}
					<span>{capFirst(effect.name)}: {effect.text}</span>
				{/each}
			</div>
			<hr class="my-2" />
		{/if}
		{#if ability.description}
			<div>
				{ability.description}
			</div>
		{/if}
		{#if ability.notes}
			<div class="gaccent-pink-200 mt-2 flex flex-col rounded-md bg-slate-500 p-2">
				{#each ability.notes as note}
					<span>{note}</span>
				{/each}
			</div>
		{/if}
		{#if ability.stats}
			<hr class="my-2" />
			<div class="flex flex-col">
				{#each ability.stats as stat}
					<span>{stat.name}: {stat.text}</span>
				{/each}
			</div>
		{/if}
		{#if ability.cooldown || ability.manacost}
			<hr class="my-2" />
			<div class="flex justify-between">
				<div class={ability.cooldown ? 'visible' : 'invisible'}>
					<span>cooldown: {ability.cooldown ?? 123} sec</span>
				</div>
				<div class={ability.manacost ? 'visible' : 'invisible'}>
					<span>manacost: {ability.manacost ?? 123}</span>
				</div>
			</div>
		{/if}
	</div>
{/if}
