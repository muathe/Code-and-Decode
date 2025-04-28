alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def secret(words, shift_key, options):
    
    if option == "decode":
        shift_key *= -1
    
    
    display = ""
    for char in words:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_key
            display += alphabet[new_position]
    
        else:
            display += char
        
    print(f"Your {option}d word is {display}")
    
    
    
    
continuation = True

while continuation == True:


    option = input("Would you like to encode or decode: ").lower()
    word = input("Please enter a word you would like: ").lower()
    shift = int(input("Please enter the amount of shifts: "))

    shift = shift % 26

    secret(words = word, shift_key = shift, options = option)

    result = input("Do you want to continue? Yes or NO\n").lower()
    if result == "no":
        continuation = False
        print("Good Bye")


#cell30
