const nullIfEmpty = (s: null | undefined | string | unknown[]) => (s == null || s.length === 0) ? null : s
export default nullIfEmpty