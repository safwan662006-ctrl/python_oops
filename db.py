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
        Phone int,
    );
""")
cursor.execute("""
    INSERT INTO students VALUES 101,'JOHN','john123@gmail.com',9856341254
            """)


#save changes
conn.commit()

#close connection
conn.close()

print("Database created successfully")