import sqlite3
conn = sqlite3.connect('LabQuiz2_D04_tables')

c = conn.cursor()

def main():

   

    c.execute(
        'SELECT * FROM Transactions WHERE MemID = ?'
    )