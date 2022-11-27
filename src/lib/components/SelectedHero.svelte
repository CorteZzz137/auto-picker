<script lang="ts">
	import { tick } from 'svelte';

	export let src = 'alchemist';
	let video: HTMLVideoElement;
	let source: HTMLSourceElement;

	const handleNewHero = async (s: string) => {
		if (video) video.pause();
		if (source) source.setAttribute('src', s);
		if (video) video.load();
		if (video) video.play();
	};

	$: handleNewHero(src);
</script>

<!-- svelte-ignore a11y-mouse-events-have-key-events -->
<div class="h-28 w-20">
	<video bind:this={video} autoplay loop class="h-full object-fill">
		<source bind:this={source} src="/heroes/videos/{src}.webm" type="video/webm" />
		<track kind="captions" />
	</video>
</div>
