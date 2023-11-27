# K.L.M - BLOCKCHAIN - Void

## Description

Bienvenus dans le merveilleux monde du web3. Ce challenge est un challenge de logique, jespère qu'il ne vous a pas trop pris la tête.

## Contract

```Solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Void {

    bool public solved;

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
```

### Step 1: Lecture du contrat

Dans ce contrat, on remarque qu'il y a trois checks... chaque bytes que nous passons doivent être égaux à 1, 2 et 3 en même temps. Ce qui est impossible. Mais que se passerait-il si nous passions un tableau vide ?? i serait directement inférieur à la taille du tableau, alors on passerait directement à la fonction qui agit sur le booléen. 

### Step 2: Solve

Deux façons possibles (que j'ai effectué) :

```bash
cast send $TAR "FlagMe(bytes[])" [] --rpc-url=$RPC --private-key=$PK
```
ou alors ajouter le RPC à Metamask, connecter Metamask à RemixIDE, importer le contrat puis solve avec l'interface directement.

K.L.M
