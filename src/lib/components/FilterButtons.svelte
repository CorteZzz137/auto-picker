<script lang="ts">
	import { capFirst } from '../scripts/helpers';
	import { flags, marksId, rolesId } from '../scripts/showFlag';

	let roles = ['carry', 'support'] as const;
	let marks = [
		'melee',
		'ranged',
		'disabler',
		'durable',
		'escape',
		'initiator',
		'nuker',
		'pusher'
	] as const;
</script>

<div class="flex justify-between gap-3 text-slate-300">
	<div class="flex gap-2">
		{#each roles as role}
			<button
				on:click={() => {
					$flags.role ^= rolesId[capFirst(role)];
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
</div>
