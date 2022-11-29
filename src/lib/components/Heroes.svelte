<script lang="ts">
	import Agility from '$lib/components/Agility.svelte';
	import Intelligence from '$lib/components/Intelligence.svelte';
	import Strength from '$lib/components/Strength.svelte';
	import type { Hero } from '$lib/types/heroes';

	export let heroes: Hero[];
	export let pointerEvents = true;
	let onlyCarry = false;
	let onlySupport = false;
</script>

<div class="flex aspect-video flex-col gap-3 px-10 py-6">
	<Strength on:selected on:dragstart {heroes} {pointerEvents} {onlyCarry} {onlySupport} />
	<Agility on:selected on:dragstart {heroes} {pointerEvents} {onlyCarry} {onlySupport} />
	<Intelligence on:selected on:dragstart {heroes} {pointerEvents} {onlyCarry} {onlySupport} />
	<div class="flex gap-3 text-slate-300">
		<button
			on:click={() => {
				onlyCarry = !onlyCarry;
			}}
			class={!onlyCarry ? 'opacity-50' : ''}>carry</button
		>
		<button
			on:click={() => {
				onlySupport = !onlySupport;
			}}
			class={!onlySupport ? 'opacity-50' : ''}>support</button
		>
	</div>
</div>
