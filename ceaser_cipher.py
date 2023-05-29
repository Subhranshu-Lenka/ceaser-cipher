alphabets = """A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z"""
alphabets = alphabets.split(" ")
ignorables = [" ", ".", "!", ";", "@", "#",
              "$", "%", "^", "&", "*", "_", ":", "?"]


print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           []             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")


def ceaser_cipher(msg, shift, direction):
    end_txt = ""
    if direction == "decode":
        shift *= -1
    for i in msg:
        if i in ignorables:
            end_txt += i
        else:
            ind = alphabets.index(i)
            if (ind <= 25) and (ind+shift > 25):
                ind = (ind % 25)-1
            elif ind > 25 and (ind+shift > 51):
                ind = (ind % 51)+25
            end_txt += alphabets[ind+shift]
    print(f"The {direction}d text is {end_txt}.")


yes = True
while(yes):
    direction = input(
        "Type 'encode' to Encrypt the message \nType 'decode' to decrypt the messasge\n").lower()

    if direction != "encode" and direction != "decode":
        print("You wrote wrong spelling!!!")
        continue
    else:
        msg = input("Enter your message here \t")
        shift = int(input("Enter the number of shifts required\t"))
        ceaser_cipher(msg=msg, shift=shift, direction=direction)

        restart = input(
            'Type "yes" if you want to go again. Otherwise type "no"\t').lower()
        if(restart != "yes"):
            print("GoodBye !")
            break
