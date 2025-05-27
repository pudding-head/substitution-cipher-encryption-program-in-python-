# substitution cipher encryption program in python 
import random 
import string 
chars= " " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key = chars.copy() 
random.shuffle(key)

# encryption
plain_text=input("enter a msg to encript: ")
chiper_text=""

for letter in plain_text:
    index=chars.index(letter)
    chiper_text +=key[index]

print(f"original msg: {plain_text}")
print(f"encrypted msg: {chiper_text}")


# decryption
chiper_text=input("enter a msg to encript: ")
plain_text=""

for letter in chiper_text:
    index=key.index(letter)
    plain_text +=chars[index]

print(f"encrypted msg: {chiper_text}")
print(f"original msg: {plain_text}")
