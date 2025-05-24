import mysql.connector as sql
import os
from getpass import getpass

def connect_to_db():
    try:
        # Step 1: Connect without specifying a database to check/create it
        temp_conn = sql.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            passwd=os.getenv('DB_PASS', 'manager')
        )
        temp_cursor = temp_conn.cursor()
        
        # Step 2: Create the database if it doesn't exist
        db_name = os.getenv('DB_NAME', 'AUTO_MOBILE_SURVICE_STATION')
        temp_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        temp_conn.commit()
        temp_conn.close()

        # Step 3: Reconnect with the database specified
        conn = sql.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            passwd=os.getenv('DB_PASS', 'Badalmunda@0183'),
            database=db_name
        )
        if conn.is_connected():
            print("Successfully Connected")
        return conn

    except sql.Error as e:
        print(f"Database connection error: {e}")
        return None

def insert_customer(conn):
    try:
        c1 = conn.cursor()
        v_sno = int(input("Enter the serial Number: "))
        v_cname = input("Enter the customer name: ")
        v_cdetails = input("Enter the customer details: ")
        v_caddress = input("Enter the customer address: ")
        v_cpincode = int(input("Enter the pincode: "))
        v_cpuramt = int(input("Enter the pur amt: "))
        v_cdisc = float(input("Enter the discount: "))

        V_SQL_Insert = """
            INSERT INTO customer_details 
            (sno, cname, cdetails, caddress, cpincode, cpuramt, cdisc) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        c1.execute(V_SQL_Insert, (v_sno, v_cname, v_cdetails, v_caddress, v_cpincode, v_cpuramt, v_cdisc))
        conn.commit()
        print("CUSTOMER Created Congrats!!!")
    except ValueError:
        print("Invalid input. Please enter valid data.")
    except sql.Error as e:
        print(f"Database error: {e}")

def authenticate_user(conn):
    try:
        c1 = conn.cursor()
        username = input('USERNAME: ')
        password = getpass('PASSWORD: ')
        c1.execute("SELECT * FROM user WHERE username = %s AND passwd = %s", (username, password))
        data = c1.fetchall()
        if data:
            print("Authentication successful.")
            # import main  # Uncomment if needed
        else:
            print("Invalid credentials. Try again.")
    except sql.Error as e:
        print(f"Database error: {e}")

def main():
    conn = connect_to_db()
    if not conn:
        return

    while True:
        print("\nAutomobile Service Station")
        print("1. Service Station")
        print("2. Source")
        print("3. Selling")
        print("4. Exit")
        try:
            choice = int(input("Enter the Choice: "))
            if choice == 1:
                insert_customer(conn)
            elif choice == 2:
                authenticate_user(conn)
            elif choice == 3:
                print("Selling feature not implemented yet.")
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    conn.close()

if __name__ == "__main__":
    main()

