
import matplotlib.pyplot as pl
import sqlite3
conn=sqlite3.connect("stu.db")
cur=conn.cursor()
cur.execute("select * from stu")
rows=cur.fetchall()



    
import pandas as pd
df=pd.read_sql_query("select clas,mon,present,abse from stu  order by present ",conn)
fig = pl.figure()
fig.set_facecolor("pink")
fig = pl.axes()
fig.set_facecolor("yellow")

x=df['clas']
y=df['present']
z=df['abse']

pl.xlabel("CLASSES",color='blue',fontsize=20)
pl.ylabel("Attendance",color='green',fontsize=20)
pl.bar(x,y,width=0.5,edgecolor='green')
pl.bar(x,z,width=0.5)
pl.title("CLASS WISE ATTENDANCE DETAILS",color='r',fontsize=22)
pl.legend(labels=['Present','Absent'])
pl.get_current_fig_manager().window.state('zoomed')
pl.show()
