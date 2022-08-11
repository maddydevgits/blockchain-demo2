// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;
pragma experimental ABIEncoderV2;

contract demo {
  
  string[] m; // state variable (hi - 2), (hello - 5)
  address owner;

  constructor() public { // constructor will be called only when this contract is deployed
    owner=msg.sender; // the person who sends the msg is owner
  }

  modifier onlyOwner() { // function modifier
    require(msg.sender==owner); // owner - 1st wallet, and non-owner (user - 2nd wallet)
    _;
  }

  // a function to store a message
  function insertMessage(string memory a) public onlyOwner {
    m.push(a); // assign value of a to m
  }

  // a function to read a message
  function readMessage() public view onlyOwner returns(string[] memory) {
    return(m);
  }

}
