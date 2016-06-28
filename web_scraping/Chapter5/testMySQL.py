import pymysql

conn = pymysql.connect(host='192.168.33.10', user='root', passwd='root', db='scraping')
cur = conn.cursor()
cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()
