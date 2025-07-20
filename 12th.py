import matplotlib.pyplot as pl
import sqlite3
conn=sqlite3.connect("markss.db")
cur=conn.cursor()
cur.execute("select * from markss")
rows=cur.fetchall()

    
import pandas as pd
df=pd.read_sql_query("select * from markss where clas='12th' order by tText  ",conn)
fig = pl.figure()
fig.set_facecolor("teal")
fig = pl.axes()
fig.set_facecolor("green")

pl.xlabel("Students",color='red',fontsize=20)
pl.ylabel("Marks",color='red',fontsize=20)
y=df['tText']
x=df['name']
pl.xticks(rotation = 50)
pl.bar(x,y,width=0.2,color='gold',hatch='ox')
pl.title("CLASS 12TH STUDENTS MARKS",color='r',fontsize=22)
pl.grid(axis='y')
pl.annotate('MAY AMMA \n BLESS US \n ALL!!!', (0,0), (-130,350), fontsize=18,fontstyle='italic',
             xycoords='axes fraction', textcoords='offset points', va='bottom')
pl.get_current_fig_manager().window.state('zoomed')
pl.show()


















