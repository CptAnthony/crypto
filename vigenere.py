

from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    #code assembler
    encrypt_text = ("")
    #key extender
    extended_key = (key * ((len(text) // len(key)+1)))
    resized_key = extended_key[0:((len(text)))]
    #list of string and text characters
    text_list = list(text)
    key_list = list(resized_key)
    #counter for alphabet_position
    key_counter = 0

    for i in (text_list):
        if str(i).isalpha() is True:
            rot_number = alphabet_position(key_list[key_counter])
            rot_item = rotate_character(i,rot_number)
            encrypt_text = encrypt_text + rot_item
            key_counter = key_counter + 1
        else:
            encrypt_text = encrypt_text + str(i)
    
    return(encrypt_text)

def main():
    message = str(input("Type a message:"))
    cipher = str(input("Encryption key:"))
    encrypt(message, cipher)

if __name__ == '__main__':
    main()
