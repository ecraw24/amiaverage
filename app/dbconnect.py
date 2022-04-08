import psycopg2.extras as ext
import psycopg2

# next is needed
import os

#next is needed
DATABASE_URL = os.environ.get('DATABASE_URL')
DB_HOST = "ec2-34-233-0-64.compute-1.amazonaws.com"
DB_USER = "uctkamhrtztovh"
DB_PASSWORD = "a19a921e11a4673df324943cf1b3616f9239d8d34bf06ffbd58ca9faa64b9b97"
DB_NAME = "d7g9b48ralreio"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, sslmode='require')

# Execute statments in here

cur = conn.cursor(cursor_factory=ext.DictCursor)

cur.execute("SELECT * FROM skillsinfo;")
print(cur.fetchall())

def enterInfo():
  skillname = cur.execute("SELECT skillname FROM skillsdetail WHERE skillid=3;")
  return skillname.fetchall()
  

conn.commit()
cur.close()
conn.close()
