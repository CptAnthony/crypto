def get_initials(fullname):
    fullname_upper = fullname.upper()
    answer = ("")
    for i in (fullname_upper.split()):
            answer = answer + i[0]
    return answer

def main():
    username = input("What is your full name?")
    get_initials(username)

if __name__ == '__main__':
    main()
