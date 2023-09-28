import os
import psycopg2

# PostgreSQL database connection parameters
db_params = {
    "host": "localhost",
    "database": "piscineds",  # Your database name
    "user": "rmorel",          # Your database user
    "password": "mysecretpassword",  # Your database password
    "port": "5432"             # Your PostgreSQL port
}

# Directory containing the CSV files
csv_dir = "../data/subject/customer/"

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# List all CSV files in the directory
csv_files = [f for f in os.listdir(csv_dir) if f.endswith(".csv")]

# Iterate through the CSV files and create a database for each
for csv_file in csv_files:
    # Extract the database name from the CSV file name (without the extension)
    db_name = os.path.splitext(csv_file)[0]
    print(f"Creating database {db_name}...")

    # SQL script to create the table and load data
    sql_script = f"""
    DROP TABLE IF EXISTS {db_name};
    CREATE TABLE {db_name} (
        id BIGSERIAL PRIMARY KEY,
        event_time TIMESTAMP,
        event_type VARCHAR(50),
        product_id INTEGER NOT NULL,
        price FLOAT,
        user_id BIGINT NOT NULL,
        user_session VARCHAR(100)
    );

    COPY {db_name}(event_time, event_type, product_id, price, user_id, \
            user_session)
    FROM '{os.path.join(csv_dir, csv_file)}'
    DELIMITER ','
    CSV HEADER;
    """

    # Execute the SQL script
    cursor.execute(sql_script)
    conn.commit()

    print("Created.")

# Close the database connection
cursor.close()
conn.close()
