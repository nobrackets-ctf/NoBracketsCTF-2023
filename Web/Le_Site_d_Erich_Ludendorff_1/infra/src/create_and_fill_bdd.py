# Should be a secret, do not show to users !
import sqlite3
import os
from flag import FLAG_3

con = sqlite3.connect("users.db")
cur = con.cursor()
cur.execute("CREATE TABLE users(uid, username, password, grade);")
cur.execute(f"INSERT INTO users VALUES ('{os.urandom(24).hex()}','georg.bruchmuller','{os.urandom(24).hex()}','guest');")
cur.execute(f"INSERT INTO users VALUES ('{os.urandom(24).hex()}','erich.ludendorff','{FLAG_3}','admin');")
cur.execute(f"INSERT INTO users VALUES ('{os.urandom(24).hex()}','oskar.von.hutier ','{os.urandom(24).hex()}','guest');")
cur.execute(f"INSERT INTO users VALUES ('{os.urandom(24).hex()}','alexandre.vassilievitch.samsonov ','{os.urandom(24).hex()}','guest');")
con.commit()
