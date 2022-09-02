import { getMostProbableShiftCount, shiftText, base } from '../frequencyAnalysis.js'

const encrypted = 'UGRZEJFYVJRKVFERTYRZINZKYYZJWVVKZEKYVRZIKYRKLDSIRXVFLJFCUGVIJFEFWJGRZEKYVIVNRJREFCUDRENYFJRZUNVCCNZC'

const mostProbableShiftCount = getMostProbableShiftCount(encrypted)

console.log('guessed shift amount:', 26 - mostProbableShiftCount)
console.log('guessed key:', String.fromCharCode(base + 26 - mostProbableShiftCount))
console.log('shifted text:', shiftText(encrypted, mostProbableShiftCount))
