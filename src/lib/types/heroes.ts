export type Role = 'Initiator' | 'Melee' | 'Ranged' | 'Carry' | 'Nuker' | 'Disabler' | 'Escape' | 'Pusher' | 'Durable' | 'Support';

export type Attribute = 'strength' | 'agility' | 'intelligence';

export type Percentage = `${number}%`;

export type Advantage = {
	name: string;
	advantage: Percentage;
	id: number;
};

export type Disadvantage = {
	name: string;
	disadvantage: Percentage;
	id: number;
};

export type Hero = {
	id: number;
	name: string;
	lowercase_name: string;
	attribute: Attribute;
	roles: Role[];
	winrate: Percentage;
	items: string[];
	lane: {
		name: string;
		presence: Percentage;
	};
	advantage: Advantage[];
	disadvantage: Disadvantage[];
};
