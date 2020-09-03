from tkinter import*
import sqlite3
from tkinter import messagebox

#path of database
conn=sqlite3.connect("C:/Users/ayush/Desktop/python/HMS/database/registration.db")
c=conn.cursor()

class student_page:
	
	def __init__(self, master, *args, **kwargs):
		self.master=master
		self.gender = StringVar(root)
		
		
		self.h1=Label(master,text="GAUTAM BUDDHA UNIVERSITY\nGREATER NOIDA", font=("arial 20 bold")).place(x=400,y=0)
		self.h2=Label(master,text="STUDENT'S HOSTEL ALLOTMENT FORM 2018-19", font=("arial 16")).place(x=360,y=70)
		
		self.h0=Label(master,text="NOTE : ALL THE ENTRIES ARE COMPULSARY TO FILL", font=("arial 8 underline")).place(x=10,y=100)

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

		self.a5=Label(root,text="Permanent\nAddress :",width=15,height=2,font=('arial',12,'bold')).place(x=-19,y=250)
		self.entry5=Entry(root)
		self.entry5.place(x=160,y=250)

		self.CHOICES_gender = {'MALE', 'FEMALE', 'TRANSGENDER'}
		self.gender.set('select')
		self.gender_menu = OptionMenu(master, self.gender, *self.CHOICES_gender)
		Label(master, text="Gender :",width=15,height=2,font=('arial',12,'bold')).place(x=-28,y=300)
		self.gender_menu.place(x=160,y=312)
		
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

		self.a14=Label(root,text="Enrollment no. :",width=15,height=2,font=('arial',12,'bold')).place(x=700,y=200)
		self.entry14=Entry(root)
		self.entry14.place(x=860,y=212,relwidth=0.2,relheight=0.03)

		self.CHOICES_year = {'1', '2', '3', '4', '5'}
		self.gender.set('select')
		self.gender_menu = OptionMenu(master, self.gender, *self.CHOICES_gender)
		Label(master, text="Gender :", width=15, height=2, font=('arial', 12, 'bold')).place(x=-28, y=300)
		self.gender_menu.place(x=160, y=312)

		# self.a15=Label(root,text="Year:",width=15,height=2,font=('arial',12,'bold')).place(x=660,y=240)
		# self.entry15=Entry(root)
		# self.entry15.place(x=860,y=252)

		self.a16=Label(root,text="Branch :",width=15,height=2,font=('arial',12,'bold')).place(x=673,y=280)
		self.entry16=Entry(root)
		self.entry16.place(x=860,y=292)

		self.a17=Label(root,text="Fee reciept no. :",width=15,height=2,font=('arial',12,'bold')).place(x=700,y=320)
		self.entry17=Entry(root)
		self.entry17.place(x=860,y=332,relwidth=0.2,relheight=0.03)

		self.btn_1=Button(master, text="SUBMIT",command=self.get_items,width=12,height=2,bg='green').place(x=550,y=650)
		self.btn_2=Button(master, text="CLEAR",command=self.clear_all,width=12,height=2,bg='red').place(x=650,y=650)
		
		self.master.bind("<Return>,self.get_items")
		self.master.bind("<Up>,self.clear_all")

	#inserting into database    
	def get_items(self):
		self.g1=self.entry1.get()
		self.g2=self.entry2.get()
		self.g3=self.entry3.get()
		self.g4=self.entry4.get()
		self.g5=self.entry5.get()
		self.g6=self.gender.get()
		self.g7=self.entry7.get()
		self.g8=self.entry8.get()
		self.g9=self.entry9.get()
		self.g10=self.entry10.get()
		self.g11=self.entry11.get()
		self.g12=self.entry12.get()
		self.g13=self.entry13.get()
		self.g14=self.entry14.get()
		self.g15=self.entry15.get()
		self.g16=self.entry16.get()
		self.g17=self.entry17.get()

		if self.g1=="" or self.g2=="" or self.g3=="" or self.g4=="" or self.g5=="" or self.g6=="" or self.g7=="" or self.g8=="" or self.g8=="" or self.g9=="" or self.g10=="" or self.g11=="" or self.g12=="" or self.g13=="" or self.g14=="" or self.g15=="" or self.g16=="" or self.g17=="":
			messagebox.showinfo("ERROR","please fill all the remaining entries....")
		else:
			sql="INSERT INTO student_registration (sname,dob,mname,fname,address,gender,email,contact,lname,relation,ladd,lcontact,school,rollno,year,branch,fee)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
			c.execute(sql,(self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8, self.g9, self.g10, self.g11, self.g12,  self.g13, self.g14, self.g15, self.g16, self.g17))
			conn.commit()

			messagebox.showinfo("SUCCESS","successsfully added to the database")

			
	#clear the field
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
		self.entry17.delete(0, END)

	
	# def limit(self):
	# 	self.d=StringVar()
	# 	self.value = self.d.get()
	# 	if len(self.value) > 10:
	# 		self.d.set(self.value[:10])
	# 		self.d.trace('w', limit)
	#

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
