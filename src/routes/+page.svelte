<script lang="ts">
	import Heroes from '$lib/components/Heroes.svelte';
	import { invoke } from '@tauri-apps/api/tauri';
	import { onMount } from 'svelte';
	import type { Hero } from '$lib/types/heroes';
	import DynamicHero from '$lib/components/DynamicHero.svelte';
	import PickComponent from '$lib/components/PickComponent.svelte';
	import { heroes } from '$lib/scripts/heroes';
	import { selectedId } from '$lib/scripts/selectedHeroStore';
	import { flags } from '$lib/scripts/showFlag';
</script>

<div class="grid grid-cols-[71vw_29vw] grid-rows-[71vh_29vh]">
	<Heroes />
	<div class="row-start-2 h-full border border-dashed border-white">
		<DynamicHero hero={$heroes[$selectedId]} border={false} />
	</div>
	<div class="col-start-2 row-span-2 mx-auto text-gray-200">
		<PickComponent />
	</div>
</div>
