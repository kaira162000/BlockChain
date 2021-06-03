// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract SampleContract{
    string value;
    //constructor function
    constructor(){
        value = "initial";
    }

    //reading a value
    function get() public view returns(string memory) {
        return value;
    }
    //set the value
    function set(string memory _value) public {
        value = _value;
    }
}