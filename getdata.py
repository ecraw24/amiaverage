import psycopg2
import psycopg2.extras as ext
# next is needed
import os



#next is needed
DATABASE_URL = os.environ.get('DATABASE_URL')
#DB_HOST = "ec2-3-217-251-77.compute-1.amazonaws.com"
#DB_USER = "nvalcjgkjirosy"
#DB_PASSWORD = "a1d078c1ef28b3ccb5d5f9ff4583e42243fbd419766d05dacafd70e3dbd79d62"
#DB_NAME = "d4ecfjhp2gbtco"
conn = psycopg2.connect(DATABASE_URL)
DB_HOST = "ec2-3-217-251-77.compute-1.amazonaws.com"
DB_USER = "nvalcjgkjirosy"
DB_PASSWORD = "a1d078c1ef28b3ccb5d5f9ff4583e42243fbd419766d05dacafd70e3dbd79d62"
DB_NAME = "d4ecfjhp2gbtco"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)



cur = conn.cursor()



##### YOUR CODE GOES HERE ####################






cur.execute("SELECT * FROM skillsinfo;")
data = cur.execute("SELECT * FROM skillsinfo;")

print(data)

skill_name1 = cur.execute("SELECT Skill_name FROM skillsinfo WHERE id=1;")

print(skill_name1)




#############################################

conn.commit()




cur.close()








conn.close()


























