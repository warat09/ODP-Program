from tkinter import *
import csv
import os
try:
    def sayhello():                                 
        block.destroy()
        mywin = Tk()
        mywin.title('Online Dispense Program')
        mywin.geometry('750x300')
        mywin.config(bg='peachpuff')
        
        Head = Label(mywin,bg='Peachpuff',text='Online Dispense Program')
        Head.place(x=310,y=0)
        mywin.resizable(0, 0)    
    #------------------------------------------------#  Scale of window & other features 
        Topic_1 = Label(mywin,bg='Peachpuff',text='ใส่ข้อมูลส่วนตัว')      # ช่องใส่ประวัติส่วนตัว 
        Topic_1.place(x=10,y=20)
        
        global inp_name
        global inp_age
        global inp_weight
        global inp_height
        global inp_location

        name_user = StringVar(mywin)
        age_user = IntVar(mywin)
        height_user = DoubleVar(mywin)
        weight_user = DoubleVar(mywin)
        location_user = StringVar(mywin)

        name = Label(mywin,bg='Peachpuff',text='ชื่อ ')                # input name
        name.place(x=30,y=40)
        try:
            inp_name = Entry(mywin,textvariable = name_user)
            inp_name.place(x=85,y=40)
        except AttributeError:
            print('Error')

        age = StringVar()
        age = Label(mywin,bg='Peachpuff',text='อายุ ')                 # input age
        age.place(x=30,y=70)
        try:
            inp_age = Entry(mywin,textvariable = age_user)
            inp_age.place(x=85,y=70)
        except AttributeError:
            print('Error')
            
        height=StringVar()
        height = Label(mywin,bg='Peachpuff',text='ส่วนสูง ')            # input height
        height.place(x=30,y=100)
        try:
  
            inp_height = Entry(mywin,textvariable = weight_user)
            inp_height.place(x=85,y=100)
        except AttributeError:
            print('Error')

        weight=StringVar()
        weight = Label(mywin,bg='Peachpuff',text='น้ำหนัก ')           # input weight
        weight.place(x=30,y=130)
        try:
            inp_weight = IntVar()
            inp_weight = Entry(mywin,textvariable = height_user)
            inp_weight.place(x=85,y=130)
        except AttributeError:
            print('Error')

        location=StringVar()
        location = Label(mywin,bg='Peachpuff',text='ที่อยู่ ')           # input location
        location.place(x=30,y=160)
        try:
            inp_location = StringVar()
            inp_location = Entry(mywin,textvariable = location_user)
            inp_location.place(x=85,y=160)
        except AttributeError:
            print('Error')


        def inf():  # ค่าที่input ยังไม่link import ไปที่ inf.txt # #'Label' object has no attribute 'get'# 

            filepath = 'inp.txt'
            try:
                name_info = inp_name.get()
                age_info = inp_age.get()
                height_info = inp_height.get()
                weight_info = inp_weight.get()
                location_info = inp_location.get()
            except AttributeError:
                print('Error')

            file = open('inp.txt', "w",encoding='utf-8')
            file.write(name_info + "\n")
            file.write(age_info + "\n")
            file.write(height_info + "\n")
            file.write(weight_info + "\n")
            file.write(location_info + "\n")
            file.close()
              
        #------------------------------------------------#
        bt_inf = Button(mywin,text='ตกลง', bg="blue" , command=inf)
        bt_inf.place(x=20,y=230)

        #------------------------------------------------#

        Topic_2 = Label(mywin,bg='Peachpuff',text='อาการป่วย')  
        Topic_2.place(x=280,y=20)
        
        def alle1():
            filepath='Alle.csv'
            file = open('Alle.csv','a',encoding='utf-8')
            file.write('ไข้/ปวดหัว :'+'\n''Paracetamol 500 MG : ครั้งละ 2 เม็ด / ทุกๆ 4-6 ขม. กินติดต่อจนกว่าจะหาย '+'\n'
                        '/'+'\n')
                
        check1 = StringVar()
        check1 = Button(mywin,bg = 'Peachpuff',
                        text='ไข้/ปวดหัว',
                        command = alle1)
        check1.place(x=250,y=50)

        def alle2():
            filepath='Alle.csv'
            file = open('Alle.csv','a',encoding='utf-8')
            file.write('ไอ /เจ็บคอ/เสมหะ :'+'\n''Kamillosan M : ผ่นครั้งละ 1-2 ที / ทุกครั้งที่มีอาการ'+'\n'
                        'Guafenesin 200 MG : ครั้งละ 1 เม็ด  / วันละ 4 ครั้ง (3 หลังอาหาร 1 ก่อนนอน) กินจะกว่าจะไม่มีอาการ'+'\n'
                        '/'+'\n')
            
        check2 = StringVar()
        check2 = Button(mywin,bg = 'Peachpuff',
                        text= 'ไอ /เจ๊บคอ/เสมหะ',
                        command = alle2)
        check2.place(x=250,y=100)

        def alle3():
            filepath='Alle.csv'
            file = open('Alle.csv','a',encoding='utf-8')
            file.write("คัดจมูก/มีน่้ำมูก :"+'\n''น้ำเกลือ 1 lt : 7 ขวด / ล้างจมูกเช้า-เย็น จนกว่าจะหาย'+'\n'
                       '/'+'\n')

        check3 = StringVar()
        check3 = Button(mywin,bg = 'Peachpuff',
                        text = 'คิดจมูก/มีน้ำมูก/แน่นจมูก',
                        command = alle3)
        check3.place(x=250,y=150)

        def alle4():
            filepath='Alle.csv'
            file = open('Alle.csv','a',encoding='utf-8')
            file.write('ผื่นขึ้น :'+'\n''Topicort : ใช้ทาทุกครั้งที่มีอาการ'+'\n'
                        '/'+'\n')

        check4 = StringVar()
        check4 = Button(mywin,bg = 'Peachpuff',
                        text = 'ผื่นขึ้น',
                        command =alle4)
        check4.place(x=250,y=200)

        def alle5():
            filepath='Alle.csv'
            file = open('Alle.csv','a',encoding='utf-8')
            file.write('อาเจียน :'+'\n''Dimenhydrinate : ครั้งละ 1 เม็ด / หลังอาหาร 3 มื้อ'+'\n'
                        '/'+'\n')

        check5 = StringVar()
        check5 = Button(mywin,bg = 'Peachpuff',
                        text = 'อาเจียน',
                        command = alle5)
        check5.place(x=400,y=50)
            
        def alle6():
            filepath='Alle.csv'
            file = open('Alle.csv','a',encoding='utf-8')
            file.write('หอบ :'+'\n''Ventolin Evohaler 100 mcg : ผ่นทุกครั้งที่มีอาการ'+'\n'
                        '/'+'\n')

        check6 = StringVar()
        check6 = Button(mywin,bg = 'Peachpuff',
                        text = 'หอบ',
                        command = alle6)
        check6.place(x=400,y=100)

        def alle7():
            
            file = open('Alle.csv','a',encoding='utf-8')
            file.write('คันตา/ตาแดง :'+'\n''OPSAR 120 ML : ใช้ล้างตาทุกครั้งที่มีอาการ'+'\n'
                        '/'+'\n')

        check7 = StringVar()
        check7 = Button(mywin,bg = 'Peachpuff',
                        text = 'ตาแดง',
                        command = alle7)
        check7.place(x=400,y=150)

        def pay1():
            filepath='Payment.csv'
            file = open('Payment.csv','w',encoding='utf-8')
            file.write('วิธีการชำระเงิน : Credit Card'+'\n')        
                
        check8 = StringVar()
        check8 = Button(mywin,text='Credit Card',                            
                        command= pay1)
        check8.place(x=300,y=250)
            
        def pay2():
            filepath='Payment.csv'
            file = open('Payment.csv','w',encoding='utf-8')
            file.write('วิธีการชำระเงิน : เก็บเงินปลายทาง'+'\n')
            
        check9 = StringVar()
        check9 = Button(mywin,text='เก็บเงินปลายทาง',
                        command= pay2)
        check9.place(x=380,y=250)

        def bt_next():
            mywin.destroy()
            result = Tk()
            result.title('Result')
            result.geometry('500x300')
            result.config(bg='peachpuff')

            head =Label(result,text='Check Out',bg='peachpuff',font='14')
            head.pack()

            global mysym
            global myinp
            global mypay
         
            filepath='inp.txt'
            with open('inp.txt','r',encoding='utf-8')as ininp:
                ip = csv.reader(ininp)
                myinp = list(ip)

            print(myinp)
            
            filepath='Alle.csv'
            
            with open('Alle.csv','r',encoding='utf-8') as insym:
                rd = csv.reader(insym)
                mysym = list(rd)

            print(mysym)

            filepath='Payment.csv'
            with open('Payment.csv','r',encoding='utf-8') as inpay:
                pm = csv.reader(inpay)
                mypay =list(pm)
                
            print(mypay)

                                  
            text = Label(result,text=myinp,bg='peachpuff',font='14').place(x=50,y=50)    
            text1 = Label(result,text=mysym,bg='peachpuff').place(x=50,y=100)
            text2 = Label(result,text=mypay,bg='peachpuff').place(x=50,y=150)

            
 
            
        Next = Button(mywin,text ='Next',command = bt_next)     
        Next.place(x=500,y=200)

 
    block=Tk()
    block.title('Who Are You?')
    block.minsize(300,200)
    block.resizable(0, 0)
    block.config(bg='peachpuff')

    lb = Label(block,text = 'ยินดีต้อนรับสู่โปรแกรม ODP',bg='peachpuff',font='14')
    lb.pack()

    ask = Label(block,text = 'คุณเป็นใคร?',bg='peachpuff',font='8')
    ask.pack()

    bt = Button(block,text = 'ผู้ป่วย',command=sayhello,width = 20)
    bt.place(x=75,y=80)

    bt2 = Button(block, text = 'ปิด',command = block.destroy,bg='red',width = 10)
    bt2.place(x=180,y=170)
        #------------------------------------------------# หน้าLogin

    def register_user(): #login และ register
    
        username_info = username.get()
        password_info = password.get()
    
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
    
        username_entry.delete(0, END)
        password_entry.delete(0, END)
    
        Label(register_screen, text="Registration Success",bg='Peachpuff', fg="green", font=("calibri", 11)).pack()
        
    def register(): #หน้ากดเข้าไปกรอกข้อมูลสมัครสมาชิก
        global register_screen
        
        register_screen = Toplevel(main)
        register_screen.title("ลงทะเบียน")
        register_screen.config(bg='Peachpuff')
        register_screen.resizable(0, 0)
        register_screen.minsize(300,200)

        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()
        
        Label(register_screen, text="ใส่รหัสของคุณ", bg="red").pack()
        Label(register_screen, bg='Peachpuff',text="").pack()        
            
        username_lable = Label(register_screen,bg='Peachpuff', text="Username * ")
        username_lable.pack()
        
        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()
        
        password_lable = Label(register_screen,bg='Peachpuff', text="Password * ")
        password_lable.pack()
            
        password_entry = Entry(register_screen, textvariable=password, show='●')
        password_entry.pack()
            
        Label(register_screen,bg='Peachpuff', text="").pack()
            
        Button(register_screen, text="Register", width=10, height=1, bg="blue" ,command = register_user).pack()

    def login():
        global Login
        Login = Toplevel(main)
        Login.config(bg='Peachpuff')
        Login.title("เข้าสู่ระบบ")
        Login.geometry("300x250")
    
        global username_verify
        global password_verify
    
        username_verify = StringVar()
        password_verify = StringVar()
    
        global username_En
        global password_En

        Label(Login, text="ใส่รหัสของคุณ",bg='red').pack()
        Label(Login, text="",bg='Peachpuff').pack()
    
        Label(Login, text="Username * ",bg='Peachpuff').pack()
        username_En = Entry(Login, textvariable=username_verify)
        username_En.pack()
        Label(Login, text="",bg='Peachpuff').pack()
        Label(Login, text="Password * ",bg='Peachpuff').pack()
        password_En = Entry(Login, textvariable=password_verify, show= '●')
        password_En.pack()
        Label(Login, text="",bg='Peachpuff').pack()

        Button(Login,text='Login',height='2',width='30',bg='blue',command = login_verify).pack()
        
    def login_sucess():
        global login_success_screen
        login_success_screen = Toplevel(Login)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK",command = readinformation).pack()

    def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_En.delete(0, END)
        password_En.delete(0, END)
    
        list_of_files = os.listdir() #เปิดไฟล์โดยใช้os
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                login_sucess()
    
            else:
                password_not_recognised() 

        else:
            user_not_found()

    def user_not_found():
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(Login)
        password_not_recog_screen.title('ไม่พบข้อมูล')
        password_not_recog_screen.geometry("150x100")
        Label(password_not_recog_screen, text="ขออภัยเราไม่พบข้อมูลในระบบ ").pack()
        Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()    

    '''def delete_login_success():'''
        #รอของผู้ป่วยเสร็จ

    def delete_password_not_recognised(): #ทำลายกล่องเมื่อกด pass ผิด
        password_not_recog_screen.destroy()

    def readinformation(): #ตอนกดokแล้วให้มันprintไปอยู่ในหน้ากล่องinp
        result = Tk()
        result.title('Result')
        result.geometry('500x300')
        result.config(bg='peachpuff')

        head =Label(result,text='Information patient',bg='peachpuff',font='14')
        head.pack()

        global mysym
        global myinp
        global mypay
         
        filepath='inp.txt'
        with open('inp.txt','r',encoding='utf-8')as ininp:
            ip = csv.reader(ininp)
            myinp = list(ip)

        print(myinp)
            
        filepath='Alle.csv'
            
        with open('Alle.csv','r',encoding='utf-8') as insym:
            rd = csv.reader(insym)
            mysym = list(rd)

        print(mysym)

        filepath='Payment.csv'
        with open('Payment.csv','r',encoding='utf-8') as inpay:
            pm = csv.reader(inpay)
            mypay =list(pm)
                
        print(mypay)

                                  
        text = Label(result,text=myinp,bg='peachpuff',font='14').place(x=50,y=50)    
        text1 = Label(result,text=mysym,bg='peachpuff').place(x=50,y=100)
        text2 = Label(result,text=mypay,bg='peachpuff').place(x=50,y=150)
        
                
        
            
    def first_main ():
        global main  
        main= Toplevel()

        main.title("Login")
        main.minsize(300,250)
        main.resizable(0, 0)
        main.config(bg='Peachpuff')

        T6=Label(main,text="คุณมีรหัสผ่านหรือยัง", bg="Peachpuff", width="20", height="2", font=("Calibri", 13)) 
        T6.place(x=60,y=20)

        RegisterButton=Button(main,text="ลงทะเบียน(เฉพาะผู้เกี่ยวข้อง)", height="2", width="30",command=register)
        RegisterButton.place(x=48,y=75)

        LoginButton=Button(main,text="เข้าสู่ระบบ", height="2", width="30",command = login)
        LoginButton.place(x=48,y=155)        

    bt1 = Button(block, text = 'หมอ',command=first_main, width= 20)
    bt1.place(x=75,y=130)

    mainloop()

except Exception:
    print('Error')
