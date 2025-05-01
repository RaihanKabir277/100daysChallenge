
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(original_text, shift_amount):
#     encrypted_text = ""
#     for letter in original_text:
#         # find = alphabet.index(letter)
#         # find += shift_amount
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)

#         encrypted_text += alphabet[shifted_position]

#     print(f"Here is the encoded text : {encrypted_text}")

# def decrypt(original_text, shift_amount):
#     decrypted_text = ""
#     for letter in original_text:
#         # find = alphabet.index(letter)
#         # find += shift_amount
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)

#         decrypted_text += alphabet[shifted_position]

#     print(f"Here is the encoded text : {decrypted_text}")


# encrypt(text,shift)
# decrypt(text,shift)

def caesar(original_text, shift_amount, encode_or_decode):
    encrypted_decrypted_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
            
    elif encode_or_decode == "encode":
        shift_amount *= +1
    
            
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)

            encrypted_decrypted_text += alphabet[shifted_position]
        else:
            encrypted_decrypted_text += letter
        

    print(f"Here is the {encode_or_decode}d text : {encrypted_decrypted_text}")

# caesar(text, shift, direction)


# while True:
#     again = input("Enter Yes if you want to again otherwise enter No :\n").lower()
#     if again == "yes":
#         direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#         text = input("Type your message:\n").lower()
#         shift = int(input("Type the shift number:\n"))
#         caesar(text, shift, direction)
#     elif again == "no":
#         print("Goodbye!")
#         break
#     else:
#         print("You enter a wrong things ....")

#  ---------  more sufficisnt way of using where loop here -----------

again = True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    restart = input("Enter Yes if you want to again otherwise enter No :\n").lower()

    if restart == "no":
        again = False
        print("Goodbye....")
        
