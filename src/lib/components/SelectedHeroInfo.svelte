<script lang="ts">
	import { heroes } from '../scripts/heroes';
	import { selectedId } from '../scripts/selectedHeroStore';
	import DynamicHeroPoster from './DynamicHeroPoster.svelte';
	import Ability from './Ability.svelte';
	import TalantTree from './TalantTree.svelte';
	import Items from './Items.svelte';
	import InvokerSkillsButton from './InvokerSkillsButton.svelte';
	import { toLower } from '../scripts/helpers';

	const baseAttributes = ['strength', 'agility', 'intelligence'] as const;
</script>

<div class="relative flex justify-between">
	<div class="relative flex gap-2">
		<div class="h-[168px] w-[120px]">
			<DynamicHeroPoster
				hero={$heroes[$selectedId]}
				border={false}
				bigPoster={true}
				namePos={'top'}
			/>
		</div>
		<div
			class="absolute top-full my-auto flex w-[120px] -translate-y-full flex-col gap-1 bg-black/50 px-2 py-1"
		>
			{#each baseAttributes as baseAttribute}
				<div class="flex gap-2">
					<img
						src="/{baseAttribute}.png"
						alt={baseAttribute.substring(0, 3)}
						class="h-5 w-5"
					/>
					<span>
						{$heroes[$selectedId].attributes.main[baseAttribute.substring(0, 3)].base} +{$heroes[
							$selectedId
						].attributes.main[baseAttribute.substring(0, 3)].increment}
					</span>
				</div>
			{/each}
		</div>
		<div class="flex flex-col gap-2">
			<div class="flex gap-3">
				{#each $heroes[$selectedId].roles as role}
					<span>
						{role}
					</span>
				{/each}
			</div>
			<div class="flex">
				{#if $heroes[$selectedId].name !== 'Invoker'}
					<div class="flex gap-2">
						{#each $heroes[$selectedId].abilities as ability}
							{#if ability.name !== 'APPLICATION DAMAGE:'}
								<Ability {ability} />
							{/if}
						{/each}
					</div>
				{:else}
					<div class="flex gap-2">
						{#each $heroes[$selectedId].abilities as ability, i}
							{#if i < 4}
								<Ability {ability} />
							{/if}
						{/each}
					</div>
					<InvokerSkillsButton />
				{/if}
				<TalantTree tree={$heroes[$selectedId].tree} />
				<Items items={$heroes[$selectedId].items} />
			</div>
			<div class="flex flex-col">
				<span>
					Movement speed: {$heroes[$selectedId].attributes.other.movespeed}
				</span>
				<span>Armor: {$heroes[$selectedId].attributes.other.armor}</span>
				<span>Attack time: {$heroes[$selectedId].attributes.other.attack_time}</span>
				<span>Base damage: {$heroes[$selectedId].attributes.other.damage}</span>
			</div>
		</div>
	</div>
	<div class="my-auto flex h-full flex-col gap-[2px]">
		{#each $heroes[$selectedId].main_abilities as ability, i}
			<div class="flex gap-[2px]">
				<img
					src="/heroes/images/{$heroes[$selectedId].lowercase_name}/{toLower(
						ability
					)}.jpg"
					alt={ability}
					class="h-[26px] w-[26px]"
				/>
				{#each $heroes[$selectedId].ability_build as build, j}
					<div
						class="flex h-[26px] w-[26px] items-center justify-center ring-1 ring-inset {build ===
						i + 1
							? 'bg-cyan-600/30'
							: ''}"
					>
						{build === i + 1 ? j + 1 : ''}
					</div>
				{/each}
			</div>
		{/each}
		<div class="flex gap-[2px]">
			{#if $heroes[$selectedId].ability_build.reduce((prev, cur) => prev || cur > $heroes[$selectedId].main_abilities.length, false)}
				<img src="/talents.svg" alt="tree" class="h-[26px] w-[26px]" />
				{#each $heroes[$selectedId].ability_build as build, j}
					<div
						class="flex h-[26px] w-[26px] items-center justify-center ring-1 ring-inset {build >
						$heroes[$selectedId].main_abilities.length
							? 'bg-cyan-600/30'
							: ''}"
					>
						{build > $heroes[$selectedId].main_abilities.length ? j + 1 : ''}
					</div>
				{/each}
			{/if}
		</div>
	</div>
</div>
