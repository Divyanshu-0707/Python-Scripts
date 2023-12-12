import mysql.connector
import pandas as pd

# Replace these with your MySQL server and database information
host = "localhost"
user = "DS"  # USERNAME
password = "saraswat@17"  # PASSWORD
database = "IndianNamesDatabase"

# Create a connection to the MySQL server
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Create a new table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS MyTable (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Name1 VARCHAR(255),
            Name2 VARCHAR(255),
            Name3 VARCHAR(255),
            Name4 VARCHAR(255)
        )
        """
        cursor.execute(create_table_query)
        connection.commit()

        # Insert some data into the table
        insert_data_query = """
        INSERT INTO MyTable (Name1, Name2, Name3, Name4)
        VALUES ('John', 'Doe', 'Alice', 'Smith'),
               ('Jane', 'Johnson', 'Asimov', 'Brown')
               ('Bill', 'William', 'Albert', 'Brown')
               ('Joe', 'Henery', 'Bob', 'Brown')
        """
        cursor.execute(insert_data_query)
        connection.commit()

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")


try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        # Retrieve data from the MySQL table into a DataFrame
        query = "SELECT * FROM MyTable"
        df = pd.read_sql(query, connection)

        # Print the DataFrame
        print(df)

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")

        #12/12/23
