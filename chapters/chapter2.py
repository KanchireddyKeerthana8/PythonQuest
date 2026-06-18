from game.xp import add_xp

def start_chapter():

    print("\nChapter 2")
    print("The king needs a score value.")

    print("\nTask:")
    print("Create a variable called score")
    print("Store number 100")

    answer = input("\nType your code: ")

    if answer == "score = 100":

        print("Correct!")

        add_xp(100)

        return True

    else:
        print("Try Again.")
        return False