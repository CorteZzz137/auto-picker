<script lang="ts">
	import type { Hero } from '$lib/types/heroes';

	export let hero: Hero;
</script>

<video
	poster="/heroes/images/{hero.lowercase_name}.jpg"
	src="/heroes/videos/{hero.lowercase_name}.webm"
	class="h-full object-fill"
	autoplay
	loop
>
	<track kind="captions" />
</video>
