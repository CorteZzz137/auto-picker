type Enumerate<N extends number, Acc extends number[] = []> = Acc['length'] extends N ? Acc[number] : Enumerate<N, [...Acc, Acc['length']]>;

export type IntRange<F extends number, T extends number> = Exclude<Enumerate<T>, Enumerate<F>>;

export function capFirst<T extends string>(str: T): Capitalize<T> {
	return (str[0].toUpperCase() + str.slice(1, str.length)) as Capitalize<T>;
}
