logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def ceaser (original_text, shift_amount, encode_or_decode):
    coded_text = ""
    if encode_or_decode == "decode".lower():
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            coded_text += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
        else:
            coded_text += letter

    print(f"Here is the {encode_or_decode}d result: {coded_text}")

continue_program = True
while continue_program:

    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    while direction not in ["encode", "decode"]:
        print("Invalid decision, try again!")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    rerun = input("Would you like to go again? Yes or No:\n").lower()
    while rerun not in ["yes", "no"]:
        print("Invalid input, please type 'yes' or 'no'.")
        answer = input("Would you like to go again? Yes or No:\n").lower()

    if rerun == "no".lower():
        print("Thank you!")
        continue_program = False
