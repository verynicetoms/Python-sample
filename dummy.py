#pip install psycopg2-binary
import psycopg2
import random


def generate_dummy_data():
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ivy", "Jack"]
    genders = ["Male", "Female"]
    
    name = random.choice(names)
    email = f"{name.lower()}@example.com"
    phone = f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    gender = random.choice(genders)
    
    return name, email, phone, gender


conn = psycopg2.connect(
    dbname="dbname",
    user="username",
    password="password",
    host="writeendpoint",
    port="port"
)
cursor = conn.cursor()


create_table_query = '''
    CREATE TABLE IF NOT EXISTS dummy_table (
        id SERIAL PRIMARY KEY,
        name TEXT,
        email TEXT,
        phone TEXT,
        gender TEXT
    )
'''
cursor.execute(create_table_query)
conn.commit()

for _ in range(10):
    name, email, phone, gender = generate_dummy_data()
    insert_query = '''
        INSERT INTO dummy_table (name, email, phone, gender)
        VALUES (%s, %s, %s, %s)
    '''
    data = (name, email, phone, gender)
    cursor.execute(insert_query, data)
    conn.commit()


conn.close()

print("good.")