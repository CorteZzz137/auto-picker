<script lang="ts">
	import { input } from '../scripts/input';
	import AttributeGrid from './AttributeGrid.svelte';
	import FilterButtons from './FilterButtons.svelte';
</script>

<div class="relative flex aspect-video flex-col gap-3 px-10 py-6">
	<div class="flex">
		<AttributeGrid attribute={'strength'} />
		<AttributeGrid attribute={'agility'} />
	</div>
	<div class="flex">
		<AttributeGrid attribute={'intelligence'} />
		<AttributeGrid attribute={'all'} />
	</div>
	<FilterButtons />
	<input
		type="text"
		class="absolute right-1/2 top-4 w-[256px] -translate-x-[22px] rounded-sm bg-slate-800/80 text-cyan-50"
		bind:value={$input}
	/>
</div>
