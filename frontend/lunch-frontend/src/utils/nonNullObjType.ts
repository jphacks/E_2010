type NonNullObj<T> = { [K in keyof T]: NonNullable<T[K]> }
export default NonNullObj