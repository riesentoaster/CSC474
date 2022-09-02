import { getScore, base } from '../frequencyAnalysis.js'

const encrypted = 'VXGDTBDHAWHXEZSHPWDIWACCDHUWECRMZARQGQVDDWFQYGQNDDYAKNMQUGAUDSLAKNBEVWCJLUHSGCKOXGGBDSMJXCXFSJIUXVGJTJRUGXGNEUJWCLDRQSEADLAGJBCYJWRCNHGXCJUQDACCDBDAVNMSWJTJQQVEXAZBOSACDHKSCMDHKGCRMIHAGNCDGVDDAJTQIQDCQKINQYGMHMZYDQEANTMUIRNDGXIQDYFXDALQLADWZDVTNCGUSMGJNVKGGLDHQSCMSXWGRLTBLLWJSXSKPUVQQKTWUUDGENCSJQECNBGYNQDSSDANCYLEPPHSOZTWAHQSCCGQVXXWHIZWSTQQEWGBDDLKXBHJKKTEDDUGERDISFSJSEUDDLJJGGZJBEHQIXGYKKJYDHAGGLZFLSXWZHLZJAGCUUDUKKEZTJCEXLWNEQJWPBSUJFHNBJAGCXEJZWDOEYUWDOMQNSARMJWDARFUFUTOQEELDTXELGLJRXAFVCND'
const maxKeyLength = 15

const getScoresForKeyLength = (keyLength) => Array(keyLength).fill(0).map((_, i) => i)
  .map(rowNumber => encrypted.split('').filter((e, i) => i % keyLength === rowNumber).join(''))
  .map(getScore)

const averageScoreByLength = Array(maxKeyLength - 1).fill(0).map((_, i) => i + 1).map(rowLenght =>
  getScoresForKeyLength(rowLenght)
    .map(score => score[0][1])
    .reduce((acc, cur, i, a) => acc + cur / a.length, 0)
)

const keyLengthWithBestScore = averageScoreByLength.map((e, i) => ([i + 1, e])).sort((a, b) => a[1] - b[1])[0][0]

console.log(getScoresForKeyLength(keyLengthWithBestScore).reduce((acc, cur) => acc + String.fromCharCode(base + 26 - cur[0][0]), ''))
