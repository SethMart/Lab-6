def encoder(password):
    # First we want to take encoded password and covert it to a list.
    pass_str = str(password)
    pass_list = list((pass_str.strip(" ")))
    res_list = []
    # Use for loop to shift each digit and add to list.
    for password in pass_list:
        shift_up = (int(password) + 3) % 10
        res_list.append(shift_up)
    # Remove list.
    password = ''.join(str(digit) for digit in res_list)

    return password


def decoder(password):  # decoder function
    new_integer = ''  # open "list" but for strings
    for integer in password:  # for loop to go through the password
        single_int = ((int(integer)) - 3) % 10
        # adds three after converting the integer into an integer than uses modulo to isolate the digit
        single_int = str(single_int)  # converts it back into a string
        new_integer += single_int  # adds the converted string into the ''
    return new_integer  # return statement


def main():
    # Use while loop for Menu.
    while True:
        print()
        print('Welcome to Password Coding!')
        print('------------------')
        print()
        print('1. Encode Password')
        print('2. Decode Password')
        print('3. Exit')
        print()
        selection = int(input('Select an option: '))
        # Make specified range for menu selection.
        if selection in range(1, 3):
            password = input('Enter the password: ')
            if selection == 1:
                print(f'The encoded password is: {encoder(password)}!')

            elif selection == 2:
                print(f'The decoded password is: {decoder(password)}!')

        else:
            exit()


main()