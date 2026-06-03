import sqlite3
import json

def export_history():

    connection = sqlite3.connect("calculator.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM history")

    data = cursor.fetchall()

    with open("history.json", "w") as file:

        json.dump(data, file, indent=4)

    connection.close()