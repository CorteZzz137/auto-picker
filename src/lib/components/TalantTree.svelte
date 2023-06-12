<script lang="ts">
	import type { TreeChoice } from '../types/heroes';

	export let tree: TreeChoice[];
	let show = false;
	const levels = [25, 20, 15, 10] as const;
</script>

<div class="relative">
	<img
		on:mouseenter={() => (show = true)}
		on:mouseleave={() => (show = false)}
		src="/talents.svg"
		alt="tree"
		class="ml-2 h-10 w-10"
	/>
	{#if show}
		<div
			class="absolute bottom-12 left-7 flex -translate-x-1/2 gap-4 bg-slate-700/90 p-2 text-xs"
		>
			<div class="relative flex">
				<div
					class="absolute -top-2 right-[26px] flex flex-col gap-3 rounded-l-lg bg-slate-700/90 p-2"
				>
					{#each levels as _level, i}
						<div class="relative flex justify-end gap-2 whitespace-nowrap">
							<span>{tree[i].left.name}</span>
							<div
								style="width: {tree[i].left.pickrate}"
								class="absolute right-0 top-0 h-full w-1/2 {parseFloat(
									tree[i].left.pickrate.split('%')[0]
								) > 50
									? 'bg-green-500/50'
									: 'bg-green-500/20'}"
							/>
						</div>
					{/each}
				</div>
				<div class="flex flex-col gap-2">
					{#each levels as level}
						<div class="flex justify-end gap-2 whitespace-nowrap">
							<span
								class="h-[19px] w-[19px] rounded-full border border-white/50 text-center"
							>
								{level}
							</span>
						</div>
					{/each}
				</div>
				<div
					class="absolute -top-2 left-[26px] flex flex-col gap-3 rounded-r-lg bg-slate-700/90 p-2"
				>
					{#each levels as _level, i}
						<div class="relative flex gap-2 whitespace-nowrap">
							<span>{tree[i].right.name}</span>
							<div
								style="width: {tree[i].right.pickrate}"
								class="absolute left-0 top-0 h-full w-1/2 {parseFloat(
									tree[i].right.pickrate.split('%')[0]
								) > 50
									? 'bg-green-500/50'
									: 'bg-green-500/20'}"
							/>
						</div>
					{/each}
				</div>
			</div>
		</div>
	{/if}
</div>
