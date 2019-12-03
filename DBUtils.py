import mysql.connector


class DBConnector():
    """
    A class representing a ...
    """

    def __init__(self, host, user, passwd, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )
        self.mycursor = self.mydb.cursor()

    def insert(self, table, columns, records):
        values_container = ','.join(["%s" for i in range(len(records[0]))])
        sql = "INSERT IGNORE INTO " + table + "(" + columns + ") VALUES (" + values_container + ")"
        self.mycursor.executemany(sql, records)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record/s inserted in table", table)

    def select(self, columns, table, where):
        sql = "SELECT " + columns + "FROM" + table + "WHERE" + where
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()


class DBCreator():

    @staticmethod
    def start_db(host, user, passwd, db, tables_to_be_created):
        DBCreator.create_db(host, user, passwd, db)
        DBCreator.create_tables(host, user, passwd, db, tables_to_be_created)

    @staticmethod
    def create_db(host, user, passwd, db):
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )

        mycursor = mydb.cursor()

        mycursor.execute("SHOW DATABASES")

        db_exists = False

        for x in mycursor:
            if x[0].lower() == db.lower():
                db_exists = True

        if not db_exists:
            mycursor.execute("CREATE DATABASE " + db)

    @staticmethod
    def create_tables(host, user, passwd, db, tables_to_be_created):
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=db
        )

        mycursor = mydb.cursor()

        mycursor.execute("show tables")

        myresult = mycursor.fetchall()

        existing_tables = [elem[0] for elem in myresult]

        for table_name in tables_to_be_created:
            if table_name not in existing_tables:
                mycursor.execute(tables_to_be_created[table_name])
