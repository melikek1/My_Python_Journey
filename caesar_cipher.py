# A complete Caesar Cipher algorithm with encryption and decryption wrapper functions.
# Demonstrates string manipulation, default parameters, and basic cryptography concepts.

def caesar(text, shift, encrypt=True):
    # Input validation for the shift parameter
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Reverse the shift if decryption is requested
    if not encrypt:
        shift = -shift
        
    # Create the shifted alphabet and translation table
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    
    return text.translate(translation_table)

# Wrapper function for easy encryption
def encrypt(text, shift):
    return caesar(text, shift)

# Wrapper function for easy decryption
def decrypt(text, shift):
    return caesar(text, shift, False)

# --- Example Usage ---
secret_message = "Courage is found in unlikely places."
print("Original:", secret_message)

# Encrypt the message
encrypted_message = encrypt(secret_message, 5)
print("Encrypted:", encrypted_message)

# Decrypt the message back to normal
decrypted_message = decrypt(encrypted_message, 5)
print("Decrypted:", decrypted_message)
