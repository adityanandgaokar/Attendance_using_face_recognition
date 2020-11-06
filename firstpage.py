from tkinter import *

import os
from datetime import datetime;
root=Tk()

root.configure(background="white")


#root.geometry("300x300")

def function1():
    
    os.system("py datasetcapture.py")
    
def function2():
    
    os.system("py trainingdataset.py")

def function3():

    os.system("py recog.py")
    

def function4():

    root.destroy()

#def attend():
    #os.startfile("attendanceNew folder2019-06-08.xls")

image1 = PhotoImage(file = r'D:/Projects/Face Recognition of mine/data_collection.png') 

image1 =image1.subsample(2, 2) 



root.title("ATTENDANCE MANAGEMENT USING FACE RECOGNITION")


Label(root, text="ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="orange",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


Button(root,text="Create Dataset", image = image1, font=("times new roman",30),bg="#0D47A1",fg='white',command=function1, compound=CENTER).grid(row=3,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


Button(root,text="Train Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


Button(root,text="Recognize + Attendance",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


#Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#0D47A1",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function4).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
