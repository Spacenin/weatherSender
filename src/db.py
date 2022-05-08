import json
import mysql.connector
from mysql.connector import Error

#Function to get connection to mysql database
def getConnection():
    connection = None

    #Load JSON with login details
    with open("/home/pi/Code/pys/weatherSend/data/db.json") as jsonFile:
        dataForBase = json.load(jsonFile)

    #Create connection to mysql db
    try:
        connection = mysql.connector.connect(host=dataForBase["hostname"], user=dataForBase["user"], passwd=dataForBase["pass"], database=dataForBase["db"])
    
    except Error as err:
        print(f"Error: ' {err}'")

    return(connection)

#Get all numbers currently stored as (zipcode, name, number)
def getNumbers():
    #Create connection
    connection = getConnection()
    
    if connection:
        cursor = connection.cursor()

        #Setup query
        query = """
            SELECT * FROM numberSet
        """

        #Run query and return results
        try:
            cursor.execute(query)
            resultSet = cursor.fetchall()

        except Error as err:
            print(f"Error: '{err}'")
            resultSet = None
        
        return(resultSet)

    else:
        return(None)