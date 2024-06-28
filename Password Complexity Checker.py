def Password_Complexity_Checker(pswd):
    length= len(pswd)>12
    uppercase = any(char.isupper() for char in pswd)
    lowercase = any(char.islower() for char in pswd)
    number = any(char.isdigit() for char in pswd)
    special = any(not char.isalnum() for char in pswd)
    score=sum([length,uppercase,lowercase,number,special])

    if score==5:
        strength= "Very Strong"
    elif score==4:
        strength= "Strong"
    elif score==3:
        strength= "Moderate"
    elif score==2:
        strength= "week"
    else:
        strength= "Very Week"

    feedback = []
    if not length:
        feedback.append("Password should be more than 12 characters long.")
    if not uppercase:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number:
        feedback.append("Password should contain at least one number.")
    if not special:
        feedback.append("Password should contain at least one special character.")
    return strength, feedback

print('''
 **********************************
 *                                *
 *                                *
 *       Password Complexity      *
 *           Checker              *
 *                                *
 *                                *
 **********************************



    Key Points for Strong Password
        1. More than 12 Characters 
        2. Must contain a Capital Letter
        3. Must contain a Small Letter
        4. Must contain a Digit
        5. Must contain a Special character
''')

pswd = input("Enter a password: ")
strength,feedback=Password_Complexity_Checker(pswd)

print(f"Password strength:  {strength}")
if feedback:
    print("Feedback: ")
    for i in feedback:
        print("- ", i)
