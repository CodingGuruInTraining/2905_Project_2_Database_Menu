import dbCreate, dbAdd, dbUpdate, dbDelete, dbShowAll, dbShowOne

def main():
    keep_running = True
    while keep_running:
        showMenu()

def showMenu():
    print("=" * 45)
    print("Enter the number next to the menu item you want:")
    print("1 -- Create Table")
    print("2 -- Add New Entry")
    print("3 -- Update Entry")
    print("4 -- Delete Entry")
    print("5 -- Show Table")
    print("6 -- Show Entry")
    print("Press any other key to exit.")
    print("=" * 45)
main()
