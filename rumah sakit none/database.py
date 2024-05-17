import mysql.connector

class database:

    __conn = mysql.connector.connect(
        host = "your_host",
        user = "your_user",
        password = "your_password",
        database = "your_database"
    )
    
    cursor = __conn.cursor(buffered=True)

    @classmethod
    def select(cls, table, column, val):
        cls.cursor.execute(f"SELECT * FROM `{table}` WHERE `{column}` = '{val}'")
        fetch = cls.cursor.fetchall()
        return fetch

    @classmethod
    def select_all(cls, table):
        cls.cursor.execute(f"SELECT * FROM `{table}`")
        fetch = cls.cursor.fetchall()
        return fetch

    @classmethod
    def insert(cls, table, columns, val):
        string = ', '.join(['%s' for _ in range(len(val))])
        query = f"INSERT INTO `{table}` ({', '.join(columns)}) VALUES ({string})"
        cls.cursor.execute(query, val)
        cls.__conn.commit()

    @classmethod
    def update(cls, table, column1, val1, column2, val2):
        update = f"UPDATE `{table}` SET `{column1}` = '{val1}' WHERE `{column2}` = '{val2}'"
        cls.cursor.execute(update)
        cls.__conn.commit()

    @classmethod
    def delete(cls, table, column, val):
        delete = f"DELETE FROM `{table}` WHERE `{column}` = '{val}'"
        cls.cursor.execute(delete)
        cls.__conn.commit()

    @classmethod
    def delete_all(cls, table):
        delete = f"DELETE FROM `{table}` WHERE 1=1"
        cls.cursor.execute(delete)
        cls.__conn.commit()

