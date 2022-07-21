import sqlite3
from pprint import pprint


class DB:
    conn = sqlite3.connect('source/buildings.db')

    def __init__(self):
        self.cur = self.conn.cursor()

    def add_table(self, name: str, filds_and_types: dict):
        """
        This method creates new table if not exists
        :param name: table name
        :param filds_and_types: dictionary of fields and them types. like {"number": "INT", "name": "TEXT"}
        :return: None
        """
        command = f"CREATE TABLE IF NOT EXISTS {name}(id INT PRIMARY KEY"
        for field in filds_and_types:
            command += f", {field} {filds_and_types[field]}"
        command += ");"
        self.cur.execute(command)
        self.conn.commit()

    def delete_table(self, name: str):
        """
        This method removes selected tables from DB
        :param name: table name
        :return: None
        """
        self.cur.execute(f"DROP TABLE IF EXISTS {name}")
        self.conn.commit()

    def insert_row(self, table: str, fields: tuple, row: tuple):  # row: list?
        command = f"INSERT INTO {table}{str(fields)} VALUES{str(row)};"
        print(command)
        self.cur.execute(command)
        self.conn.commit()

    def simple_select(self, name: str):
        self.cur.execute(f"SELECT * FROM {name};")
        return self.cur.fetchone()

    def all_select(self, name: str) -> list:
        self.cur.execute(f"SELECT * FROM {name};")
        return self.cur.fetchall()

    def load_data_from_file(self, file: str, table: str):
        fields = tuple(self.get_table_fields(table))
        values = '(' + ('?, ' * (len(fields) - 1)) + '?)'
        with open(file, 'r') as f:
            file = f.read().split("\n")
            to_db = [row.split(",") for row in file]
            res = [tuple(x) for x in to_db]
            command = f"INSERT INTO {table} {fields} VALUES {values};"
            res.pop(0)
            res.pop()
            for block in res:
                self.cur.execute(command, block)
            self.conn.commit()

    def get_table_fields(self, name) -> list:
        cursor = self.conn.execute(f"select * from {name}")
        return list(map(lambda x: x[0], cursor.description))

    def exec(self, query: str) -> list:
        self.cur.execute(query)
        return self.cur.fetchall()


if __name__ == "__main__":
    BUILDINGS = "buildings"

    fields = {"name": "TEXT", "price": "INT", "color": "TEXT", "preference": "TEXT"}
    base = DB()
    # delete table
    # base.delete_table(BUILDINGS)
    # add table
    # base.add_table(BUILDINGS, fields)
    # fill table
    # base.load_data_from_file("source/buildings.csv", BUILDINGS)
    # get all
    # pprint(base.all_select(BUILDINGS))
    # get special
    result = base.exec(f"""SELECT name from {BUILDINGS} WHERE color = "purple";""")
    print(result)

    for name in result:
        print(f'''
    def {name[0].lower().replace(" ", "_")}(self):
        pass''')
