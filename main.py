from fastapi import FastAPI
import psycopg2

app = FastAPI(
    title='Trading App'
)

DB_NAME = "tg_bot"
DB_USER = "postgres"
DB_PASSWORD = "xuxin1999"
DB_HOST = "localhost"
DB_PORT = 5432


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

cur = conn.cursor()
cur.execute('select * from users')

rows = cur.fetchall()
columns = [desc[0] for desc in cur.description]
print(columns)


# Convert each row to a dictionary and append to a list
users = []
for row in rows:
    row_dict = {}
    for i in range(len(columns)):
        row_dict[columns[i]] = row[i]
    users.append(row_dict)

# Close the cursor and connection
cur.close()
conn.close()

@app.get('/users/{user_id}') # Точка входа
def get_user(user_id: int):
    return [user for user in users if user['id'] == user_id]
