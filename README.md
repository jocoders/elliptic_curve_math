# Elliptic Curve Max

Elliptic Curve Max is a Python-based project designed for working with elliptic curve cryptography. This project includes various helper functions to perform mathematical operations and cryptographic computations. The primary focus of this project is on elliptic curve calculations, such as key generation, signing messages, and verifying signatures.

## Features

- **Elliptic Curve Cryptography**: Implements cryptographic functionalities using elliptic curves.
- **Key Generation**: Generates private and public key pairs using NIST P-521 elliptic curve.
- **Message Signing**: Provides functionality to digitally sign messages.
- **Signature Verification**: Verifies the authenticity of messages using their signatures.

## Technologies Used

- **Python**: Core programming language.
- **ECDSA Library**: For elliptic curve operations using standards like NIST P-521.

## Code Examples

Below is an example of how the functions can be used in the project.

### Generate Keys
```python
from ecdsa import SigningKey, NIST521p

# Generate private and public keys
private_key = SigningKey.generate(curve=NIST521p)
public_key = private_key.verifying_key

print("Private Key:", private_key.to_string().hex())
print("Public Key:", "04" + public_key.to_string().hex())  # "04" prefix for uncompressed format
```

### Sign a Message
```python
def sign_message(message, private_key):
    return private_key.sign(message.encode('utf-8'))

# Example usage
message = "Sign this message!"
signature = sign_message(message, private_key)
print("Signature:", signature.hex())
```

### Verify a Signature
```python
def verify_message(message, signature, public_key):
    return public_key.verify(signature, message.encode('utf-8'))

# Example usage
verified = verify_message(message, signature, public_key)
print("Verified:", verified)
```

### Example Output

Here is an example output when running the code:

```json
{
  "message": "Sign this message!",
  "public_key": "04<your-public-key-hex-value>",
  "signature": "<your-signature-hex-value>"
}
```

The `Verified` output will either be `True` or `False`, indicating whether the signature is valid for the given message.

## How to Run

1. Install the required dependencies:
   ```bash
   pip install ecdsa
   ```

2. Run the Python script:
   ```bash
   python your_script_file.py
   ```

## Future Enhancements

- Add support for other elliptic curves.
- Implement advanced cryptographic schemes like ECDH (Elliptic Curve Diffie-Hellman).
- Introduce error handling and extended unit tests for higher reliability.

## Contributing

Contributions are welcome! If you're interested in optimizing existing features or adding new ones, feel free to open an issue or submit a pull request.

## Licensing

This project is licensed under the MIT License. See the LICENSE file for more information.
