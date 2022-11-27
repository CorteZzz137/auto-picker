import type { Tweened } from 'svelte/motion';

type draggableProps = {
	coords: Tweened<{ x: number; y: number }>;
	staticHero: boolean;
};

export default function drag(node: HTMLDivElement, props: draggableProps) {
	let x: number;
	let y: number;

	let globalDX: number;
	let globalDY: number;

	let { coords, staticHero } = props;

	function handleMousedown(e: MouseEvent) {
		globalDX = 0;
		globalDY = 0;
		x = e.clientX;
		y = e.clientY;

		document.addEventListener('mousemove', handleMousemove);
		document.addEventListener('mouseup', handleMouseup);
	}

	function handleMousemove(e: MouseEvent) {
		const dx = e.clientX - x;
		const dy = e.clientY - y;
		globalDX += dx;
		globalDY += dy;
		x = e.clientX;
		y = e.clientY;
		if (staticHero && (Math.abs(globalDX) > 5 || Math.abs(globalDY) > 5)) {
			node.dispatchEvent(
				new CustomEvent('dragstart', {
					detail: { x, y }
				})
			);
			return;
		}
		coords.update((coords) => {
			return { x: coords.x + dx, y: coords.y + dy };
		});
	}

	function handleMouseup(e: MouseEvent) {
		document.removeEventListener('mousemove', handleMousemove);
		document.removeEventListener('mouseup', handleMouseup);
	}

	node.addEventListener('mousedown', handleMousedown);
	return {
		destroy() {},
		update(newProps: draggableProps) {
			if (staticHero !== newProps.staticHero) staticHero = newProps.staticHero;
		}
	};
}
