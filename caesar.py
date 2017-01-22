from sys import argv, exit
from helpers import rotate_character

def encrypt(text, rot):
    encrypt_text = ("")
    text_list = list(text)
    for i in (text_list):
        rot_item = rotate_character(i,rot)
        encrypt_text = encrypt_text + rot_item
    return(encrypt_text)

def user_input_is_valid(cl_args):
    if (len(cl_args) == 2):
        if cl_args[1].isdigit() is True:
            return True
        else:
            return False
    else:
        return False

def main():
    if user_input_is_valid(argv) is True:
        message = str(input("Type a message:"))
        rotations = int(argv[1])
        encrypt(message, rotations)
    else:
        print("usage: python3 caesar.py n")
        exit()


if __name__ == '__main__':
    main()
