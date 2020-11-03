import sqlite3
conn = sqlite3.connect('LabQuiz2_D04_tables')

c = conn.cursor()

def main():

   
    ID = input("Enter a member id: ")

    c.execute("SELECT MemName, BookTitle, TransactionType, TransactionDate FROM Members M, Books B, Transactions T WHERE T.MemID = ? AND T.BookID = B.BookID AND M.MemID = ?", (ID,))

    rows= c.fetchall()
    
    print(rows)
    