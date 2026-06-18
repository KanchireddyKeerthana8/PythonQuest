from game.xp import add_xp
def start_chapter():

    print("\nChapter 1")
    print("The castle gate is locked.")

    print("\nTask:")
    print("Create a variable called key")
    print('Store "golden_key"')

    answer = input("\nType your code: ")

    if answer == 'key = "golden_key"':
        print("Gate Opened!")

        add_xp(100)
        return True
    else:
        print("Try again.")
    return False