# K.L.M - BLOCKCHAIN - Welcome

## Description

Bienvenus dans le merveilleux monde du web3. Ce challenge est un challenge d'introduction afin de vous faire découvrir ce qui rend mes journées palpitantes ^^.

## Contract

```Solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Welcome {

    bool public solved;

    function FlagMe(string memory input) public {
        require(keccak256(abi.encodePacked(input)) == keccak256(abi.encodePacked("Welcome to the final !")), "Wrong Answer"); 
        solved = true;
    }
}
```

### Step 1: Lecture du contrat

Dans ce contrat, on remarque directement la fonction FlagMe() qui permet de passer le booléen "solve" à True. Vu que c'est notre objectif, nous allons essayer d'appeler cette fonction. Elle prend en entrée une chaine de caractères et la compare à la chaine suivante : "Welcome to the final !".

### Step 2: Solve

Deux façons possibles (que j'ai effectué) :

```bash
cast send $TAR "FlagMe(String)" "Welcome to the final !" --rpc-url=$RPC --private-key=$PK
```
ou alors ajouter le RPC à Metamask, connecter Metamask à RemixIDE, importer le contrat puis solve avec l'interface directement.

K.L.M
