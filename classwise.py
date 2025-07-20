import matplotlib.pyplot as pl
import sqlite3
conn=sqlite3.connect("markss.db")
cur=conn.cursor()
cur.execute("select * from markss")
rows=cur.fetchall()

    
import pandas as pd
df=pd.read_sql_query("select clas,tText from markss order by tText ",conn)
fig = pl.figure()
fig.set_facecolor("pink")
fig = pl.axes()
fig.set_facecolor("yellow")

x=df['clas']
y=df['tText']
pl.xlabel("CLASSES",color='blue',fontsize=20)
pl.ylabel("MARKS",color='green',fontsize=20)
pl.bar(x,y,width=0.5,edgecolor='green')
pl.title("CLASS WISE MARK DETAILS",color='r',fontsize=22)
pl.legend(labels=['CLASSES','MARKS'])
pl.get_current_fig_manager().window.state('zoomed')
pl.show()

