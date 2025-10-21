print("Bitte tragen deinen Benutzeenamen ein: ")
user_name = input() # 

print("Bitte gebe jetzt dein Password: ")
password = input() #

print("Regestrierung erfolgreich bei Subway :-)")
print("--------------------------------------")

#login

print("Gebe jetzt dein Benutzernamen ein: ")
eingabe_user_name = input()

#if Bedinung wenn das ist dann führe das hier aus
if eingabe_user_name == user_name:
    print("Alles Klar Benutzernamen war korrekt und gabe Password ein")
    eingabe_password = input()
    if password == eingabe_password:
        print("Erfolgreich eingeloggt, viel Spass nit dden Coupons")
    else:
        print("Fslsche Password")

else:
    print("Falscher Username")