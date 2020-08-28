import Registration_and_Login

def Menu():

    print('------------(RPG)------------')
    print('\n 1) Login')
    print(' 2) Registration')

    try:
        selection = int(input('\n Make your Selection: '))
    except:
        print('Choose the right one please =)')

    if selection == 1:
        Registration_and_Login.Login()
    elif selection == 2:
        Registration_and_Login.Registration()

Menu()
