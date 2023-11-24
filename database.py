import psycopg2 as psy

def connect():
    try:
        global conn, cur
        conn = psy.connect(host = 'localhost', dbname = 'postgres', user = 'postgres', password = 'Anthasanafro15!', port = 5432)
        cur = conn.cursor()
    except:
        print("could not connect to database")

def disconnect():
    cur.close()
    conn.close()

def add_password(u, p, a):
    cur.execute("INSERT INTO passwords (username, password, app) VALUES (%s, %s, %s)", (u, p ,a))
    conn.commit()
    
def data():
    cur.execute("SELECT * FROM passwords;")
    result = cur.fetchall()
    print(result)




