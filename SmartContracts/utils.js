const Web3 = require('web3');

const web3 = new Web3('http://localhost:7545')
//console.log(web3)
const privateKey = 'cfa692c615c0c06381029f64274ca9837439a324a016c224191e136722c71416'
const myAccount = web3.eth.accounts.wallet.add(privateKey)
console.log(myAccount)
//To use the variables in the deploy function, exporting
module.exports = {
    web3: web3,
    myAccount: myAccount
}
