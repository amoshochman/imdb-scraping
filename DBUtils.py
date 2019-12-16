import mysql.connector


class DBConnector():
    """
    A class to run scripts on a specific DB.
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
        """
        Inserts records "records" into columns "columns" from table "table".
        :param table: the table to insert to.
        :param columns: the columns to insert to.
        :param records: the values to use.
        :return: the numbers of records actually inserted
        (pay attention: it can differ from len("records"), as part of them could already exist).
        """
        values_container = ','.join(["%s" for i in range(len(records[0]))])
        sql = "INSERT IGNORE INTO " + table + "(" + columns + ") VALUES (" + values_container + ")"
        self.mycursor.executemany(sql, records)
        self.mydb.commit()
        return self.mycursor.rowcount

    def select(self, columns, table, where=None):
        """
        Select from table "table" the records that fulfill the conditions in "where" parameter, if present,
        and retrieves the values in "columns" parameter.
        :param columns: the columns to retrieve data from.
        :param table: the table to use.
        :param where: if present, the conditions that need to be fulfilled by the query.
        """
        sql = "SELECT " + columns + " FROM " + table
        if where:
            sql += " where " + where
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()


class DBCreator():

    @staticmethod
    def start_db(host, user, passwd, db, tables_to_be_created):
        """
        Creates the specified DB if it doesn't exist and creates the tables from the specified ones that
        don't exist.
        :param host: the host.
        :param user: the user.
        :param passwd: the password.
        :param db: the database.
        :param tables_to_be_created: the tables that need to be created.
        """
        DBCreator.__create_db(host, user, passwd, db)
        DBCreator.__create_tables(host, user, passwd, db, tables_to_be_created)

    @staticmethod
    def __create_db(host, user, passwd, db):
        """
        Creates the specified DB if it doesn't exist.
        :param host: the host.
        :param user: the user.
        :param passwd: the password.
        :param db: the database.
        """
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
                break

        if not db_exists:
            mycursor.execute("CREATE DATABASE " + db)

    @staticmethod
    def __create_tables(host, user, passwd, db, tables_to_be_created):
        """
        From the specified tables creates the ones that don't exist in the DB.
        :param host: the host.
        :param user: the user.
        :param passwd: the password.
        :param db: the database.
        :param tables_to_be_created: the tables that need to be created.
        """
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
