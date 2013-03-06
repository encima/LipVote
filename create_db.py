import sqlite3
con = sqlite3.connect('lipvote.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE choons (id INTEGER PRIMARY KEY, choon char(100) NOT NULL, artist char(100) NOT NULL, votes INTEGER NOT NULL)")
# con.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
# con.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
# con.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
# con.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
con.commit()
