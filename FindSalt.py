from web3 import Web3

def compute_address(deployer_address: str, salt: bytes, creation_code: bytes) -> str:
    prefix = bytes.fromhex('ff')
    deployer = bytes.fromhex(deployer_address[2:])  # remove '0x'
    init_code_hash = Web3.keccak(creation_code)

    packed = prefix + deployer + salt + init_code_hash
    hash_bytes = Web3.keccak(packed)

    address_int = int.from_bytes(hash_bytes, 'big') & ((1 << 160) - 1)
    address_hex = hex(address_int)[2:].zfill(40)

    return f"0x{address_hex}"

DEPLOYER = "0x7FA9385bE102ac3EAc297483Dd6233D62b3e1496"
BASE_CODE = "6080604052348015600e575f5ffd5b5060ce80601a5f395ff3fe6080604052348015600e575f5ffd5b50600436106026575f3560e01c806306fdde0314602a575b5f5ffd5b60306044565b604051603b91906081565b60405180910390f35b5f7f736d617278000000000000000000000000000000000000000000000000000000905090565b5f819050919050565b607b81606b565b82525050565b5f60208201905060925f8301846074565b9291505056fea2646970667358221220 5011bbacc7a6d9c8072de86deb41e0527e64d2b38bb9e1ce561b2d39e54264bd64736f6c634300081c0033"
          #0x6080604052348015600e575f5ffd5b5060ce80601a5f395ff3fe6080604052348015600e575f5ffd5b50600436106026575f3560e01c806306fdde0314602a575b5f5ffd5b60306044565b604051603b91906081565b60405180910390f35b5f7f736d617278000000000000000000000000000000000000000000000000000000905090565b5f819050919050565b607b81606b565b82525050565b5f60208201905060925f8301846074565b9291505056fea2646970667358221220 436935b7976546c2a8833c2f9aa5a9fbffb724800c2f9d600e6d7899bfcb895264736f6c634300081c0033
INIT_CODE = bytes.fromhex(BASE_CODE)
#SALT = bytes.fromhex("0000000000000000000000000000000000000000000000000000000000374346")

# result_address = compute_address(DEPLOYER, SALT, INIT_CODE)
# print(f"Computed address: {result_address}")

print("Start")
i = 0
while True:
    if i % 100000 == 0:
        print(f"Checked {i} values...")

    salt = i.to_bytes(32, 'big')
    address = compute_address(DEPLOYER, salt, INIT_CODE)

    if 'badc0de' in address.lower():
        print(f"\nFound! salt: 0x{salt.hex()}")
        print(f"Address: {address}")
        break

    i += 1
