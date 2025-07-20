import matplotlib.pyplot as pl
import sqlite3
conn=sqlite3.connect("markss.db")
cur=conn.cursor()
cur.execute("select * from markss")
rows=cur.fetchall()

    
import pandas as pd
df=pd.read_sql_query("select * from markss where clas='10th' order by tText asc ",conn)
fig = pl.figure()
fig.set_facecolor("royalblue")
fig = pl.axes()
fig.set_facecolor("deeppink")

pl.xlabel("Students",color='red',fontsize=20)
pl.ylabel("Marks",color='red',fontsize=20)
y=df['tText']
x=df['name']
pl.bar(x,y,width=0.2,color='gold',hatch='ox')
for num in range(len(x)):
    pl.text(num,y[num],y[num],ha='center',va='bottom')
pl.title("CLASS 10TH STUDENTS MARKS",color='r',fontsize=22)
pl.grid(True)
pl.annotate('MAY AMMA \n BLESS US \n ALL!!!', (0,0), (-130,350), color='gold',fontsize=18,fontstyle='oblique',
             xycoords='axes fraction', textcoords='offset points', va='bottom')
pl.get_current_fig_manager().window.state('zoomed')
pl.show()


















