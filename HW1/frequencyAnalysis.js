const englishLetterFrequencies = { E: 0.13, T: 0.091, A: 0.082, O: 0.075, I: 0.07, N: 0.067, S: 0.063, H: 0.061, R: 0.06, D: 0.043, L: 0.04, C: 0.028, U: 0.028, M: 0.024, W: 0.024, F: 0.022, G: 0.02, Y: 0.02, P: 0.019, B: 0.015, V: 0.0098, K: 0.0077, J: 0.0015, X: 0.0015, Q: 0.00095, Z: 0.00074 }

export const frequencyAnalysis = (text) => {
  const count = Array(26).fill(0).map((_, i) => ({ [String.fromCharCode('A'.charCodeAt(0) + i)]: 0 })).reduce((acc, cur) => Object.assign(acc, cur), {})
  text.split('').forEach(e => count[e]++)
  const frequencies = Object.entries(count).sort((a, b) => b[1] - a[1]).map(([k, v], i, a) => ([k, v / text.length]))
  const score = Object.entries(englishLetterFrequencies).map(([k, v], i) => v * Math.abs(i - frequencies.map(e => e[0]).indexOf(k))).reduce((acc, cur) => acc + cur, 0)
  return { count, frequencies, score }
}
