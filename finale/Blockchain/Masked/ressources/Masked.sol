// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Masked {

    bool public solved = false;
    address public Admin;

    modifier OnlyAdmin{
        require(msg.sender == Admin, "YOU SHALL NOT RULE THIS CONTRACT");
        _;
    }

    function Win(uint guess) OnlyAdmin public {
        if (guess == block.timestamp){
            solved = true;
        }
    }

    function changeOwner() public {
        Admin = msg.sender;
    }
}
