import sqlite3

conn = sqlite3.connect('buildings.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS buildings(
    buildingid INT PRIMARY KEY,                          
    name TEXT,
    price INT,
    color TEXT,
    properties TEXT); 
    """)
conn.commit()
# cur.execute("""INSERT INTO buildings(
#     buildingid, name, price, color, properties)
#     VALUES('2', 'Port', '1', 'Green', '');""")
# conn.commit()
cur.execute("SELECT * FROM buildings;")
one_result = cur.fetchone()
print(one_result)