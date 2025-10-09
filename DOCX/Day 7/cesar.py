# implementation Cesar Encryption

#this function do encyption
def encrypt()->str:
    klar_text = input("\nplease enter Text to be encrypted:")
    key = input("please enter encryption Key:")
    return "it is encrypted " + klar_text + " and " + str(key)

def decode()->str:
    cypher_text = input("\nplease enter Text to be DECRYPTED:")
    key = input("please enter DECRYPTED KEY:")
    return "it is DECRYPTED from " + cypher_text + " and KEY " + key



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

