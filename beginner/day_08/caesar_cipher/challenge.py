alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 
           'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 
           's', 't', 'u', 'v','w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode'  to decryt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Don't change the code above 

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amunt):

    cipher_text = ""

    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amunt
        new_letter = alphabet[new_position]
        cipher_text += new_position
    print(f"The encoded text is {cipher_text}")

    #TODO-2L Inside the 'encrypt' function, shift each letter of the 'text' forwards in the
    #alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #print output: "The encoded text is mjqgt"

#TODO-3: Call the encrypt function and pass in tge user inputs. You should be able to test the code and encrypt a message.


# Don't change the code above 

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amunt):

    plain_text = ""

    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amunt
        plain_text += alphabet[new_position]
        # cipher_text += new_position
    print(f"The decoded text is {plain_text}")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' *backwards* in the
    #alphabet by the shift amount and print the dencrypted text.
    #e.g.
    #plain_text = "mjqgt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The encoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct
# function based on that 'direction variable. You shoudl be able to test the code to encrypt *AND* decrytpt a message.
if direction == 'encode':
    encrypt(plain_text=text, shift_amunt=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amunt=shift)

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called ceaser().
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == 'decode': 
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
        #TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is coded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = ""... .. 3" 

    print(f"the d{cipher_direction}d text is {end_text}")

#TODO-1: Import and print the logo form art.py when the program starts.
# from art import logo
# print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shif again and call the ceasar() fucntion again?
#Hint: Try creating a new function that calls itself if they type 'yes'.
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type yuour message:\n")
    shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Hint: Think about how you can use the modulus (%).
shift = shift % 26
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
if result == "no":
    should_continue = False
    print("Good Bye")
