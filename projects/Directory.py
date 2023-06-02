import sys
import os
import tkinter
from tkinter.ttk import *
from tkinter import *

def restart_program():
    os.system("clear")  
    python = sys.executable
    os.execl(python, python, * sys.argv)

def main():
    Name = StringVar(Directory,value="")
    Address = StringVar(Directory,value="")
    Mailing = StringVar(Directory,value="")
    
    def Update():
        add.destroy()
        delete.destroy()
        update.destroy()
        
    def Delete():
        add.destroy()
        delete.destroy()
        update.destroy()
        
    def Add():
        add.destroy()
        delete.destroy()
        update.destroy()
        var1 = tkinter.IntVar()
                    
        def entry():
            if var1.get() == 1:
                mailing.delete(0,END)
                mailing.update()
                mailing.config(state="disabled")
            elif var1.get() == 0:
                mailing.config(state="normal")
                mailing.update()      
                      
        def next_wind():     
            instruct.config(text="Is the information below correct? If so, press confirm for it to be added to the directory.")
            
            if var1.get() == 1:    
                Display = Label(Directory,text=f"Name: {name.get()}\nAddress: {address.get()}\nMailing Address: {address.get()}\n")
            elif var1.get() == 0:
                Display = Label(Directory,text=f"Name: {name.get()}\nAddress: {address.get()}\nMailing Address: {mailing.get()}\n")

            Display.pack()
            
            c1.destroy()
            name.destroy()
            c2.destroy()
            address.destroy()
            c3.destroy()
            mailing.destroy()
            c4.destroy()
            Next.destroy()
            back.destroy()
            
            confirm = Button(Directory,text="Confirm",command=Confirm)
            confirm.pack(side=tkinter.BOTTOM)
            
            cancel = Button(Directory,text="Back",command=restart_program)
            cancel.pack(side=tkinter.BOTTOM)
            
        def Check():
            instruct1 = Label(Directory,text="Please enter a first and last name")
            instruct2 = Label(Directory,text="Please enter an Address")
            instruct3 = Label(Directory,text="Please enter a Mailing Address")
            
            if Name.get() == "":
                instruct1.pack()
            elif Name.get() != "":
                instruct1.config(text="")
                
            if Address.get() == "":
                instruct2.pack()
            elif Address.get() != "":
                instruct2.config(text="")
                
            if Mailing.get() == "" and var1.get() == 0:
                instruct3.pack()
            elif Mailing.get() != "" and var1.get() == 0:
                instruct3.config(text="")
                
        def Confirm():
            if var1.get() == 0:
                with open("directory.txt","a") as f:
                    f.write("Name: " + Name.get() + "\n")
                    f.write("Address: " + Address.get() + "\n")
                    f.write("Mailing Address: " + Mailing.get() + "\n")
                    f.write("------------------------")
            elif var1.get() == 1:
                with open("directory.txt","a") as f:
                    f.write("Name: " + Name.get() + "\n")
                    f.write("Address: " + Address.get() + "\n")
                    f.write("Mailing Address: " + Address.get() + "\n")
                    f.write("------------------------")
                    
                    
        #adding info about person
        c1 = Label(Directory,text="Name:",font=('Helvetica',18))
        c1.pack()
        
        name = tkinter.Entry(Directory,textvariable=Name)
        name.focus_set()
        name.pack()
        
        c2 = Label(Directory,text="Address:",font=('Helvetica',18))
        c2.pack()
        
        address = tkinter.Entry(Directory,textvariable=Address)
        address.focus_set()
        address.pack()
        
        c3 = Label(Directory,text="Mailing Address:",font=('Helvetica',18))
        c3.pack()
        
        mailing = tkinter.Entry(Directory,textvariable=Mailing)
        mailing.focus_set()
        mailing.pack()
        
        c4 = Checkbutton(Directory,text="Is the Mailing Address the same as the Address above?",variable=var1,onvalue=1,offvalue=0,command=entry)
        c4.pack()
                               
        Next = Button(Directory,text="Next",command=Check)
        Next.pack(side=tkinter.BOTTOM)
        
        back = Button(Directory,text="Back",command=restart_program)
        back.pack(side=tkinter.BOTTOM)

    #instructions
    instruct = Label(Directory,text="Welcome to your Directory.",font=('Helvetica',18))
    instruct.pack()
    
    delete = Button(Directory,text="Delete Contact",command=Delete)
    delete.pack(side=tkinter.BOTTOM) 
    
    update = Button(Directory,text="Update Contact",command=Update)
    update.pack(side=tkinter.BOTTOM)
    
    add = Button(Directory,text="Add New Contact",command=Add)
    add.pack(side=tkinter.BOTTOM)
    
    
if __name__ == "__main__":
    
    with open("directory.txt","w") as f:
        f.write("Directory:\n")
    
    #create GUI with title    
    Directory = Tk()
    Directory.title("Directory")
    Directory.geometry("750x750")

    main()
            
    #start GUI
    Directory.mainloop()

