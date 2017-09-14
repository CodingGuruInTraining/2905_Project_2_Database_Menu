import sqlite3

# Defines main.
def main(go = False):
    # Only runs if True boolean is passed. This prevents
    # import from running at start.
    if go == True:
        addEntry()


def addEntry():
    # Runs function to gather user inputs.
    answers = getInputs()
    # Variables are defined.
    filename = "storeDB.sqlite"
    table1 = "products"
    # Connects to database.
    conn = sqlite3.connect(filename)
    connCursor = conn.cursor()

    # Exception handler.
    try:
        # Combines values into statement string.
        connCursor.execute("INSERT OR IGNORE INTO {tn} VALUES (NULL, {f1}, {f2}, {f3}, {f4}, {f5}, {f6})".
                   format(tn=table1, f1="\'" + answers[0] + "\'", f2=float(answers[1]), f3=int(answers[2]),
                  f4=int(answers[3]), f5="\'" + answers[4] + "\'", f6="\'" + answers[5] + "\'"))
    except sqlite3.IntegrityError:
        print("Error with primary key")
    except sqlite3.Error:
        print("Error; bad values or no table")

    # Executes statement and closes connection.
    conn.commit()
    conn.close()

# Gets inputs from users and returns all in a list.
def getInputs():
    prodName = input("Product Name: ")
    price = input("Price: ")
    quantity = input("Quantity: ")
    numSold = input("# Sold: ")
    description = input("Description: ")
    color = input("Color: ")
    answers = [prodName, price, quantity, numSold, description, color]
    return answers

