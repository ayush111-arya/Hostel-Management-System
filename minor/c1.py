from tkinter import *
import os
import sys

class buttons:
	
	def main_1(self):
		os.system('main1.py')
	def main_2(self):
		os.system('main2.py')
	def main_3(self):
		os.system('student_update.py')
	def __init__(self,master,*args,**kwargs):
		self.master=master
		
		self.l1=Label(master,text="HOSTEL MANAGEMENT SYSTEM",font=("arial 28 bold"),background="lightskyblue4").place(x=340,y=0)
		self.l2=Label(master,text="GAUTAM BUDDHA UNIVERSITY , GREATER NOIDA , UP ",font=("arial 16 bold"),background="lightskyblue4").place(x=365,y=50)
		
		self.l3=Label(master,text="STUDENTS",font=("arial 20 bold")).place(x=90,y=160)
		self.btn_1=Button(master,text="Add Student",command=self.main_1,width=12,height=2).place(x=120,y=260)
		self.btn_2=Button(master,text="Search Student",command=self.main_2,width=12,height=2).place(x=120,y=360)
		self.btn_3=Button(master,text="Update Student",command=self.main_3,width=12,height=2).place(x=120,y=460)
		self.btn_4=Button(master,text="Delete Student",width=12,height=2).place(x=120,y=560)

		self.l4=Label(master,text="OTHERS",font=("arial 20 bold")).place(x=1030,y=160)
		#self.btn_5=Button(master,text="Staff",width=12,height=2).place(x=1045,y=260)
		#self.btn_6=Button(master,text="Expenses",width=12,height=2).place(x=1045,y=360)
		#self.btn_7=Button(master,text="Fee & Room",width=12,height=2).place(x=1045,y=460)
		self.btn_8=Button(master,text="About",width=12,height=2).place(x=1045,y=560)


		
		

root=Tk()
root.configure(background="black")
photo=PhotoImage(file='ayush1.png')
root.state()
x=Label(root,image=photo, width=1250, height=680)
x.place(x=0,y=0)


b=buttons(root)

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



