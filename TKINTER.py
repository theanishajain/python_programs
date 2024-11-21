from tkinter import *
import datetime
clock = Tk()
clock.title('       **Digital Clock**       ')
clock.geometry('1000x500')
clock.config(bg='RosyBrown2')
def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_ampm.config(text=am)
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    lab_hr.after(200,date_time)#after function recall programs to change the time continously
#setting the hour

lab_heading = Label(clock,text='Digital Clock',font=('Time New Roman', 10 ,'bold'),bg='#D8BFD8' ,fg='white')
lab_heading.place(x=400,y=10,height=20,width=200)
                    
    
#************DATE*********************
lab_hr=Label(clock,text='00', font=('Time New Roman',60,'bold'),bg='#8B7765',fg="black")
lab_hr.place(x=120,y=45,height=110,width=100)
lab_hr_txt=Label(clock,text='Hour', font=('Time New Roman',20,'bold'),bg='#8B7765',fg="black")
lab_hr_txt.place(x=120,y=195,height=30,width=100)


#setting Minutes Label box
lab_min=Label(clock,text='00', font=('Time New Roman',60,'bold'),bg='#8B7765',fg="black")
lab_min.place(x=340,y=45,height=110,width=100)
lab_min_txt=Label(clock,text='Min', font=('Time New Roman',20,'bold'),bg='#8B7765',fg="black")
lab_min_txt.place(x=340,y=195,height=30,width=100)

#setting the seconds
lab_sec=Label(clock,text='00', font=('Time New Roman',60,'bold'),bg='#8B7765',fg="black")
lab_sec.place(x=560,y=45,height=110,width=100)
lab_sec_txt=Label(clock,text='Sec', font=('Time New Roman',20,'bold'),bg='#8B7765',fg="black")
lab_sec_txt.place(x=560,y=195,height=30,width=100)#40 + 110 + 45 = 195


#setting the minutes
lab_ampm=Label(clock,text='00', font=('Time New Roman',45,'bold'),bg='#8B7765',fg="black")
lab_ampm.place(x=780,y=45,height=110,width=100)
lab_ampm_txt=Label(clock,text='Am/Pm', font=('Time New Roman',20,'bold'),bg='#8B7765',fg="black")
lab_ampm_txt.place(x=780,y=195,height=30,width=100)

#*******************TIME*******************
lab_date=Label(clock,text='00', font=('Time New Roman',60,'bold'),bg='#8B7765',fg="black")
lab_date.place(x=120,y=270,height=110,width=100)
lab_date_txt=Label(clock,text='Date', font=('Time New Roman',20,'bold'),bg='#8B7765',fg="black")
lab_date_txt.place(x=120,y=415,height=30,width=100)

#MONTH
lab_mo=Label(clock,text='00', font=('Time New Roman',60,'bold'),bg='#8B7765',fg="black")
lab_mo.place(x=340,y=270,height=110,width=100)
lab_mo_txt=Label(clock,text='Month', font=('Time New Roman',20,'bold'),bg='#8B7765',fg="black")
lab_mo_txt.place(x=340,y=415,height=30,width=100)


#setting up year
lab_year=Label(clock,text='00', font=('Time New Roman',60,'bold'),bg='#8B7765',fg="black")
lab_year.place(x=560,y=270,height=110,width=100)
lab_year_txt=Label(clock,text='Year', font=('Time New Roman',20,'bold'),bg='#8B7765',fg="black")
lab_year_txt.place(x=560,y=415,height=30,width=100)#40 + 110 + 45 = 195

#setting up the day
lab_day=Label(clock,text='00', font=('Time New Roman',35,'bold'),bg='#8B7765',fg="black")
lab_day.place(x=780,y=270,height=110,width=100)
lab_day_txt=Label(clock,text='Day', font=('Time New Roman',20,'bold'),bg='#8B7765',fg="black")
lab_day_txt.place(x=780,y=415,height=30,width=100)

















date_time()
clock.mainloop()

