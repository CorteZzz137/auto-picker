<script lang="ts">
	import Heroes from './lib/components/Heroes.svelte';
	import { heroes } from './lib/scripts/heroes';
	import { onMount } from 'svelte';
	import { invoke } from '@tauri-apps/api/tauri';
	import PickComponent from './lib/components/PickComponent.svelte';
	import { selectedId } from './lib/scripts/selectedHeroStore';
	import SelectedHeroInfo from './lib/components/SelectedHeroInfo.svelte';

	onMount(async () => {
		let test = await invoke('get_heroes');
		heroes.update(() => JSON.parse(test as string));
	});
</script>

<div class="grid grid-cols-[71vw_29vw] grid-rows-[71vh_29vh]">
	<Heroes />

	<div class="col-span-2 row-start-2 h-full w-full bg-cyan-950/[0.35] p-4 text-cyan-50">
		{#if $heroes[$selectedId]}
			<SelectedHeroInfo />
		{/if}
	</div>
	<div class="col-start-2 mx-auto text-gray-200">
		<PickComponent />
	</div>
</div>
