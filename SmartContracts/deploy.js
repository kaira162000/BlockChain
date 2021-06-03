const{web3, myAccount} = require('./utils')
const {bytecode} = require('./contractsArtifacts')

async function deploy() {

    //the transaction object would be broadcasted into the network
    await web3.eth.sendTransaction({
        from: myAccount.address,
        gas: 800000,
        data: bytecode
    }).on('receipt',console.log)
}

deploy()