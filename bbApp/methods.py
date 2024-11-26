#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.
#Streamlit. “Session State - Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state. Accessed 15 Oct. 2024.
#“How do you solve the error of mysql.connector.errors.ProgrammingError: 1203 (42000): User sql12740146 already has more than 'max_user_connections' active connections” prompt. ChatGPT, GPT-3.5 version, OpenAI, 30 Oct. 2024., chat.openai.com.
#TheCodex. “Python and MySQL - Selecting and Getting Data.” YouTube, 8 July 2018, www.youtube.com/watch?v=jA1GO6g_Rw0&list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G&index=4. Accessed 25 Oct. 2024.
#Kelise. “How Can I Limit INT in MySQL?” Stack Overflow, 3 May 2021, stackoverflow.com/questions/67370961/how-can-i-limit-int-in-mysql. Accessed 20 Oct. 2024.
#UDACITY. “Create a Timer in Python: Step-By-Step Guide.” Udacity, 23 Sept. 2021, www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html. Accessed 20 Oct. 2024.

import time
import random
import mysql.connector
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

'''
connect to a remote mysql database

return: database that stores all game information
'''
def dbConnection():
    return mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12740146",
        password="q3knMTiDxF",
        auth_plugin='mysql_native_password',
        database="sql12740146"
    )

'''
create the initial tables that are needed for the game in the database
'''
def dbSetup():
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS sql12740146")
        mycursor.execute("CREATE TABLE IF NOT EXISTS login (accountName VARCHAR(20), password VARCHAR(20))")
        mycursor.execute("CREATE TABLE IF NOT EXISTS track (pin VARCHAR(7), playerNum TINYINT NOT NULL)")
        mycursor.execute("SHOW TABLES")
        for table in mycursor:
            print(table)
    finally:
        mycursor.close()
        mydb.close()

dbSetup()

'''
click a button and go to the next page

buttonName (str): button that is being clicked to switch page
nextName (str): name of page that is being switched to
'''
def nextPage(buttonName, nextName):
    if buttonName:
        switch_page(nextName)

'''
display error message when a button is clicked and some condition are not met

buttonName (str): button that is being clicked to switch page
message (str): error message displayed
'''
def errorMessage(buttonName, message):
    if buttonName:
        st.text(message)

'''
login function of the game, user can use existing account to enter the game

name (str): account name entered by user
password (str): password entered by user
gotoNext (str): the button that is used to go to next page when login information is verified

return (str): account name of current user
'''
def log(name, passwordIn, gotoNext):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT accountName, password FROM login")
        fetched = mycursor.fetchall()
        loginCheck = False

        for accountName, password in fetched:
            if name == accountName and passwordIn == password:
                loginCheck = True
                nextPage(gotoNext, "UI3")
                if 'accountName' not in st.session_state:
                    st.session_state.accountName = name
                st.session_state.accountName = name
                break

        if not loginCheck:
            message = "wrong account name or password, try again"
            errorMessage(gotoNext, message)

    finally:
        mycursor.close()
        mydb.close()

    return name

'''
sign up function of the game, user can use create new account

name (str): account name entered by user
password (str): password entered by user
gotoNext (str): the button that is used to go to next page when sign up information is checked and saved

return name (str): account name of current user
'''
def sign(name, password, gotoNext):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        sqlFormula = "INSERT INTO login (accountName, password) VALUES (%s, %s)"
        mycursor.execute(sqlFormula, (name, password))
        mydb.commit()
    finally:
        mycursor.close()
        mydb.close()

    if 'accountName' not in st.session_state:
        st.session_state.accountName = name
    st.session_state.accountName = name

    nextPage(gotoNext, "UI3")
    return name

'''
cheking if the game pin user has entered is valid

currentPin (str): the game pin user has entered

return check (bool): if game pin entered matches one in database
'''
def checkPin(currentPin):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    check = False
    pin=[]
    try:
        mycursor.execute("SELECT pin FROM track")
        fetched = mycursor.fetchall()
    finally:
        mycursor.close()
        mydb.close()

    for pinTup in fetched:
        pin.append(pinTup[0])

    for p in pin:
        if currentPin == p:
            check = True
            if 'currentPin' not in st.session_state:
                st.session_state['currentPin'] = currentPin
            st.session_state.currentPin = currentPin
            return check
    return check

'''
generating a game pin for new game, creating a table for the new game in databse
'''
def pinGenerator():
    gamePin = str(random.randint(100, 999)) + '-' + str(random.randint(100, 999))
    if 'currentPin' not in st.session_state:
        st.session_state['currentPin'] = gamePin
    st.session_state.currentPin = gamePin

    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        sqlFormula = "INSERT INTO track (pin) VALUES (%s)"
        mycursor.execute(sqlFormula, (gamePin,))
        mydb.commit()
        mycursor.execute(f"CREATE TABLE IF NOT EXISTS `{gamePin}` (accountName VARCHAR (20), role VARCHAR(1), name VARCHAR(20), treasury INT, firstLog BOOL, allSet BOOL, race VARCHAR(30), p1 VARCHAR(20), p2 VARCHAR(20), p3 VARCHAR(20), p4 VARCHAR(20), p5 VARCHAR(20), p6 VARCHAR(20), p7 VARCHAR(20), p8 VARCHAR(20), p9 VARCHAR(20), p10 VARCHAR(20), p11 VARCHAR(20), p12 VARCHAR(20), p13 VARCHAR(20), p14 VARCHAR(20), p15 VARCHAR(20), p16 VARCHAR(20), fan INT, weather VARCHAR(20), TD INT, CAS INT)")
    finally:
        mycursor.close()
        mydb.close()

'''
create pin when user click a button, using the pinGenerator and switch_page function

buttonName (str): button that is being clicked to switch page
nextName (str): name of page that is being switched to
'''
def createPin(buttonName, nextName):
    if buttonName:
        pinGenerator()
        switch_page(nextName)

'''
checking if the user is admin or player according to information stored in database

roles (array): array stores A or P values indicating admin or player

return passCheck (bool): if there is more than one A, returns false, else returns true
'''
def UIadmin2PassCheck(roles):
    passCheck = False
    flag = 0
    for i in range(len(roles)):
        if roles[i] == "A":
            flag += 1
    if flag == 1:
        passCheck = True
    return passCheck

'''
add item to table in tatabase 

table (str): name of the table in database
columns (array): names of the columns the items are being added to
items (array): values that are being added to columns
'''
def addToDb(table, columns, items):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        columns = ', '.join([f"`{col}`" for col in columns])
        placeholders = ', '.join(['%s'] * len(items))
        sqlFormula = f"INSERT INTO `{table}` ({columns}) VALUES ({placeholders})"
        mycursor.execute(sqlFormula, tuple(items))
        mydb.commit()
    finally:
        mycursor.close()
        mydb.close()

'''
upadate item in table in database, using value in another item as the condition

table (str): name of the table being updated
column (str): name of the column being updated
new: new value to replace the old value
condition (str): name of the column that serves as the condition of checking which row to update
conditionValue: value in the condition column to locate specific row
'''
def updateDb(table, column, new, condition, conditionValue):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        sqlFormula = f"UPDATE `{table}` SET `{column}` = %s WHERE `{condition}` = %s"
        mycursor.execute(sqlFormula, (new, conditionValue))
        mydb.commit()
    finally:
        mycursor.close()
        mydb.close()

'''
fetch data from table in databse

table (str): name of the table 
'''
def getFromDb(table, refColumn, refValue, targetColumn):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        sqlFormula = f"SELECT `{targetColumn}` FROM `{table}` WHERE `{refColumn}` = %s"
        mycursor.execute(sqlFormula, (refValue,))
        result = mycursor.fetchone()

        if result:
            return result[0]
        else:
            return None
    finally:
        mycursor.close()
        mydb.close()

def getNameFromDb(table, refColumn, targetColumn):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        sqlFormula = f"SELECT `{targetColumn}` FROM `{table}` WHERE `{refColumn}` IS NULL"
        mycursor.execute(sqlFormula, )
        results = mycursor.fetchall()

        if results:
            return [result[0] for result in results]
        else:
            return None
    finally:
        mycursor.close()
        mydb.close()

def getTableFromDb(table):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        mycursor.execute(f"SELECT * FROM `{table}`")
        result = mycursor.fetchall()
        return result
    finally:
        mycursor.close()
        mydb.close()

def logCheckExist(item):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        sql = "SELECT * FROM login WHERE accountName = %s"
        mycursor.execute(sql, (item,))
        myresult = mycursor.fetchall()
    finally:
        mycursor.close()
        mydb.close()
    if len(myresult) == 0:
        return False
    else:
        return True

def countRows(table):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        sqlFormula = f"SELECT COUNT(*) FROM `{table}`"
        mycursor.execute(sqlFormula)
        result = mycursor.fetchone()
        return result[0]
    finally:
        mycursor.close()
        mydb.close()

def countdown():
    ph = st.empty()
    N = 5*60
    for secs in range(N,0,-1):
        mm, ss = secs//60, secs%60
        ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
        time.sleep(1)


#debug tool method
def deleteTable(tableName):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        mycursor.execute(f"DROP TABLE IF EXISTS `{tableName}`")
        mydb.commit()
        print(f"Table `{tableName}` deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        mycursor.close()
        mydb.close()


def deleteMultipleTables(num_tables):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()

        tables_to_delete = tables[:num_tables]

        for table in tables_to_delete:
            table_name = table[0]
            deleteTable(table_name)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        mycursor.close()
        mydb.close()

def printTableContents(table):
    mydb = dbConnection()
    mycursor = mydb.cursor()
    try:
        sqlFormula = f"SELECT * FROM `{table}`"
        mycursor.execute(sqlFormula)

        rows = mycursor.fetchall()

        for row in rows:
            print(row)
    finally:
        mycursor.close()
        mydb.close()




'''
table_name = "561-161"
printTableContents(table_name)

tableName = "119-294"
deleteTable(tableName)

deleteMultipleTables(20)
'''


