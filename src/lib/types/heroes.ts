export type Role =
	| 'Initiator'
	| 'Melee'
	| 'Ranged'
	| 'Carry'
	| 'Nuker'
	| 'Disabler'
	| 'Escape'
	| 'Pusher'
	| 'Durable'
	| 'Support';

export type Attribute = 'strength' | 'agility' | 'intelligence' | 'all';

export type Percentage = `${number}%`;

export type Counter = {
	id: number;
	name: string;
	disadvantage: Percentage;
};

export type Ability = {
	name: string;
	lowercase_name: string;
	effects: { name: string; text: string }[];
	description: string;
	notes: string[];
	stats: { name: string; text: string }[];
	cooldown: string;
	manacost: string;
	lore: string;
};

export type BaseAttribute = { base: string; increment: string };

export type TreeChoice = {
	left: { name: string; pickrate: Percentage };
	right: { name: string; pickrate: Percentage };
};

export type Hero = {
	id: number;
	name: string;
	lowercase_name: string;
	attribute: Attribute;
	roles: Role[];
	winrate: Percentage;
	items: {
		name: string;
		winrate: Percentage;
	}[];
	lane: {
		name: string;
		winrate: Percentage;
	}[];
	counters: Counter[];
	abilities: Ability[];
	tree: TreeChoice[];
	attributes: {
		main: {
			str: BaseAttribute;
			agi: BaseAttribute;
			int: BaseAttribute;
		};
		other: {
			movespeed: string;
			armor: string;
			attack_time: string;
			damage: string;
		};
	};
	ability_build: number[];
	main_abilities: string[];
};
