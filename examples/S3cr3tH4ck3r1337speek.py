"""
send and receive secret messages
with a friend.

The following code will be to implement a Caesar cipher. A very standard cipher.

Created by Chace
"""

# We store the alphabet into a string called alphabet which we can index to get the letter.
alphabet = 'abcdefghijklmnopqrstuvwxyz'

ckey = input("Enter key (numbers only)")    # This will be the key that we use in our Caeser Cipher.
key = int(ckey) #convert to integer

# We take user input to encrypt whatever character they input
character = input("Please enter a phrase to encrypt:\n")
charlength = len(character)
x = 0
encrypted_character = ""

while x != charlength:

    # The find function is acting on alphabet here to return the index number of the character letter that the user inputted
    position = alphabet.find(character[x])


    # Using the % character here is modding the value (position + key) with the length of alphabet, which is 26 in this case
    # By modding it we get the remainder of (position + key) which will help on values that would go over 26.
    new_position = (position + key) % len(alphabet)


    encrypted_character += alphabet[new_position]

    x+=1
print(encrypted_character)
decode = input("would you like to decode?")
if decode == "yes":

    x = 0
    character = input("Please enter phrase to decode")
    charlengthd = len(character)
    encrypted_character = ""
    while x != charlengthd:
        # The find function is acting on alphabet here to return the index number of the character letter that the user inputted
        position = alphabet.find(character[x])


        # Using the % character here is modding the value (position + key) with the length of alphabet, which is 26 in this case
        # By modding it we get the remainder of (position + key) which will help on values that would go over 26.
        new_position = (position - key) % len(alphabet)


        encrypted_character += alphabet[new_position]

        x += 1

print (encrypted_character)
"""
This whole program will take a user inputted phrase and rotate it in the alphabet by a custum length
"""
