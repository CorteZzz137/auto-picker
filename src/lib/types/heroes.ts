export type Role = 'Initiator' | 'Melee' | 'Ranged' | 'Carry' | 'Nuker' | 'Disabler' | 'Escape' | 'Pusher' | 'Durable' | 'Support';

export type Attribute = 'strength' | 'agility' | 'intelligence' | 'all';

export type Percentage = `${number}%`;

export type Counter = {
	id: number;
	name: string;
	disadvantage: Percentage;
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
};
