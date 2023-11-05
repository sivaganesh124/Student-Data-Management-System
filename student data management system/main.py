from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class student():
    def __init__(self,root):
        self.root=root
        self.root.title("STUDENT DATA MANAGEMENT SYSTEM")
        self.root.geometry("1530x790+0+0")

        #variables
        self.var_dept = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_acdyr = StringVar()
        self.var_rollno = StringVar()
        self.var_stdname= StringVar()
        self.var_sec = StringVar()
        self.var_aadno = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phnno = StringVar()
        self.var_adrs = StringVar()
        self.var_coord = StringVar()
        self.var_skills = StringVar()
        self.var_proj = StringVar()
        self.var_1yr = StringVar()
        self.var_2yr = StringVar()
        self.var_3yr = StringVar()
        self.var_4yr = StringVar()


        #bg img
        img  = Image.open(r"mini project\3.png")
        img  = img.resize((1560,790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_lbl=Label(self.root,image=self.photoimg,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=0,width=1500,height=700)

        #title
        lbl_title=Label(bg_lbl,text="STUDENT DATA MANAGEMENT SYSTEM",font=("times new roman",37,"bold",),fg="white",bg="black")
        lbl_title.place(x=0,y=0,width=1340,height=50)

        #frame
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=15,y=55,width=1245,height=580)

        #leftframe
        Dataleftframe=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="STUDENT INFORMATION",font=("times new roman",12,"bold"),fg="black",bg="white")
        Dataleftframe.place(x=10,y=3,width=565,height=565)

        #left image 1
        img1 = Image.open(r"mini project\1.jpg")
        img1 = img1.resize((425, 250), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_lbl = Label(Dataleftframe, image=self.photoimg1, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=0, width=550, height=100)

        # current course label frame information
        std_lbl_info_frame=LabelFrame(Dataleftframe, bd=4, relief=RIDGE, padx=2, text="CURRENT INFORMATION",font=("times new roman", 12, "bold"), fg="black", bg="white")
        std_lbl_info_frame.place(x=0, y=100, width=550, height=110)

        #labesls

        #dept
        lbl_dept=Label(std_lbl_info_frame,text="DEPARTMENT",font=("arial",12,"bold"),bg="white")
        lbl_dept.grid(row=0,column=0,sticky=W)

        combo_dep=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dept,font=("arial",11,"bold"),width=14,state="readonly")
        combo_dep["value"]=("Select dept","CSE","AI&DS","IT","ECE","EEE","CIVIL","MECH")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky="W")

        #year
        lbl_year = Label(std_lbl_info_frame, text="YEAR", font=("arial", 12, "bold"), bg="white")
        lbl_year.grid(row=0, column=2, sticky=W)
        combo_year = ttk.Combobox(std_lbl_info_frame, textvariable=self.var_year,font=("arial", 11, "bold"), width=14, state="readonly")
        combo_year["value"] = ("Select year","1","2","3","4")
        combo_year.current(0)
        combo_year.grid(row=0, column=3, padx=2, pady=10, sticky="W")

        #current semester
        lbl_semester = Label(std_lbl_info_frame, text="SEMESTER", font=("arial", 12, "bold"), bg="white")
        lbl_semester.grid(row=2, column=0, sticky=W)
        combo_semester = ttk.Combobox(std_lbl_info_frame,textvariable=self.var_sem, font=("arial", 11, "bold"), width=14, state="readonly")
        combo_semester["value"] = ("Select semester", "1", "2")
        combo_semester.current(0)
        combo_semester.grid(row=2, column=1, padx=2, pady=10, sticky="W")

        # current academic year
        lbl_acdmy = Label(std_lbl_info_frame, text="ACADEMIC YEAR", font=("arial", 12, "bold"), bg="white")
        lbl_acdmy.grid(row=2, column=2, sticky=W, padx=2, pady=2)

        acdmy_entry = ttk.Entry(std_lbl_info_frame, textvariable=self.var_acdyr,font=("arial", 12, "bold"), width=14)
        acdmy_entry.grid(row=2, column=3, sticky=W, padx=2, pady=2)

        # current class frame information
        std_lbl_cls_frame = LabelFrame(Dataleftframe, bd=4, relief=RIDGE, padx=2, text="STUDENT DETAIL INFORMATION",font=("times new roman", 12, "bold"), fg="black", bg="white")
        std_lbl_cls_frame.place(x=0, y=210, width=550, height=280)

        #label entries

        # ROLLNO
        lbl_rno = Label(std_lbl_cls_frame, text="ROLLNO", font=("arial", 12, "bold"), bg="white")
        lbl_rno.grid(row=0, column=0, sticky=W, padx=2, pady=2)

        rno_entry = ttk.Entry(std_lbl_cls_frame, textvariable=self.var_rollno,font=("arial", 12, "bold"), width=14)
        rno_entry.grid(row=0, column=1, sticky=W, padx=2, pady=2)

        #name
        lbl_name = Label(std_lbl_cls_frame, text="STUDENT NAME", font=("arial", 12, "bold"), bg="white")
        lbl_name.grid(row=0, column=2, sticky=W, padx=2, pady=2)

        name_entry = ttk.Entry(std_lbl_cls_frame, textvariable=self.var_stdname,font=("arial", 12, "bold"), width=14)
        name_entry.grid(row=0, column=3, sticky=W, padx=2, pady=2)

        #section
        lbl_sec = Label(std_lbl_cls_frame, text="SECTION", font=("arial", 12, "bold"), bg="white")
        lbl_sec.grid(row=1, column=0, sticky=W, padx=2, pady=2)

        sec_entry = ttk.Entry(std_lbl_cls_frame,textvariable=self.var_sec, font=("arial", 12, "bold"), width=14)
        sec_entry.grid(row=1, column=1, sticky=W, padx=2, pady=2)

        # aadhar number
        lbl_an = Label(std_lbl_cls_frame, text="AADHAR NO", font=("arial", 12, "bold"), bg="white")
        lbl_an.grid(row=1, column=2, sticky=W, padx=2, pady=2)

        id_entry = ttk.Entry(std_lbl_cls_frame, textvariable=self.var_aadno,font=("arial", 12, "bold"), width=14)
        id_entry.grid(row=1, column=3, sticky=W, padx=2, pady=2)

        #GENDER
        lbl_gender = Label(std_lbl_cls_frame, text="GENDER", font=("arial", 12, "bold"), bg="white")
        lbl_gender.grid(row=2, column=0, sticky=W)
        combo_gender = ttk.Combobox(std_lbl_cls_frame, textvariable=self.var_gender,font=("arial", 11, "bold"), width=13, state="readonly")
        combo_gender["value"] = ("Select gender","Male","Female")
        combo_gender.current(0)
        combo_gender.grid(row=2, column=1, padx=2, pady=10, sticky="W")

        #DOB
        lbl_DOB = Label(std_lbl_cls_frame, text="DATE OF BIRTH", font=("arial", 12, "bold"), bg="white")
        lbl_DOB.grid(row=2, column=2, sticky=W, padx=2, pady=2)

        DOB_entry = ttk.Entry(std_lbl_cls_frame, textvariable=self.var_dob,font=("arial", 12, "bold"), width=14)
        DOB_entry.grid(row=2, column=3, sticky=W, padx=2, pady=2)

        #EMAIL
        lbl_em = Label(std_lbl_cls_frame, text="EMAIL", font=("arial", 12, "bold"), bg="white")
        lbl_em.grid(row=3, column=0, sticky=W, padx=2, pady=2)

        em_entry = ttk.Entry(std_lbl_cls_frame,textvariable=self.var_email, font=("arial", 12, "bold"), width=14)
        em_entry.grid(row=3, column=1, sticky=W, padx=2, pady=2)

        #PHONE NUMBER
        lbl_phn = Label(std_lbl_cls_frame, text="PHONE NUMBER", font=("arial", 12, "bold"), bg="white")
        lbl_phn.grid(row=3, column=2, sticky=W, padx=2, pady=2)

        phn_entry = ttk.Entry(std_lbl_cls_frame, textvariable=self.var_phnno,font=("arial", 12, "bold"), width=14)
        phn_entry.grid(row=3, column=3, sticky=W, padx=2, pady=2)

        #ADDRESS
        lbl_add = Label(std_lbl_cls_frame, text="ADDRESS", font=("arial", 12, "bold"), bg="white")
        lbl_add.grid(row=4, column=0, sticky=W, padx=2, pady=2)

        add_entry = ttk.Entry(std_lbl_cls_frame,textvariable=self.var_adrs, font=("arial", 12, "bold"), width=14)
        add_entry.grid(row=4, column=1, sticky=W, padx=2, pady=2)

        #class coordinator
        lbl_cc = Label(std_lbl_cls_frame, text="COORDINATOR", font=("arial", 12, "bold"), bg="white")
        lbl_cc.grid(row=4, column=2, sticky=W, padx=2, pady=2)
        #
        cc_entry = ttk.Entry(std_lbl_cls_frame, textvariable=self.var_coord,font=("arial", 12, "bold"), width=14)
        cc_entry.grid(row=4, column=3, sticky=W, padx=2, pady=2)

        #skills learned
        lbl_skl = Label(std_lbl_cls_frame, text="SKILLS", font=("arial", 12, "bold"), bg="white")
        lbl_skl.grid(row=5, column=0, sticky=W, padx=2, pady=2)

        skl_entry = ttk.Entry(std_lbl_cls_frame,textvariable=self.var_skills, font=("arial", 12, "bold"), width=14)
        skl_entry.grid(row=5, column=1, sticky=W, padx=2, pady=2)

        #PROJECTS DONE
        lbl_pro = Label(std_lbl_cls_frame, text="PROJECTS", font=("arial", 12, "bold"), bg="white")
        lbl_pro.grid(row=5, column=2, sticky=W, padx=2, pady=2)

        pro_entry = ttk.Entry(std_lbl_cls_frame, textvariable=self.var_proj,font=("arial", 12, "bold"), width=14)
        pro_entry.grid(row=5, column=3, sticky=W, padx=2, pady=2)

        #1 score
        lbl_one1 = Label(std_lbl_cls_frame, text="1YR CGPA", font=("arial", 12, "bold"), bg="white")
        lbl_one1.grid(row=6, column=0, sticky=W, padx=2, pady=2)

        one1_entry = ttk.Entry(std_lbl_cls_frame,textvariable=self.var_1yr, font=("arial", 12, "bold"), width=14)
        one1_entry.grid(row=6, column=1, sticky=W, padx=2, pady=2)

        #2 score
        lbl_one2 = Label(std_lbl_cls_frame, text="2YR CGPA", font=("arial", 12, "bold"), bg="white")
        lbl_one2.grid(row=6, column=2, sticky=W, padx=2, pady=2)

        one2_entry = ttk.Entry(std_lbl_cls_frame,textvariable=self.var_2yr, font=("arial", 12, "bold"), width=14)
        one2_entry.grid(row=6, column=3, sticky=W, padx=2, pady=2)

        #3 SCORE
        lbl_one3 = Label(std_lbl_cls_frame, text="3YR CGPA", font=("arial", 12, "bold"), bg="white")
        lbl_one3.grid(row=7, column=0, sticky=W, padx=2, pady=2)

        one3_entry = ttk.Entry(std_lbl_cls_frame, textvariable=self.var_3yr,font=("arial", 12, "bold"), width=14)
        one3_entry.grid(row=7, column=1, sticky=W, padx=2, pady=2)

        # 4 SCORE
        lbl_one4 = Label(std_lbl_cls_frame, text="4YR CGPA", font=("arial", 12, "bold"), bg="white")
        lbl_one4.grid(row=7, column=2, sticky=W, padx=2, pady=2)

        one4_entry = ttk.Entry(std_lbl_cls_frame, textvariable=self.var_4yr,font=("arial", 12, "bold"), width=14)
        one4_entry.grid(row=7, column=3, sticky=W, padx=2, pady=2)

        #button frame
        button_frame = Frame(Dataleftframe, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=0, y=492, width=550, height=43)

        btn_add=Button(button_frame,text="SAVE",command=self.add_data,font=("arial", 13, "bold"),width=12,bg="grey",fg="black")
        btn_add.grid(row=0,column=0,padx=1)

        btn_update = Button(button_frame, text="UPDATE", command=self.update_data,font=("arial", 13, "bold"), width=12, bg="grey", fg="black")
        btn_update.grid(row=0, column=1, padx=1)

        btn_del = Button(button_frame, text="DELETE", command=self.delete_data,font=("arial",13, "bold"), width=12, bg="grey", fg="black")
        btn_del.grid(row=0, column=2, padx=1)

        btn_res = Button(button_frame, text="RESET",command=self.reset_data, font=("arial", 13, "bold"), width=12, bg="grey", fg="black")
        btn_res.grid(row=0, column=3, padx=1)

        #rightframe
        Datarightframe = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="STUDENT DETAILS",font=("times new roman", 12, "bold"), fg="black", bg="white")
        Datarightframe.place(x=580, y=3, width=650, height=565)
        # right frame img
        img2 = Image.open(r"mini project\11.png")
        img2 = img2.resize((450, 250), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_lbl = Label(Datarightframe, image=self.photoimg2, bd=2, relief=RIDGE)
        bg_lbl.place(x=2, y=0, width=630, height=150)

        # search frame
        Datasearchframe = LabelFrame(Datarightframe, bd=4, relief=RIDGE, padx=2, text="STUDENT DATA",font=("times new roman", 12, "bold"), fg="black", bg="white")
        Datasearchframe.place(x=0, y=150, width=630, height=65)

        # search by
        lbl_search = Label(Datasearchframe, text="SEARCH BY:", font=("arial", 12, "bold"), bg="white")
        lbl_search.grid(row=0, column=0, sticky=W, padx=2, pady=2)

        self.var_com_search=StringVar()
        combo_search = ttk.Combobox(Datasearchframe, textvariable=self.var_com_search,font=("arial", 10, "bold"), width=15, state="readonly")
        combo_search["value"] = ("Select option", "RLNO", "PHNO")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2, pady=10, sticky="W")

        self.var_search=StringVar()
        search_entry = ttk.Entry(Datasearchframe, textvariable=self.var_search,font=("arial", 10, "bold"), width=18)
        search_entry.grid(row=0, column=2, sticky=W, padx=2, pady=2)

        btn_search = Button(Datasearchframe, command=self.search_data,text="SEARCH", font=("arial", 11, "bold"), width=12, bg="grey", fg="black")
        btn_search.grid(row=0, column=3,padx=1)

        btn_showall = Button(Datasearchframe, command=self.fetch_data,text="SHOW ALL", font=("arial", 11, "bold"), width=12, bg="grey", fg="black")
        btn_showall.grid(row=0, column=4, padx=1)

        #************************* DATA SCROLL BAR **********************#
        t_frame=Frame(Datarightframe,bd=4,relief=RIDGE)
        t_frame.place(x=0,y=216,width=630,height=320)

        scroll_barx=ttk.Scrollbar(t_frame,orient=HORIZONTAL)
        scroll_bary=ttk.Scrollbar(t_frame,orient=VERTICAL)
        self.student_datatable= ttk.Treeview(t_frame,columns=("dept","year","semester","academic year","rollno","stdname","sec","aadno","gender","dob","email","phnno","adrs","coordinator","skills","proj","1yr","2yr","3yr","4yr",),xscrollcommand=scroll_barx.set,yscrollcommand=scroll_bary.set)

        scroll_barx.pack(side=BOTTOM,fill=X)
        scroll_bary.pack(side=RIGHT,fill=Y)

        scroll_barx.config(command=self.student_datatable.xview)
        scroll_bary.config(command=self.student_datatable.yview)

        self.student_datatable.heading("dept",text="DEPARTMENT")
        self.student_datatable.heading("year", text="YEAR")
        self.student_datatable.heading("semester", text="SEMESTER")
        self.student_datatable.heading("academic year", text="ACADEMIC YEAR")
        self.student_datatable.heading("rollno", text="ROLLNO")
        self.student_datatable.heading("stdname", text="STUDENT NAME")
        self.student_datatable.heading("sec", text="SECTION")
        self.student_datatable.heading("aadno", text="AADHAR NO")
        self.student_datatable.heading("gender", text="GENDER")
        self.student_datatable.heading("dob", text="DATE OF BIRTH")
        self.student_datatable.heading("email", text="EMAIL")
        self.student_datatable.heading("phnno", text="PHONE NUMBER")
        self.student_datatable.heading("adrs", text="ADDRESS")
        self.student_datatable.heading("coordinator", text="COORDINATOR")
        self.student_datatable.heading("skills", text="SKILLS")
        self.student_datatable.heading("proj", text="PROJECTS")
        self.student_datatable.heading("1yr", text="1YR CGPA")
        self.student_datatable.heading("2yr", text="2YR CGPA")
        self.student_datatable.heading("3yr", text="3YR CGPA")
        self.student_datatable.heading("4yr", text="4YR CGPA")


        self.student_datatable["show"]="headings"

        self.student_datatable.column("dept",width=200)
        self.student_datatable.column("year", width=200)
        self.student_datatable.column("semester", width=200)
        self.student_datatable.column("academic year", width=200)
        self.student_datatable.column("rollno", width=200)
        self.student_datatable.column("stdname", width=200)
        self.student_datatable.column("sec", width=200)
        self.student_datatable.column("aadno", width=200)
        self.student_datatable.column("gender", width=200)
        self.student_datatable.column("dob", width=200)
        self.student_datatable.column("email", width=200)
        self.student_datatable.column("phnno", width=200)
        self.student_datatable.column("adrs", width=200)
        self.student_datatable.column("coordinator", width=200)
        self.student_datatable.column("skills", width=200)
        self.student_datatable.column("proj", width=200)
        self.student_datatable.column("1yr", width=200)
        self.student_datatable.column("2yr", width=200)
        self.student_datatable.column("3yr", width=200)
        self.student_datatable.column("4yr", width=200)

        self.student_datatable.pack(fill=BOTH,expand=1)
        self.student_datatable.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()




    def add_data(self):
        if (self.var_dept.get()=="" or self.var_email.get()=="" or self.var_rollno.get()==""):
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Siva@1234",database="sivaganesh")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                               self.var_dept.get(),
                                                                                                                               self.var_year.get(),
                                                                                                                               self.var_sem.get(),
                                                                                                                               self.var_acdyr.get(),
                                                                                                                               self.var_rollno.get(),
                                                                                                                               self.var_stdname.get(),
                                                                                                                               self.var_sec.get(),
                                                                                                                               self.var_aadno.get(),
                                                                                                                               self.var_gender.get(),
                                                                                                                               self.var_dob.get(),
                                                                                                                               self.var_email.get(),
                                                                                                                               self.var_phnno.get(),
                                                                                                                               self.var_adrs.get(),
                                                                                                                               self.var_coord.get(),
                                                                                                                               self.var_skills.get(),
                                                                                                                               self.var_proj.get(),
                                                                                                                               self.var_1yr.get(),
                                                                                                                               self.var_2yr.get(),
                                                                                                                               self.var_3yr.get(),
                                                                                                                               self.var_4yr.get()
                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student data has been added!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    #fetch function
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Siva@1234", database="sivaganesh")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student ")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_datatable.delete(*self.student_datatable.get_children())
            for i in data:
                self.student_datatable.insert("",END,values=i)
            conn.commit()
        conn.close()
    # get cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_datatable.focus()
        content=self.student_datatable.item(cursor_row)
        data=content["values"]

        self.var_dept.set(data[0])
        self.var_year.set(data[1])
        self.var_sem.set(data[2])
        self.var_acdyr.set(data[3])
        self.var_rollno.set(data[4])
        self.var_stdname.set(data[5])
        self.var_sec.set(data[6])
        self.var_aadno.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phnno.set(data[11])
        self.var_adrs.set(data[12])
        self.var_coord.set(data[13])
        self.var_skills.set(data[14])
        self.var_proj.set(data[15])
        self.var_1yr.set(data[16])
        self.var_2yr.set(data[17])
        self.var_3yr.set(data[18])
        self.var_4yr.set(data[19])

    def update_data(self):
        if (self.var_dept.get() == "" or self.var_email.get() == "" or self.var_rollno.get() == ""):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                update = messagebox.askyesno("Update", "Are you sure you want to update the student data",
                                             parent=self.root)
                if update:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Siva@1234",
                                                   database="sivaganesh")
                    my_cursor = conn.cursor()

                    # Use proper formatting in your SQL query
                    sql_query = """UPDATE student SET DEPT=%s, YEAR=%s, SEM=%s, `ACD YR`=%s, STDNAME=%s, SEC=%s, AADNO=%s, 
                                   GEND=%s, DOB=%s, EMAIL=%s, PHNO=%s, ADRS=%s, COORD=%s, SKILLS=%s, PROJ=%s, `1yr`=%s, 
                                   `2yr`=%s, `3yr`=%s, `4yr`=%s WHERE RLNO=%s"""

                    data = (
                        self.var_dept.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_acdyr.get(),
                        self.var_stdname.get(),
                        self.var_sec.get(),
                        self.var_aadno.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phnno.get(),
                        self.var_adrs.get(),
                        self.var_coord.get(),
                        self.var_skills.get(),
                        self.var_proj.get(),
                        self.var_1yr.get(),
                        self.var_2yr.get(),
                        self.var_3yr.get(),
                        self.var_4yr.get(),
                        self.var_rollno.get()
                    )

                    my_cursor.execute(sql_query, data)
                    conn.commit()
                    conn.close()

                    self.fetch_data()
                    messagebox.showinfo("Success", "Student successfully updated", parent=self.root)
                else:
                    if not update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_rollno.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure to delete this student data",parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Siva@1234",database="sivaganesh")
                    my_cursor = conn.cursor()
                    sql="delete from student where RLNO=%s"
                    value=(self.var_rollno.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your student has been deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    #reset
    def reset_data(self):
        self.var_dept.set("Select dept")
        self.var_year.set("Select year")
        self.var_sem.set("Select semester")
        self.var_acdyr.set("")
        self.var_rollno.set("")
        self.var_stdname.set("")
        self.var_sec.set("")
        self.var_aadno.set("")
        self.var_gender.set("Select gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phnno.set("")
        self.var_adrs.set("")
        self.var_coord.set("")
        self.var_skills.set("")
        self.var_proj.set("")
        self.var_1yr.set("")
        self.var_2yr.set("")
        self.var_3yr.set("")
        self.var_4yr.set("")
    #search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Siva@1234",database="sivaganesh")
                my_cursor = conn.cursor()
                my_cursor.execute(" select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_datatable.delete(*self.student_datatable.get_children())
                    for i in data:
                        self.student_datatable.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)









root=Tk()
obj=student(root)
root.mainloop()


