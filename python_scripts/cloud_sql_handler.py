from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql
import logging
import os
import csv
import json


def create_table(table_name: str, table_schema):
    create_stmt = sqlalchemy.text(f"CREATE TABLE IF NOT EXISTS {table_name} {table_schema}")
    print(create_stmt)
    try:
        with pool.connect() as db_conn:
            try:
                with db_conn.begin():
                    db_conn.execute(create_stmt)
            except Exception as e:
                print("Error inside with", e)
    except Exception as e:
        print("Error outside with", e)


    return

def insert_data(table_name: str, table_schema, parameters):

    # insert statement
    insert_stmt = sqlalchemy.text(
        f"INSERT INTO {table_name} {table_schema} VALUES (:ID, :First_Name, :Last_Name, :Email, :Phone)",
    )

    with pool.connect() as db_conn:
        try:
            with db_conn.begin():
                result = db_conn.execute(insert_stmt, parameters)
        except Exception as e:
            logging.error(e)
            raise e

    return result


def query_data(query):
    with pool.connect() as db_conn:
        try:
            with db_conn.begin():
                result = db_conn.execute(sqlalchemy.text(query)).fetchall()
        except Exception as e:
            logging.error(e)
            raise e

    result_list = []

    # Do something with the results
    for row in result:
        result_list.append(row)
    
    return result_list


def drop_table(table_name):
    drop_stmt = sqlalchemy.text(f"DROP TABLE {table_name}")

    with pool.connect() as db_conn:
        try:
            with db_conn.begin():
                result = db_conn.execute(drop_stmt)
        except Exception as e:
            logging.error(e)
            raise e
    
    return True


# build connection
def getconn() -> pymysql.connections.Connection:
    with Connector() as connector:
        conn = connector.connect(
            "workshop-project-0606:us-central1:workshop-instance",
            "pymysql",
            user="admin",
            password="admin",
            db="practice-dataset"
        )
    return conn

# create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)


def main():

    # Get config information
    with open("config.json") as f:
        config = json.load(f)
    
    # Get project-id
    project_id = config["gcp_project_id"]

    # Get csv file path
    file_path = config["sql_data_csv"]
    csv_file_path = os.path.join(os.getcwd(), file_path)

    # Get SQL table name to be used
    table_name = config["sql_table_name"]

    ##### Create table with the provided schema #####
    create_table(table_name, "( ID int, First_Name varchar(255), Last_Name varchar(255), Email varchar(255), Phone varchar(255) ,PRIMARY KEY(ID))")
    
    rows_list = []

    with open(csv_file_path, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # print(row)
            row.update({"First_Name": row.pop("First Name"), "Last_Name": row.pop("Last Name")})
            updated_row = dict((k, row[k]) for k in ['ID', 'First_Name', 'Last_Name', 'Email', 'Phone'] if k in row)
            rows_list.append(updated_row)
    
    ##### Insert data into the table with the given schema and parameters #####
    # response = insert_data(table_name, "(ID, First_Name, Last_Name, Email, Phone)", rows_list)

    ##### Query data by providing the query #####
    result = query_data(f"SELECT * from {table_name}")
    print(result)

    ##### Drop the table #####
    # res = drop_table(table_name)
    # print(res)


if __name__ == "__main__":
    main()
