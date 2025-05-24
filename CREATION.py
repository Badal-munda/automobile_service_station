import mysql.connector as sql

try:
    conn = sql.connect(
        host='localhost',
        user='root',          # Confirm this is correct
        passwd='manager',      # Replace with the correct password
        database='AUTO_MOBILE_SURVICE_STATION'
    )
    if conn.is_connected():
        print("Successfully Connected")
    c1 = conn.cursor()
    c1.execute('''
        CREATE TABLE IF NOT EXISTS customer_details(
            sno int primary key,
            customer_name varchar(25),
            customer_details varchar(30),
            customer_address varchar(30),
            customer_pincode int,
            customer_puramt int,
            customer_disc float
        )
    ''')
    print('Table created or already exists')

except sql.Error as e:
    print(f"MySQL Error: {e}")
    print("Check your username, password, or database permissions.")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed")
