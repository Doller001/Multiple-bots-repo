import sqlite3

conn = sqlite3.connect("bot.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY
)
""")
conn.commit()


def add_user(user_id: int):
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()


def get_all_users():
    cur.execute("SELECT user_id FROM users")
    return [row[0] for row in cur.fetchall()]


def total_users():
    cur.execute("SELECT COUNT(*) FROM users")
    return cur.fetchone()[0]
