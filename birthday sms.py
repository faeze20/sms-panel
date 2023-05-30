from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import ghasedakpack
import datetime
def send_sms():
    # create api key
        sms = ghasedakpack.Ghasedak("39a79a573ba0e90ee353b76acb178b8d33ee0626ed96cd7cb9ec984cf2612ac6")
        date_today=datetime.date.today()
        # create formate date
        date_today = str(int(date_today.strftime("%d")))+"/"+str(int(date_today.strftime("%m")))+"/"+date_today.strftime("%Y")

        date_user=edate.get()
        if date_user==date_today:
            
            sms.send({ 'message':etext.get(),  'receptor' :eadress.get() })
            # زمان‌بندی فراخوانی تابع send_sms() هر یک دقیقه
        window.after(60000, send_sms)    

window=Tk()
window.configure(bg="green")
window.geometry("500x600")
window.title("sms panel")
window.resizable(width=False,height=False)
Label(window,text="Sms Panel", fg="black",bg="yellow",cursor="arrow",width=71,height=2).place(x='5',y='1')
adress=Label(window,bg="green" ,text="  number phone    :  ")
adress.place(x='80',y='100')
eadress=Entry(window)
eadress.place(x='200',y='100')

text=Label(window,bg="green",text=" Enter your Message :  ")
text.place(x='80',y='180')
etext=Entry(window)
etext.place(x='200',y='180')

text=Label(window,text=" Enter your date :  ",bg="green")
text.place(x='80',y='260')
edate = DateEntry(window)
edate.place(x='200',y='260')

Button(window,text="send",command=send_sms,width=5,height=2).place(x='240',y='350')
window.after(60000, send_sms)  # زمان‌بندی اولیه فراخوانی تابع send_sms() هر یک دقی
window.mainloop()