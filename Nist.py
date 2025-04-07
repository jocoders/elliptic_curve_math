import json
from ecdsa import SigningKey, NIST521p

# Generate keys
private_key = SigningKey.generate(curve=NIST521p)
public_key = private_key.verifying_key

# print("Private Key:", private_key.to_string().hex())
# print("Public Key:", public_key.to_string().hex())

def sign_message(message, private_key):
    return private_key.sign(message.encode('utf-8'))

def verify_message(message, signature, public_key):
    return public_key.verify(signature, message.encode('utf-8'))


# Create message and signature
message = "Sign this message!"
signature = sign_message(message, private_key)

output = {
    "message": message,
    "public_key": "04" + public_key.to_string().hex(),  # "04" prefix for uncompressed format
    "signature": signature.hex()
}

print(json.dumps(output, indent=2))

verified = verify_message(message, signature, public_key)
print("Verified:", verified)




