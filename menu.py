import dbCreate, dbAdd, dbUpdate, dbDelete, dbShowAll, dbShowOne


def main():
    keep_running = True
    while keep_running:
        showMenu()
        userChoice = input()
        runMenu(userChoice)
        more = input("Would you like to do more? (Y/N)")
        if more.lower() == "n":
            print("Yeah, neither did I.")
            keep_running = False


def showMenu():
    print('=' * 45)
    print('Enter the number next to the menu item you want:')
    print('1 -- Create Table')
    print('2 -- Add New Entry')
    print('3 -- Update Entry')
    print('4 -- Delete Entry')
    print('5 -- Show Table')
    print('6 -- Show Entry')
    print('Enter any other key to exit.')
    print('=' * 45)


def runMenu(num):
    if num == '1':
        dbCreate
    elif num == '2':
        dbAdd
    elif num == '3':
        dbUpdate
    elif num == '4':
        dbDelete
    elif num == '5':
        dbShowAll
    elif num == '6':
        dbShowOne
    else:
        print("Shutting down...goodbye")
        exit()
main()
