import mysql.connector as mysql
cnx = mysql.MySQLConnection(
    host = "db-server-evergreen-jpl.mysql.database.azure.com",
    port = 3306,
    user = "evergreenadmin@db-server-evergreen-jpl",
    password = "qrxGAA19",
    database = "evergreen",
)