// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Void {

    bool public solved = false;

    function FlagMe(bytes[] memory _guess) public {
        for (uint i = 0; i < _guess.length; i++) {
            // Can my bytes be 1,2 and 3 at the same time ?
            require(keccak256(_guess[i]) == keccak256("1"),"Check1 not passed");
            require(keccak256(_guess[i]) == keccak256("2"),"Check2 not passed");
            require(keccak256(_guess[i]) == keccak256("3"),"Check3 not passed");
        }
        solved = true;
    }
}
