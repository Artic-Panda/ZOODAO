// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract ERC20TOKEN is ERC20 {
    address public owner;

    constructor(uint256 _initialSupply) ERC20("Test", "TEST") {
        owner = msg.sender;
        _mint(msg.sender, _initialSupply);
    }

    modifier onlyOwner {
        require(msg.sender == owner, "You are not the owner");
        _;
    }

    function burn(address _account, uint256 _amount) external onlyOwner {
        _burn(_account, _amount);
    }

}
