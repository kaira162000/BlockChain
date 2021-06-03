const {web3, myAccount} = require('./utils')
const {contractAddress, abi} = require('./contractsArtifacts')

let contract = new web3.eth.Contract(JSON.parse(abi), contractAddress)

async function get() {
    let r = await contract.methods.get().call()
    return r;
}

async function set(value) {
    let r = await contract.methods.set(value).send({
        from: myAccount.address,
        gas: 800000
    })
    return r.transactionHash;
}

// get()
// set("hello")
// get()

window.addEventListener('load',()=>{
    document.getElementById("get").onclick = () => {
        get().then((r) => {
            document.getElementById("resultOfGet").innerHTML = r
        })
    }
    document.getElementById("set").onclick = () => {
        var val = document.getElementById("value").value
        set(val).then((r)=>{
            document.getElementById("resultOfSet").innerHTML = r
        })
    }
})
