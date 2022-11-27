<script lang="ts">
	import Agility from '$lib/components/Agility.svelte';
	import Intelligence from '$lib/components/Intelligence.svelte';
	import Strength from '$lib/components/Strength.svelte';
	import type { Hero } from '$lib/types/heroes';

	export let heroes: Hero[];
	export let pointerEvents = true;
</script>

<div class="flex flex-col gap-3 px-10 py-8">
	<Strength on:selected on:dragstart {heroes} {pointerEvents} />
	<Agility on:selected on:dragstart {heroes} {pointerEvents} />
	<Intelligence on:selected on:dragstart {heroes} {pointerEvents} />
</div>
