from fastapi import FastAPI
import psycopg2

from config import DB_USER, DB_HOST, DB_NAME, DB_PASS, DB_PORT

app = FastAPI(
    title='Trading App'
)


conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

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
