import psycopg2
import os

DATABASE_URL = os.getenv('DATABASE_URL')

def get_conn():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    