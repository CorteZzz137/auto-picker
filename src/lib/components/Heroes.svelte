<script lang="ts">
	import Agility from '$lib/components/Agility.svelte';
	import Intelligence from '$lib/components/Intelligence.svelte';
	import Strength from '$lib/components/Strength.svelte';
	import FilterButtons from './FilterButtons.svelte';

	let onlyCarry = false;
	let onlySupport = false;
</script>

<div class="flex aspect-video flex-col gap-3 px-10 py-6">
	<Strength />
	<Agility />
	<Intelligence />
	<FilterButtons />
</div>
