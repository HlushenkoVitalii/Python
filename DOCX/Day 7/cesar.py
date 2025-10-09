# implementation Cesar Encryption

#this function do encyption
def encrypt(klar_text:str, key:int)->str:
    return "it is encrypted " + klar_text + " and " + str(key)

def decode(encrypted: str, key:int )->str:
    return "it is decoded text"





def main():
    result = ""
    print("hello, I am cesar enc and dec app!")
    userChoice = input("If you want decrypt press d or encrypt press e: ")
    
    if(userChoice == "e"):
        result = encrypt("jojo", 5)
    elif(userChoice == "d"):
        result = decode("something", 4)
    else:
        result = ""

    print(result)

if __name__ == "__main__":
    main()

