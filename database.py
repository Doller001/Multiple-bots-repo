import sqlite3

conn = sqlite3.connect("bot.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY
)
""")
conn.commit()

def add_user(uid):
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (uid,))
    conn.commit()

def get_all_users():
    cur.execute("SELECT user_id FROM users")
    return [x[0] for x in cur.fetchall()]

def total_users():
    cur.execute("SELECT COUNT(*) FROM users")
    return cur.fetchone()[0]
