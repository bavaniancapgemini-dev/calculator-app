def save_history(text):

    file = open("calculation_history.txt", "a")

    file.write(text + "\n")

    file.close()