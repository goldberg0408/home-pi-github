import MySQLdb
import matplotlib.pyplot as plt

## xpoint, ypoint (x = time, y = temperature)

sql = "select t_time, t_temperature from temperature where t_day = '05'"
db = MySQLdb.connect("localhost","root","1234","SCOTT")
cur = db.cursor()
cur.execute(sql)
row = cur.fetchall()

x=[]
y=[]

for i in row:
    x.append(i[0])
    y.append(i[1])
    print(int(i[0]), int(i[1]))

plt.title('temperature')
plt.xlabel('time')
plt.ylabel('temperature')
plt.xlim([0,24])
plt.plot(x,y)
plt.savefig("lineexampl.png", dpi=350)
plt.show()
cur.close()
db.close()
