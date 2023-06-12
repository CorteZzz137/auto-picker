<script lang="ts">
	import { heroes } from '../scripts/heroes';
	import Ability from './Ability.svelte';

	let show = false;
	const invoker = $heroes[40];
</script>

<button
	on:click={() => (show = !show)}
	class="h-10 w-3 rounded-r-xl bg-gradient-to-b from-blue-500 via-fuchsia-600 to-orange-500"
/>

{#if show}
	<div class="fixed bottom-44 h-14 w-[488px] rounded-lg bg-slate-700/80 p-2 backdrop-blur-sm">
		<div class="flex gap-2">
			{#each invoker.abilities as ability, i}
				{#if i > 3}
					<Ability {ability} invokerAbility={true} />
				{/if}
			{/each}
		</div>
	</div>
{/if}
