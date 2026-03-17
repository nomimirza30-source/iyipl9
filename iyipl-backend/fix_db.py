import sqlite3

conn = sqlite3.connect('iyipl.db')
cursor = conn.cursor()

cursor.execute("UPDATE users SET role = 'SUPER_ADMIN' WHERE role = 'super_admin' COLLATE NOCASE")
cursor.execute("UPDATE users SET role = 'ADMIN' WHERE role = 'admin' COLLATE NOCASE")
cursor.execute("UPDATE users SET role = 'PARTNER' WHERE role = 'partner' COLLATE NOCASE")
cursor.execute("UPDATE users SET role = 'STAFF' WHERE role = 'staff' COLLATE NOCASE")

conn.commit()
conn.close()
print("Fixed DB enum values")
