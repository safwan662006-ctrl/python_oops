import sqlite3
 
# Create/connect to database
conn = sqlite3.connect("tution.db")
 
# Create a cursor
cursor = conn.cursor()
 
# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
""")



cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id int PRIMARY KEY,
        Name TEXT,
        Email TEXT,
        Phone int
    );
""")




#save changes
conn.commit()

#close connection
conn.close()

print("Database created successfully")