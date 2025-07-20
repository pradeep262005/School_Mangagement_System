import matplotlib.pyplot as pl
import sqlite3
conn=sqlite3.connect("marks.db")
cur=conn.cursor()
cur.execute("select * from marks")
rows=cur.fetchall()

    
import pandas as pd
df=pd.read_sql_query("select clas,tText from marks order by tText ",conn)
fig = pl.figure()
fig.set_facecolor("pink")
fig = pl.axes()
fig.set_facecolor("yellow")

x=df['clas']
y=df['tText']
pl.xlabel("CLASSES",color='blue',fontsize=20)
pl.ylabel("MARKS",color='green',fontsize=20)
pl.plot(x,y,color='BLACK',marker='*',markersize=10,markeredgecolor='red')
pl.bar(x,y,width=0.5)
pl.title("CLASS WISE MARK DETAILS",color='r',fontsize=22)
pl.legend(labels=['CLASSES','MARKS'])
pl.show()
