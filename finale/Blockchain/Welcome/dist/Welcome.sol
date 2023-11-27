// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Welcome {

    bool public solved = false;

    function FlagMe(string memory input) public {
        require(keccak256(abi.encodePacked(input)) == keccak256(abi.encodePacked("Welcome to the final !")), "Wrong Answer"); 
        solved = true;
    }
}