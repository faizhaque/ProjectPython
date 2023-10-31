def encode(password):
    password_encode = ''
    for char in password:
        digit = (int(char) + 3) % 10
        str_digit = str(digit)
        password_encode += str_digit
    return password_encode



def main():
    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")
        if option == "3":
            break
        password = input("Please enter a password to encode: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!")


if __name__ == '__main__':
    main()

