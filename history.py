def save_history(text):

    file = open("calculation_history.txt", "a")

    file.write(text + "\n")

    file.close()

def show_history():

    file = open("calculation_history.txt", "r")

    history = file.readlines()

    file.close()

    print("\n---- HISTORY ----")

    for item in history:
        print(item.strip())