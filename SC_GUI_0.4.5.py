#   IMPORT: #
import tkinter.font
from tkinter import *
from tkinter import ttk
import sqlite3


#   MainW.Start   ###################################################################################################################################

#Define MainW:
MainW = Tk()
MainW.title("SC-Gui-V.5")
MainW.resizable(0,0)

#Figure out screen size:
Screen_Width = MainW.winfo_screenwidth()
Screen_Height = MainW.winfo_screenheight()

#Use Manual or Scale (ScaleBoth or set Width and Height sepered) Set all not used to "0" To ensure programms to runs right:

#Manual Size:
App_W = 0 #Pixels
App_H = 0 #Pixels

#Auto Size Scale selection:
Scale_Both = 55 #%
Scale_W = 0 #%
Scale_H = 0 #%

#IF/ELSE: Selects manual or auto scale and auto center window by its size:
if App_W > 0 :
    _W = App_W
    _H = App_H
    #Position Calc:
    _X = int((Screen_Width / 2)-(_W / 2))
    _Y = int((Screen_Height / 2)-(_H / 2))
    #Input MainW Size and postition:
    MainW.geometry(f"{_W}x{_H}+{_X}+{_Y}")
else:
    if Scale_Both > 0:
        App_Auto_W = Scale_Both
        App_Auto_H = Scale_Both
        #Scale Calc:
        _W = int(Screen_Width / 100 * App_Auto_W) 
        _H = int(Screen_Height / 100 * App_Auto_H)
        #Position Calc:
        _X = int((Screen_Width / 2)-(_W / 2))
        _Y = int((Screen_Height / 2)-(_H / 2))
        #Input MainW Size and postition:
        MainW.geometry(f"{_W}x{_H}+{_X}+{_Y}")
    else:
        App_Auto_W = Scale_W
        App_Auto_H = Scale_H
        #Scale Calc:
        _W = int(Screen_Width / 100 * App_Auto_W) 
        _H = int(Screen_Height / 100 * App_Auto_H)
        #Position Calc:
        _X = int((Screen_Width / 2)-(_W / 2))
        _Y = int((Screen_Height / 2)-(_H / 2))
        #Input MainW Size and postition:
        MainW.geometry(f"{_W}x{_H}+{_X}+{_Y}")

#   MainW.END   ###################################################################################################################################

#   App_Interface(GUI/Class).Start   ###################################################################################################################################

class App:
    def __init__(self, master):
        self.master = master

    def login(self):
        #Login_Frame
        self.Login_Frame = Frame(self.master)
        self.Login_Frame.pack(pady=(int(_H/2),50))

        #Labels:
        Label_Username = Label(self.Login_Frame, text="Username:",font=("Arial","16"))
        Label_Username.grid(row=1, column=0, padx=5, pady=3)
        Label_Password = Label(self.Login_Frame, text="Password:",font=("Arial","16"))
        Label_Password.grid(row=2, column=0, padx=5, pady=3)

        #Entry:
        self.Entry_Username = Entry(self.Login_Frame,font="Arial,12",)
        self.Entry_Username.grid(row=1, column=1, ipady=5,pady=5)
        self.Entry_Password = Entry(self.Login_Frame,font="Arial,12", show="*")
        self.Entry_Password.grid(row=2, column=1, ipady=5,pady=5)

        #Buttons:
        Login_Button = Button(self.Login_Frame, text="Login",font="Arial,12")
        Login_Button.bind("<Button-1>",self.menubar)
        Login_Button.bind("<Return>", self.menubar)
        Login_Button.grid(row=1, column=2, padx=10,ipadx=5)
        Close_Button = Button(self.Login_Frame, text="Close",font="Arial,12")
        Close_Button.bind("<Button-1>", self.Close_MainW)
        Close_Button.bind("<Return>", self.Close_MainW)
        Close_Button.grid(row=2, column=2, padx=10,ipadx=5)
        
    def menubar(self,event):
        self.Login_Frame.pack_forget()
        menubar= Menu(self.master)
        self.master.config(menu=menubar)
        #Cargo_Menu:
        #Date:
        self.Date_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Date", menu=self.Date_menu)
        self.Date_menu.add_command(label="Open Date",command=self.Open_Date, font=("Arial","12"))
        self.Date_menu.add_command(label="New Date",command=self.New_Date, font=("Arial","12"))
        self.Date_menu.add_command(label="Edit Date",command=self.Edit_Date, font=("Arial","12"))
        self.Date_menu.add_command(label="Remove Date",command=self.Remove_Date, font=("Arial","12"))
        #Separato_Date:
        self.Date_menu.add_separator()
        #Exit/Logout:
        self.Date_menu.add_command(label="Logout",command=self.Return_To_Loggin, font=("Arial","12"))
        self.Date_menu.add_command(label="Close",command=MainW.quit, font=("Arial","12"))
        #Cargo:
        cargo_menu = Menu(menubar,tearoff=0)
        cargo_menu.add_command(label="Open Cargo",command=self.Test, font=("Arial","12"))
        cargo_menu.add_command(label="New Cargo",command=self.Test, font=("Arial","12"))
        cargo_menu.add_command(label="Edit Cargo",command=self.Test, font=("Arial","12"))
        cargo_menu.add_command(label="Remove Cargo",command=self.Test, font=("Arial","12"))
        menubar.add_cascade(label="Cargo", menu=cargo_menu)
        #Supplier:
        Supplier_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Suppliers", menu=Supplier_menu)
        Supplier_menu.add_command(label="Open Supplier",command=self.Test, font=("Arial","12"))        
        Supplier_menu.add_command(label="New Supplier",command=self.Test, font=("Arial","12"))
        Supplier_menu.add_command(label="Edit Supplier",command=self.Test, font=("Arial","12"))
        Supplier_menu.add_command(label="Remove Supplier",command=self.Test, font=("Arial","12"))

    def Open_Date(self):
        self.Enable_Menubar_Buttons()
        self.Hide_Frames()
        #Disable Open_Date Button
        self.Date_menu.entryconfig("Open Date", state="disabled")
        #Tree_Frame:
        self.tree_frame = Frame(self.master,bg="#e0e0e0")
        self.tree_frame.pack(pady=0,padx=0,fill="both",expand=1)
        #Tree_Scroll_Bar:
        self.Tree_Scroll = Scrollbar(self.tree_frame)
        self.Tree_Scroll.pack(side=RIGHT, fill=Y )
        #Tree_Style/Define Tree:
        self.style = ttk.Style()
        #Pick Theme:
        self.style.theme_use("clam")
        #Conf_Style:
        self.style.configure("Treeview",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="silver"        
            )
        self.style.map("Treeview",
            background =[("selected", "#006782")])
        Data_Tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.Tree_Scroll.set, height=int(_H/2))
        #Conf The ScrollBar:
        self.Tree_Scroll.config(command=Data_Tree.yview)
        #Define Columns:
        Data_Tree["columns"] = ("Date","Time", "Deliver", "Goods", "Unloader", "Ordernumber", "Pallet Total", "Phycial Pallets", "Ramp Number")
        #Format Our Columns;
        Data_Tree.column("#0", width=0, stretch=NO)
        Data_Tree.column("Date", anchor=W, width=35)
        Data_Tree.column("Time", anchor=W, width=25)
        Data_Tree.column("Deliver", anchor=W, width=90)
        Data_Tree.column("Goods", anchor=W, width=200)
        Data_Tree.column("Unloader", anchor=CENTER, width=45)
        Data_Tree.column("Ordernumber",anchor=W, width=65)
        Data_Tree.column("Pallet Total", anchor=CENTER, width=60)
        Data_Tree.column("Phycial Pallets",anchor=CENTER, width=60)
        Data_Tree.column("Ramp Number",anchor=CENTER, width=35)
        #Hedings:
        Data_Tree.heading("#0",text="", anchor=W)
        Data_Tree.heading("Date",text="Date", anchor=W)
        Data_Tree.heading("Time",text="Time", anchor=W)
        Data_Tree.heading("Deliver",text="Truck Comppany", anchor=W)
        Data_Tree.heading("Goods",text="Goods", anchor=W)
        Data_Tree.heading("Unloader",text="Unloader", anchor=CENTER)
        Data_Tree.heading("Ordernumber",text="Ordernumber", anchor=W)
        Data_Tree.heading("Pallet Total",text="Pallet Total", anchor=CENTER)
        Data_Tree.heading("Phycial Pallets",text="Phycial Pallets", anchor=CENTER)
        Data_Tree.heading("Ramp Number",text="Ramp Number", anchor=W)
        #Example Data:
        data = [
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],       
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],    
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"],
            ["7.10.2020","2:21", "Posti", "Metsä Tissue Corp", "Driver", 7896541, 66, 33, "E40"],
            ["7.10.2020","2:25", "Kaukokiito", "Nestle, Fatzer, Best friend", "Driver", 7896541, 66, 33, "E32"],
            ["7.10.2020","3:21", "DB Schenker", "AMO", "We", 7896541, 66, 33, "E25"],
            ["7.10.2020","4:45", "Ferroline", "APChemicals", "We", 7896541, 66, 33, "E8"],
            ["7.10.2020","22:21", "Ahola Transport", "Orthex Sweden", "We", 7896541, 66, 33, "E22"],
            ["7.10.2020","12:21", "Post nord", "Kärcher", "Driver", 7896541, 66, 33, "E17"],
            ["7.10.2020","7:21", "Alpi Eesti", "TukkuNet", "We", 7896541, 66, 33, "E12"]
        ]
        #Striped row tags:
        Data_Tree.tag_configure("oddrow", background="white")
        Data_Tree.tag_configure("evenrow", background="#ccf4ff")
        #Input Data:
        count=0

        for record in data:
            if count % 2 == 0:
                Data_Tree.insert(parent="", index="end", iid=count, text="",
                values=(record[0],
                record[1],
                record[2],
                record[3],
                record[4],
                record[5],
                record[6],
                record[7],
                record[8]),
                tags=("evenrow"),)
                count += 1
            else:
                Data_Tree.insert(parent="", index="end", iid=count, text="",
                values=(record[0],
                record[1],
                record[2],
                record[3],
                record[4],
                record[5],
                record[6],
                record[7],
                record[8]),
                tags=("oddrow"),)
                count += 1
        #Open_Data_Under_Menu:
        self.ODUM_Frame = Frame(self.tree_frame, bg="", height=28)
        self.ODUM_Frame.pack(pady=(5,0),padx=5,fill="x", expand=0)
        self.Select_Date_B = Button(self.ODUM_Frame, text="Select Date", command=self.Call_Date)
        self.Select_Date_B.grid(row=0,column=0, padx=(5,0), pady=4)

        #pack.tree
        Data_Tree.pack(pady=5,padx=5,expand=0, fill="x")

    def New_Date(self):
        self.Enable_Menubar_Buttons()
        self.Hide_Frames()
        #Disable New_Date Button
        self.Date_menu.entryconfig("New Date", state="disabled")
        #New_Date_Frame:
        self.New_Date_F = Frame(self.master,bg="green")
        self.New_Date_F.pack(pady=5,padx=5,fill="both",expand=1)
    
    def Enable_Menubar_Buttons(self):
        self.Date_menu.entryconfig("Open Date", state="normal")
        self.Date_menu.entryconfig("New Date", state="normal")
        self.Date_menu.entryconfig("Edit Date", state="normal")
        self.Date_menu.entryconfig("Remove Date", state="normal")

    def Edit_Date(self):
        self.Enable_Menubar_Buttons()
        self.Hide_Frames()
        #Disable Edit_Date Button
        self.Date_menu.entryconfig("Edit Date", state="disabled")
        #Edit_Date_Frame:
        self.Edit_Date_F = Frame(self.master,bg="blue")
        self.Edit_Date_F.pack(pady=5,padx=5,fill="both",expand=1)

    def Remove_Date(self):
        self.Enable_Menubar_Buttons()
        self.Hide_Frames()
        #Disable Remove_Date Button
        self.Date_menu.entryconfig("Remove Date", state="disabled")
        #Remove_Date_Frame:
        self.Remove_Date_F = Frame(self.master,bg="red")
        self.Remove_Date_F.pack(pady=5,padx=5,fill="both",expand=1)

    def Call_Date(self):
        self.Select_Date_B.config(state="disabled")
        Call_W = int(_X)
        Call_H = int(_Y)
        self.Call_Win =Toplevel(self.master)
        self.Call_Win.title("Pick a date")
        self.Call_Win.geometry(f"350x350+{Call_W}+{Call_H}")

    def Test(self): #This IS Empty Function to help write code with function connection allready on it.
        pass
 
    def Hide_Frames(self):
        #Remove_Date_F_Forget:
        try:
            self.Remove_Date_F.pack_forget()
        except AttributeError:
            pass
        #New_Date_F_Forget:
        try:
            self.Edit_Date_F.pack_forget()
        except AttributeError:
            pass
        #Edit_Date_F_Forget:
        try:
            self.New_Date_F.pack_forget()
        except AttributeError:
            pass
        #New_Login_F_Forget:
        try:
            self.Login_Frame.pack_forget()
        except AttributeError:
            pass
        #New_tree_f_Forget:
        try:
            self.tree_frame.pack_forget()
        except AttributeError:
            pass        
        #New_Call_Win_destroy:
        try:
            self.Call_Win.destroy()
        except AttributeError:
            pass


    def Return_To_Loggin(self):
        self.Entry_Username.delete(first=0,last=22)
        self.Entry_Password.delete(first=0,last=22)
        self.Hide_Frames()
        self.remove_menubar()
        self.Login_Frame.pack(pady=(int(_H/2),50))
           
    def remove_menubar(self):
        emptyMenu = Menu(self.master)
        self.master.config(menu=emptyMenu)    

    def Close_MainW(self,event):
        MainW.quit()

def SQLite(): # Gen_DataBase: Cargo_Data + User_Data (Table's)
    conn = sqlite3.connect("Cargo_Data_v2.db")

    #Create Cursor:
    C = conn.cursor()

    #Create Table: (Cargo_Data)
    C.execute("""CREATE TABLE Cargo_Data (
            Date text,
            A_Time text,
            Deliver text,
            Unloader text,
            Goods text,
            Ordernumber integer,
            Pallet Total integer,
            Phycial Pallets integer,                
            Ramp Number text)
            """)

    #Commit Changes:
    conn.commit()

    #Close Connection:
    conn.close()


App = App(MainW).login()


#Loop fro MainW:
MainW.mainloop()

