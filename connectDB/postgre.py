import traceback
import psycopg2
from psycopg2.extras import RealDictCursor

def connect(h, d, u, pw, p):
    
    query = "CREATE TABLE ipman_list (ip TEXT PRIMARY KEY, name TEXT, address TEXT);"    
    try:
        conn = psycopg2.connect(host=h, user=u, password=pw, dbname=d, port=p)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        print(query)
        
        cur.execute(query)
        conn.commit()
        
    except Exception:
        print('Fail to connect DB')