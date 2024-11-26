import sqlite3

# Create or connect to SQLite database
def create_database():
    conn = sqlite3.connect('bmi_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bmi_records (
            id INTEGER PRIMARY KEY,
            name TEXT,
            height REAL,
            weight REAL,
            bmi REAL,
            category TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_bmi_record(name, height, weight, bmi, category):
    conn = sqlite3.connect('bmi_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bmi_records (name, height, weight, bmi, category)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, height, weight, bmi, category))
    conn.commit()
    conn.close()

def fetch_bmi_records():
    conn = sqlite3.connect('bmi_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM bmi_records')
    records = cursor.fetchall()
    conn.close()
    return records

def delete_bmi_record(record_id):
    conn = sqlite3.connect('bmi_data.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM bmi_records WHERE id = ?', (record_id,))
    conn.commit()
    conn.close()