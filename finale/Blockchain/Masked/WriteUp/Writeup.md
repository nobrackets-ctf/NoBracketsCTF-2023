# K.L.M - BLOCKCHAIN - Masked

## Description

On corse la course, il faut maintenant retrouver le code masqué du contrat ^^

## Solve

### Step 1: Récupération du bytecode

Ici, on va utiliser foundry afin de retrouver le code du contrat, nous avons son adresse alors on va se faire plaisir...
```bash
cast code $TARGET
``` 
Ce qui nous renvoie le bytecode suivant :

```0x608060405234801561000f575f80fd5b506004361061004a575f3560e01c80635bc60cfc1461004e57806362a094771461006a578063799320bb14610074578063ff1b636d14610092575b5f80fd5b61006860048036038101906100639190610211565b6100b0565b005b610072610163565b005b61007c6101a5565b6040516100899190610256565b60405180910390f35b61009a6101b5565b6040516100a791906102ae565b60405180910390f35b5f60019054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161461013f576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161013690610321565b60405180910390fd5b4281036101605760015f806101000a81548160ff0219169083151502179055505b50565b335f60016101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550565b5f8054906101000a900460ff1681565b5f60019054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b5f80fd5b5f819050919050565b6101f0816101de565b81146101fa575f80fd5b50565b5f8135905061020b816101e7565b92915050565b5f60208284031215610226576102256101da565b5b5f610233848285016101fd565b91505092915050565b5f8115159050919050565b6102508161023c565b82525050565b5f6020820190506102695f830184610247565b92915050565b5f73ffffffffffffffffffffffffffffffffffffffff82169050919050565b5f6102988261026f565b9050919050565b6102a88161028e565b82525050565b5f6020820190506102c15f83018461029f565b92915050565b5f82825260208201905092915050565b7f594f55205348414c4c204e4f542052554c45205448495320434f4e54524143545f82015250565b5f61030b6020836102c7565b9150610316826102d7565b602082019050919050565b5f6020820190508181035f830152610338816102ff565b905091905056fea2646970667358221220a2b6748761762d0c39d63f3d1e1b8c21e2c427390456528954021e6728067f9264736f6c63430008160033```

on pars donc sur notre decompileur preféré : https://library.dedaub.com/decompile

### Step 2: Analyse du code

```solidity
function win(uint256 varg0) public payable { 
    require(4 + (msg.data.length - 4) - 4 >= 32);
    require(varg0 == varg0);
    require(msg.sender == _changeOwner, Error('YOU SHALL NOT RULE THIS CONTRACT'));
    if (!(varg0 - block.timestamp)) {
        _solved = 1;
    }
}
```
On remarque ici qu'il faut rentrer le timestamp du block en input mais qu'il faut également que nous ayons le rôle "changeOwner".

```solidity
function changeOwner() public payable { 
    _changeOwner = msg.sender;
}
```
Heureusement, la fonction changeOwner() n'est pas protégée nous pouvons donc l'appeler simplement.

```bash
cast send $TAR "changeOwner()" --rpc-url=$RPC --private-key=$PK
```
Désormais, nous sommes propriétaires du contrat. Nous devons maintenant trouver le timestamp et l'entrer dans la fonction.

### Step 3: Solve

Afin de simplifier ce solve, nous allons devoir écrire un contrat qui le fait automatiquement pour nous.
```solidity
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
```

Plus qu'à appeler la fonction "Win()"

K.L.M
