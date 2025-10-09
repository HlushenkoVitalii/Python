# implementation Cesar Encryption


ALPHABET = [
    ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

ALPHABET_len = len(ALPHABET)

# this fuction ask user for key encryption and return int
def get_Key()->int:
    # because allways what user typed in cli will be saved as string!
    key = input("please enter encryption Key:")
    # we mast change the type to int
    key = int(key)
    return key


# this function do encyption
def encrypt()->str:
    result = ""
    # klar text in what user typed for exmple jojo
    klar_text = input("\nplease enter Text to be encrypted:")
    key = get_Key()
    for character in klar_text:
        # we find position of each charecter in our ALPHABET ARRAY
        # 
        alphabet_index = ALPHABET.index(character)
        new_character_index = alphabet_index+key

        encrypted_Character_index = new_character_index % len(ALPHABET)
        result += ALPHABET[encrypted_Character_index]
    return result

def decode()->str:
    result = ""
    klar_text = input("\nplease enter Text to be DECRYPTED:")
    key = get_Key()
    for character in klar_text:
        alphabet_index = ALPHABET.index(character)
        new_character_index = alphabet_index-key

        encrypted_Character_index = new_character_index % len(ALPHABET)
        result += ALPHABET[encrypted_Character_index]
    return result



def main():
    result = ""
    print("hello, I am cesar enc and dec app!")
    userChoice = input("If you want decrypt press d or encrypt press e: ")
    
    if(userChoice == "e"):
        result = encrypt()
    elif(userChoice == "d"):
        result = decode()
    else:
        result = "you must only press e or d!"

    print(result)

if __name__ == "__main__":
    main()

