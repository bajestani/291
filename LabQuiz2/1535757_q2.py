import sqlite3
conn = sqlite3.connect('LabQuiz2_D04_tables')

c = conn.cursor()

def main():

   
    ID = input("Enter a book id: ")
    
    c.execute ("""SELECT * FROM Members WHERE  
                                    SELECT MemID FROM Transactions T, Members M WHERE T.MemID = M.MemID AND 
                                                                                        SELECT BookID FROM Transactions WHERE BookID = ? AND TransactionDate >= strftime("%Y %m %d", 'now' - 1 year)""", (ID))
                                                                                                                                            
