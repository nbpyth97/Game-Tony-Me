

def Registration():
    global nickname, password, lst
    lst = []
    nickname = input('\n Choose your Nickname: ')
    password = input(' Choose your Password: ')
    password_repeat = input(' Repeat your Password: ')

    while password != password_repeat:
        print('\n Please put the right password =) ')
        password_repeat = input('\n Repeat your Password: ')

    lst.append(nickname)
    lst.append(password_repeat)

    with open('E:\\Game\\Registration&Login.txt', 'a') as file:
        file.write(nickname + '#')
        file.write(password_repeat)

    import Menu
    Menu()

def Login():

    nickname_login = input('Nickname: ')
    password_login = input('Password: ')

    with open('E:\\Game\\Registration&Login.txt', 'r') as file:
        lines = file.read().split('#')

    print(lines[0])
    while nickname_login != lines[0] or password_login != lines[1]:
        print('Something wet wrong :/ try again')
        nickname_login = input('Nickname: ')
        password_login = input('Password: ')


    if nickname_login == lines[0] and password_login == lines[1]:
        print('''
        ----(Sub-Menu)----
           1) Continue the Game
           2) Restart the Game
           3) Start the Game
        ''')




