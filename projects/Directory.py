import sys
import os
import tkinter
from tkinter.ttk import *
from tkinter import *

def main():
    
    def Add():
        global mail_add    
        add.destroy()
        delete.destroy()
        update.destroy()
        var1 = tkinter.IntVar()
        
        def Confirm():
            with open('directory.txt', 'w') as f:
                f.write(f"Name: {name.get()}\nAddress: {address.get()}\nMailing Address: {mail_add}") 
        
        def restart_program():
            os.system("clear")  
            python = sys.executable
            os.execl(python, python, * sys.argv)
            
        def entry():
            if var1.get() == 1:
                mailing_Address.delete(0,END)
                mailing_Address.update()
                mailing_Address.config(state="disabled")
            elif var1.get() == 0:
                mailing_Address.config(state="normal")
                mailing_Address.update()      
                      
        def next_wind():     
            if var1.get() == 1:
                mail_add = address.get()
            elif var1.get() == 0:
                mail_add = mailing_Address.get()
            
            instruct.config(text="Is the information below correct? If so, press confirm for it to be added to the directory.")    
            Display = Label(Directory,text=f"Name: {name.get()}\nAddress: {address.get()}\nMailing Address: {mail_add}\n")
            Display.pack()
            
            Name.destroy()
            name.destroy()
            Address.destroy()
            address.destroy()
            Mailing_Address.destroy()
            mailing_Address.destroy()
            c1.destroy()
            Next.destroy()
            
            confirm = Button(Directory,text="Confirm",command=Confirm)
            confirm.pack(side=tkinter.BOTTOM)
            
            back = Button(Directory,text="Back",command=restart_program)
            back.pack(side=tkinter.BOTTOM)
                
        #adding info about person
        Name = Label(Directory,text="Name:",font=('Helvetica',18))
        Name.pack()
        
        name = tkinter.Entry(Directory)
        name.focus_set()
        name.pack()
        
        Address = Label(Directory,text="Address:",font=('Helvetica',18))
        Address.pack()
        
        address = tkinter.Entry(Directory)
        address.focus_set()
        address.pack()
        
        Mailing_Address = Label(Directory,text="Mailing Address:",font=('Helvetica',18))
        Mailing_Address.pack()
        
        mailing_Address = tkinter.Entry(Directory)
        mailing_Address.focus_set()
        mailing_Address.pack()
        
        c1 = Checkbutton(Directory,text="Is the Mailing Address the same as the Address above?",variable=var1,onvalue=1,offvalue=0,command=entry)
        c1.pack()
        
        Next = Button(Directory,text="Next",command=next_wind)
        Next.pack(side=tkinter.BOTTOM)

        
    def Update():
        add.destroy()
        delete.destroy()
        update.destroy()
        
    def Delete():
        add.destroy()
        delete.destroy()
        update.destroy()

    
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
    
    with open('directory.txt', 'w') as f:
        f.write('Directory:')
    
    #create GUI with title    
    Directory = Tk()
    Directory.title("Directory")
    Directory.geometry("750x750")

    main()
            
    #start GUI
    Directory.mainloop()

