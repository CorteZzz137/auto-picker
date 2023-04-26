<script lang="ts">
	import { capFirst } from '$lib/scripts/helpers';
	import { flags, marksId, rolesId } from '$lib/scripts/showFlag';
	import type { IntRange } from '$lib/scripts/helpers';

	let roles = ['carry', 'support'] as const;
	let marks = ['melee', 'ranged', 'disabler', 'durable', 'escape', 'initiator', 'nuker', 'pusher'] as const;
</script>

<div class="flex justify-between gap-3 text-slate-300">
	<div class="flex gap-2">
		{#each roles as role}
			<button
				on:click={() => {
					flags.update((prev) => {
						prev.role ^= rolesId[capFirst(role)];
						console.log(prev.role, capFirst(role));
						return prev;
					});
				}}
				class={$flags.role & rolesId[capFirst(role)] ? '' : 'opacity-50'}
			>
				{role}
			</button>
		{/each}
	</div>
	<div class="flex gap-2">
		{#each marks as mark}
			<button
				on:click={() => {
					$flags.marks ^= marksId[capFirst(mark)];
				}}
				class={$flags.marks & marksId[capFirst(mark)] ? '' : 'opacity-50'}
			>
				{mark}
			</button>
		{/each}
	</div>

	<!-- <button
		on:click={() => {
			onlySupport = !onlySupport;
		}}
		class={!onlySupport ? 'opacity-50' : ''}>support</button
	> -->
</div>
