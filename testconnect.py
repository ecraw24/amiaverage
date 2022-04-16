import psycopg2, os

DATABASE_URL = os.environ.get('DATABASE_URL')
DB_USER = "nvalcjgkjirosy"
DB_PASS = "a1d078c1ef28b3ccb5d5f9ff4583e42243fbd419766d05dacafd70e3dbd79d62"
DB_PORT = 5432
con = None
try:
    con = psycopg2.connect(DATABASE_URL, user=DB_USER, password=DB_PASS, port=DB_PORT)
    cur = con.cursor()

    print('PostgresSQL database version:')
    cur.execute('SELECT version()')

    db_version = cur.fetchone()
    print(db_version)
    cur.close()
except Exception as error:
    print('Cause: {}'.format(error))

finally:
    if con is not None:
        con.close()
        print('DB connection close')

