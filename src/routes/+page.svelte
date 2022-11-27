<script lang="ts">
	import Heroes from '$lib/components/Heroes.svelte';
	import SelectedHero from '$lib/components/SelectedHero.svelte';
	import { invoke } from '@tauri-apps/api/tauri';
	import { onDestroy, onMount } from 'svelte';
	import type { Hero } from '$lib/types/heroes';
	import DynamicHero from '$lib/components/DynamicHero.svelte';

	export let data: { heroes: Hero[] };

	let selectedId = 0;
	let pointerEvents = true;
	let greetMsg = '';

	async function greet() {
		// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
		greetMsg = await invoke('greet', { name: 'CorteZzz137' });
	}

	$: if (greetMsg) console.log(greetMsg);

	onMount(async () => {
		await greet();
		if (window) window.addEventListener('herodragstart', handleDragstart as EventListener);
		if (window) window.addEventListener('herodragend', handleDragend as EventListener);
	});

	onDestroy(() => {
		//if (window) window.removeEventListener('herodragstart', handleDragstart as EventListener);
	});

	const handleDragstart = (e: CustomEvent) => {
		console.log('start', e.detail);
		pointerEvents = false;
	};

	const handleDragend = (e: CustomEvent) => {
		console.log('end', e.detail);
		pointerEvents = true;
	};
</script>

<div class="grid grid-cols-[905px_auto] grid-rows-[auto_auto]">
	<Heroes
		heroes={data.heroes}
		{pointerEvents}
		on:selected={(e) => {
			selectedId = e.detail;
		}}
		on:dragstart={(e) => {
			console.log(e.detail);
		}}
	/>
	<div class="row-start-2 p-10">
		<DynamicHero hero={data.heroes[selectedId]} border={false} />
	</div>
</div>
