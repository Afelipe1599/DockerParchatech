from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Backend!"}

@app.get("/db-status")
def db_status():
    try:
        conn = psycopg2.connect(
            dbname="mydatabase",
            user="admin",
            password="admin123",
            host="database",
            port="5432",
        )
        conn.close()
        return {"status": "Database connected successfully!"}
    except Exception as e:
        return {"status": "Failed to connect to the database", "error": str(e)}
