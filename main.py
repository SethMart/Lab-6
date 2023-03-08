def decoder(password):
    # First we want to take encoded password and covert it to a list.
    pass_str = str(password)
    pass_list = list((pass_str.strip(" ")))
    res_list = []
    # Use for loop to shift each digit and add to list.
    for password in pass_list:
        shift_down = (int(password) - 3) % 10
        res_list.append(shift_down)
    # Remove list.
    password = ''.join(str(digit) for digit in res_list)

    return password
