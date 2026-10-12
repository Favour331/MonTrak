import mysql.connector

def createConn():
    conn = mysql.connector.connect(host='localhost', user='root', passwd="")
    try:
        cursor = conn.cursor()
        try:
            cursor.execute("Create Database if not exists MonTrak")
            cursor.execute("use MonTrak")
        finally:
            cursor.close()
        return conn
    except Exception:
        # Do not leave a failed connection open; let the caller handle the error.
        conn.close()
        raise
         
def createTables():
    getconn = createConn()
    cur = getconn.cursor()
    try:
        cur.execute("Create table if not exists expense (id int Auto_Increment Primary Key,Money_made int(11),Money_spent int(11),date TIMESTAMP DEFAULT CURRENT_TIMESTAMP )")
        getconn.commit()
    finally:
        cur.close()
        getconn.close()
        
def insertTable(money_made,money_spent):
    getconn = createConn()
    cur = getconn.cursor()
    try:
        # Bind values separately instead of inserting user input into SQL text.
        cur.execute(
            "INSERT INTO expense (Money_made, Money_spent) VALUES (%s, %s)",
            (money_made, money_spent),
        )
        getconn.commit()
    finally:
        cur.close()
        getconn.close()
        
def retriveMonth(monNum):
    getconn = createConn()
    cur = getconn.cursor(dictionary=True)
    try:
        # Match the entered month in the current year; parameters safely bind the month.
        cur.execute(
            "SELECT * FROM expense "
            "WHERE MONTH(`date`) = %s AND YEAR(`date`) = YEAR(CURRENT_DATE())",
            (monNum,),
        )
        # fetchall() returns all matching records as a list of dictionaries.
        return cur.fetchall()
    finally:
        cur.close()
        getconn.close()

def retriveDate(date):
    getconn = createConn()
    cur = getconn.cursor(dictionary=True)
    try:
        # Compare only the calendar date, not the time portion of the timestamp.
        cur.execute("SELECT * FROM expense WHERE DATE(`date`) = %s", (date,))
        return cur.fetchall()
    finally:
        cur.close()
        getconn.close()