"""
This is the second example. This will be a how to make your own encryption program, to send and receive secret messages
with a friend.

The following code will be to implement a Caesar cipher. A very standard cipher.

Created by alex
"""

# We store the alphabet into a string called alphabet which we can index to get the letter. Shown below in the print
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[0])  # this prints a, remember python starts at 0.
print(len(alphabet))

key = 3             # This will be the key that we use in our Caeser Cipher.

# We take user input to encrypt whatever character they
character = input("Please enter a character to encrypt:\n")

# The find function is acting on alphabet here to return the index number of the character letter that the user inputted
position = alphabet.find(character)
print("The position of %s is " % position)  # You can print string variables inside of a string with the %s

# Using the % character here is modding the value (position + key) with the length of alphabet, which is 26 in this case
# By modding it we get the remainder of (position + key) which will help on values that would go over 26.
new_position = (position + key) % len(alphabet)
print(new_position)

encrypted_character = alphabet[new_position]
print("The encrypted character is: ", encrypted_character)

"""
This whole program will take a user inputted character and rotate it in the alphabet by 3. But what about whole words?
Or decrypting the message? For the second challenge, make a program based on the Caeser cipher and that will encrpyt the
whole word and add decryption abilities.
"""
