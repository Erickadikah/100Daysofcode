# prime number checker
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number)
#      if number % i == 0:
#         is_prime = False
#     if is_prime:
#         print("it is a prime numbre.")
#     else:
#         print("its not a prime numbre.")


# n = int(input("check this number: "))
# prime_checker(number=n)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type your'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your massage:\n").lower()
shift = int(input("type the shift number:\n"))


# Todo =1 creating a function called 'encrypt' that takes the text and shift as inputs.

def encrypt(plain_text, shift_amount):
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text si {cipher_text}")


encrypt(plain_text=text, shift_amount=shift)
