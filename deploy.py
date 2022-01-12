from solcx import compile_standard, install_solc

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# compile our Solidity
install_solc("0.6.0")

compile_sol = compile_standard(
    {
        "language": "Solidity",
        "source": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)
print(compile_sol)
