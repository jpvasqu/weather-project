from tkinter import *
import mysql.connector
from tkinter import messagebox

class create:

    def __init__(self):
        self.frm_create=Frame(width=380,height=340,background="white")
        self.frm_create.place(x=225,y=65)

        btn_lbl=Button(master=self.frm_create,text="Create Account",
                       font=("Goudy Old Style",15),background="white",
                       border=0,command= self.sign_in
                       )

        self.user=Entry(master=self.frm_create,width=50,font=("Arial",10),
                        border=0)
        Frame(master=self.frm_create,width=315,height=2,
              background='black').place(x=20,y=60)

        self.passowrd=Entry(master=self.frm_create,width=50,
                            font=("Arial",10),border=0)
        Frame(master=self.frm_create,width=315,height=2,
              background='black').place(x=20,y=90)

        self.address=Entry(master=self.frm_create,width=50,
                           font=("Arial",10),border=0)
        Frame(master=self.frm_create,width=315,height=2,
              background='black').place(x=20,y=120)
        self.email=Entry(master=self.frm_create,
                         width=50,font=("Arial",10),border=0)        
        Frame(master=self.frm_create,width=315,height=2,
              background='black').place(x=20,y=150)        
        btn_lbl.place(x=130,y=5)
        #BINDING USER NAME
        def on_click(e):
            self.user.delete(0,END)
        def off_click(e):
            name=self.user.get()
            if name=="":
                self.user.insert(0,"User Name:")
        self.user.place(x=20,y=40)
        self.user.insert(0,"User Name:")
        self.user.bind('<FocusIn>',on_click)
        self.user.bind('<FocusOut>',off_click)
        #BINDING USER PASSWORD
        def on_click(e):
            self.passowrd.delete(0,END)
        def off_click(e):
            name=self.passowrd.get()
            if name=="":
                self.passowrd.insert(0,"Password:")
        self.passowrd.place(x=20,y=70)
        self.passowrd.insert(0,"Password:")
        self.passowrd.bind('<FocusIn>',on_click)
        self.passowrd.bind('<FocusOut>',off_click)
        #BINDING USER ADDRESS
        def on_click(e):
            self.address.delete(0,END)
        def off_click(e):
            name=self.address.get()
            if name=="":
                self.address.insert(0,"Address:")

        self.address.place(x=20,y=100)
        self.address.insert(0,"Address:")
        self.address.bind('<FocusIn>',on_click)
        self.address.bind('<FocusOut>',off_click)

        #BINDING USER EMAIL
        def on_click(e):
            self.email.delete(0,END)
        def off_click(e):
            name=self.email.get()
            if name=="":
                self.email.insert(0,"Email Address:")
        self.email.place(x=20,y=130)
        self.email.insert(0,"Email Address:")
        self.email.bind('<FocusIn>',on_click)
        self.email.bind('<FocusOut>',off_click)
        def create_acc():
            username = self.user.get()
            password = self.passowrd.get()
            email = self.email.get()
           
            email = self.email.get()
            data= mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='mydatabase'
                    )
            mycursor=data.cursor()
            if username == " " or password == " " or email == " ":
                messagebox.showerror(title="Invalid choy",message="Please Fill up The form")
            elif username == "User Name:":
                messagebox.showerror(title="Invalid choy",message="Invalid User Name")
            elif password == "Password:":
                messagebox.showerror(title="Invalid choy",message="Invalid Password")
            elif email == "Email Address:":
                messagebox.showerror(title="Invalid choy",message="Invalid Email Address")
            else:
               
                sql="select * from data where email=%s or email=%s"
                var=(email,email)
                mycursor.execute(sql,var)
                result=mycursor.fetchone()
                if result != None:
                    messagebox.showerror(title="Invalid choy",message=" Account Is Taken ")                  
                else:
                    sql=" insert into data(user_name,user_password,email)value(%s,%s,%s)"
                    var=(username,password,email)
                    mycursor.execute(sql,var)
                    data.commit()
                    messagebox.showinfo(title="Good Job Choy",message="Create Account Successful")
            
                    self.frm_create.destroy()    
        btn_create=Button(master=self.frm_create,text="Create Account",font=("Alkatra",15),bg="#7be1e8",fg="#0347ad",border=0,width=15,activebackground="white",cursor='hand2',command=create_acc)
        btn_create.place(x=110,y=170)
    def sign_in(self):
         self.frm_create.destroy() 