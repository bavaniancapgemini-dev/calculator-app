import sqlite3


connection = sqlite3.connect("history.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    calculation TEXT
)
""")

connection.commit()

connection.close()

def save_to_database(text):

    connection = sqlite3.connect("history.db")

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO history VALUES (?)",
        (text,)
    )

    connection.commit()

    connection.close()

def view_database_history():

    import sqlite3

    connection = sqlite3.connect("calculator.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM history")

    data = cursor.fetchall()

    connection.close()

    return data