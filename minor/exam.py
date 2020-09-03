from tkinter import*
import sqlite3
from tkinter import messagebox as ms

#path of database
conn=sqlite3.connect("C:/Users/ayush/Desktop/python/HMS/database/registration.db")
c=conn.cursor()



class student_page:
	
	def __init__(self, master, *args, **kwargs):
		self.master=master
		self.t=StringVar()
		

		self.h1=Label(master,text="SEARCH....", font=("arial 20 bold")).place(x=400,y=0)
		
		self.a0=Label(master,text="Enrollment no. :",width=15,height=2,font=('arial',15,'bold')).place(x=350,y=60)
		self.entry=Entry(master,textvariable=self.t).place(x=530,y=80,width=190)
		self.btn_0=Button(master, text="SEARCH",command=self.search, width=12,height=2,bg='yellow').place(x=750,y=60)
	   

		#personal details...
		self.h3=Label(master,text="PERSONAL DETAILS :\n",font=('script mj',14,'underline')).place(x=10,y=120)

		self.a1=Label(root,text="Student's Name :",width=15,height=2,font=('arial',12,'bold')).place(x=0,y=160)
		self.entry1=Entry(root)
		self.entry1.place(x=160,y=172)

		self.a2=Label(root,text="Date of Birth :",width=15,height=2,font=('arial',12,'bold')).place(x=320,y=160)
		self.entry2=Entry(root)
		self.entry2.place(x=480,y=172)
		
		self.a3=Label(root,text="Mother's Name :",width=15,height=2,font=('arial',12,'bold')).place(x=0,y=200)
		self.entry3=Entry(root)
		self.entry3.place(x=160,y=212)

		self.a4=Label(root,text="Father's Name :",width=18,height=2,font=('arial',12,'bold')).place(x=310,y=200)
		self.entry4=Entry(root)
		self.entry4.place(x=480,y=212)

		self.a5=Label(root,text="Permanent\nAddress :",width=15,height=3,font=('arial',12,'bold')).place(x=-19,y=250)
		self.entry5=Entry(root)
		self.entry5.place(x=160,y=270,relwidth=0.36,relheight=0.03)
	   
		self.a6=Label(root,text="Gender :",width=15,height=2,font=('arial',12,'bold')).place(x=-28,y=320)
		self.entry6=Entry(root)
		self.entry6.place(x=160,y=332)
		
		self.a7=Label(root,text="E-mail :",width=15,height=2,font=('arial',12,'bold')).place(x=-30,y=360)
		self.entry7=Entry(root)
		self.entry7.place(x=160,y=372)

		self.a8=Label(root,text="Contact no. :",width=15,height=2,font=('arial',12,'bold')).place(x=320,y=360)
		self.entry8=Entry(root)
		self.entry8.place(x=480,y=372)
		
		#local guardian's details...
		self.h3=Label(master,text="LOCAL GUARDIAN'S DETAILS (LG) :\n",font=('script mj',14,'underline')).place(x=10,y=430)
		
		self.a9=Label(root,text="LG Name :",width=15,height=2,font=('arial',12,'bold')).place(x=0,y=470)
		self.entry9=Entry(root)
		self.entry9.place(x=160,y=482)

		self.a10=Label(root,text="Permanent\nAddress of LG :",width=15,height=2,font=('arial',12,'bold')).place(x=-12,y=520)
		self.entry10=Entry(root)
		self.entry10.place(x=160,y=522)

		self.a11=Label(root,text="Relation with LG :",width=15,height=2,font=('arial',12,'bold')).place(x=320,y=470)
		self.entry11=Entry(root)
		self.entry11.place(x=480,y=482)

		self.a12=Label(root,text="Contact no. of LG :",width=15,height=2,font=('arial',12,'bold')).place(x=0,y=600)
		self.entry12=Entry(root)
		self.entry12.place(x=160,y=612)

		#college details...
		self.h4=Label(master,text="COLLEGE DETAILS :\n",font=('script mj',14,'underline')).place(x=700,y=120)

		self.a13=Label(root,text="Name of School :",width=15,height=2,font=('arial',12,'bold')).place(x=700,y=160)
		self.entry13=Entry(root)
		self.entry13.place(x=860,y=172,relwidth=0.2,relheight=0.03)

		self.a14=Label(root,text="Year",width=15,height=2,font=('arial',12,'bold')).place(x=660,y=200)
		self.entry14=Entry(root)
		self.entry14.place(x=860,y=212)

		self.a15=Label(root,text="Branch",width=15,height=2,font=('arial',12,'bold')).place(x=673,y=240)
		self.entry15=Entry(root)
		self.entry15.place(x=860,y=252)

		self.a16=Label(root,text="Fee reciept :",width=15,height=2,font=('arial',12,'bold')).place(x=680,y=280)
		self.entry16=Entry(root)
		self.entry16.place(x=860,y=292,relwidth=0.2,relheight=0.03)

		self.btn_2=Button(master, text="CLEAR",width=12,height=2,bg='red',command=self.clear_all).place(x=650,y=650)

		
		
	def search(self, *args, **kwargs):
		

		self.s=self.t.get()
		sql = "SELECT * FROM student_registration WHERE rollno=?"
		result = c.execute(sql,( self.s, ))
		for r in result:
			self.n1=r[1]
			self.n2=r[2]
			self.n3=r[3]
			self.n4=r[4]
			self.n5=r[5]
			self.n6=r[6]
			self.n7=r[7]
			self.n8=r[8]
			self.n9=r[9]
			self.n10=r[10]
			self.n11=r[11]
			self.n12=r[12]
			self.n13=r[13]
			self.n14=r[14]
			self.n15=r[15]
			self.n16=r[16]
		conn.commit()
			
		#for update
		self.entry1.delete(0, END)
		self.entry1.insert(0,str(self.n1))
			
		self.entry2.delete(0, END)
		self.entry2.insert(0,str(self.n2))

		self.entry3.delete(0, END)
		self.entry3.insert(0,str(self.n3))

		self.entry4.delete(0, END)
		self.entry4.insert(0,str(self.n4))

		self.entry5.delete(0, END)
		self.entry5.insert(0,str(self.n5))

		self.entry6.delete(0, END)
		self.entry6.insert(0,str(self.n6))

		self.entry7.delete(0, END)
		self.entry7.insert(0,str(self.n7))

		self.entry8.delete(0, END)
		self.entry8.insert(0,str(self.n8))

		self.entry9.delete(0, END)
		self.entry9.insert(0,str(self.n9))

		self.entry10.delete(0, END)
		self.entry10.insert(0,str(self.n10))

		self.entry11.delete(0, END)
		self.entry11.insert(0,str(self.n11))

		self.entry12.delete(0, END)
		self.entry12.insert(0,str(self.n12))

		self.entry13.delete(0, END)
		self.entry13.insert(0,str(self.n13))

		self.entry14.delete(0, END)
		self.entry14.insert(0,str(self.n14))

		self.entry15.delete(0, END)
		self.entry15.insert(0,str(self.n15))

		self.entry16.delete(0, END)
		self.entry16.insert(0,str(self.n16))
		conn.commit()

	def clear_all(self):
			self.entry1.delete(0, END)
			self.entry2.delete(0, END)
			self.entry3.delete(0, END)
			self.entry4.delete(0, END)
			self.entry5.delete(0, END)
			self.entry6.delete(0, END)
			self.entry7.delete(0, END)
			self.entry8.delete(0, END)
			self.entry9.delete(0, END)
			self.entry10.delete(0, END)
			self.entry11.delete(0, END)
			self.entry12.delete(0, END)
			self.entry13.delete(0, END)
			self.entry14.delete(0, END)
			self.entry15.delete(0, END)
			self.entry16.delete(0, END)
			

		
root=Tk()
b=student_page(root)
root.title("HOSTEL MANAGEMENT SYSTEM")
width = 1250
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

root.mainloop()

