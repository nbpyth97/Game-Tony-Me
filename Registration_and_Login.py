

def Registration():
    global nickname, password
    lst = []
    nickname = input('\n Choose your Nickname: ')
    password = input(' Choose your Password: ')
    password_repeat = input('Repeat your Password: ')

    while password != password_repeat:
        print('\n Please put the right password =)')
        password_repeat = input('\n Repeat your Password: ')

    lst.append(nickname)
    lst.append(password_repeat)

    with open('E:\\Game\\Registration&Login.txt', 'a') as file:
        file.write(str(lst))

    import Menu
    Menu()

def Login():

    nickname_login = input('Nickname: ')
    password_login = input('Password: ')
    lst_login = []

    with open('E:\\Game\\Registration&Login.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            lst_login.append(line)

    print(lst_login)





