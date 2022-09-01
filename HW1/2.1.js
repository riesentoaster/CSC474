import { frequencyAnalysis } from './frequencyAnalysis.js'

const encrypted = 'UGRZEJFYVJRKVFERTYRZINZKYYZJWVVKZEKYVRZIKYRKLDSIRXVFLJFCUGVIJFEFWJGRZEKYVIVNRJREFCUDRENYFJRZUNVCCNZC'

const shiftText = (text, amount) =>
  text
    .split('')
    .map(e => (e.charCodeAt(0) - 'A'.charCodeAt(0) + amount) % 26 + 'A'.charCodeAt(0))
    .map(e => String.fromCharCode(e))
    .join('')

const scores = Array(26).fill(0).map((_, i) => shiftText(encrypted, i)).map((e, i) => [i, frequencyAnalysis(e).score]).sort((a, b) => a[1] - b[1])

const guessedShiftAmount = scores[0][0]

console.log('guessed shift amount:', guessedShiftAmount)
console.log('shifted text:', shiftText(encrypted, guessedShiftAmount))
