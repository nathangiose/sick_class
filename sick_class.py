# Import everything from tkinter
# And import information for the messagebox from tkinter


from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("600x500")
window.title("Sick Class")
window.config(bg='#22e3e3')
frame = Frame(window)
# Sick Class


MSickID = Label(window, bg='#4ce322', fg='black', text="SicknessCode")
MSickID.pack(side=LEFT)
MSickID.place(x=20, y=20)

sick_entry=Entry(window, bd=1, bg='#4ce322', fg='black',)
sick_entry.pack(side=RIGHT)
sick_entry.place(x=300, y=20)

MDurationOfTreatment=Label(window, text="DurationOfTreatment", bg='#4ce322', fg='black')
MDurationOfTreatment.pack(side=LEFT)
MDurationOfTreatment.place(x=20, y=80)

weeks_monthly=Label(window, text="Weekly/Months", bg='#4ce322', fg='black')
weeks_monthly.pack(side=RIGHT)
weeks_monthly.place(x=380, y=80)

due_entry=Entry(window, bd=1, width=8, bg='#4ce322', fg='black',)
due_entry.pack(side=RIGHT)
due_entry.place(x=300, y=80)

MDoctorsID=Label(window, text="DoctorsPracticeNumber", bg='#4ce322', fg='black')
MDoctorsID.pack(side=LEFT)
MDoctorsID.place(x=20, y=150)

doc_entry=Entry(window, bd=1, bg='#4ce322', fg='black',)
doc_entry.pack(side=RIGHT)
doc_entry.place(x=300, y=150)

scan_fee=Label(window, text="Scan/Consultation Fee", bg='#4ce322', fg='black',)
scan_fee.pack(side=LEFT)
scan_fee.place(x=20, y=190)

scan_entry = Entry(window, bd=1, bg='#4ce322', fg='black')
scan_entry.pack(side=RIGHT)
scan_entry.place(x=301, y=190)


amount_paid=Label(window)
amount_paid.pack(side=LEFT)
amount_paid.place(x=20, y=260)

var=StringVar()

# The Calculations for the Sick Class


class Sick():
    def sickness(self):
        self.MSickID = MSickID
        self.MDurationOfTreatment = MDurationOfTreatment
        self.MDoctorsID = MDoctorsID
        self.medcancer = 400
        self.medinflu = 350.50

# Calculating Cancer


def sickness():
    if var.get() == "Cancer":
        if int(scan_entry.get()) > 600:
            # Error message will display


                messagebox.showinfo("Message", "Sorry we cannot treat you")
        elif int(scan_entry.get()) < 600:
           cancer_answer = int(scan_entry.get()) + 400
           amount_paid.config(text="AmountPaidForTreatment: " + str(cancer_answer))


# Calculation for the Influenza


    if var.get() == "Influenza":
        if int(scan_entry.get()) >= 600:
            influ_answer = 350.50 + int(scan_entry.get())
            amount_paid.config(text="AmountPaidForTreatment: " + str(influ_answer))
        elif int(scan_entry.get()) < 600:
            influ_answer = 350.50 + int(scan_entry.get())
            discount = (influ_answer * (2/100)) + influ_answer

# Calculating the discount recieved for the influenza


            messagebox.showinfo("Message", "2% discount")
# The discount will be included in the calculation


            amount_paid.config(text="Amount Paid For Treatment: "  + str(discount))


# Radiobutton for Cancer


radbtn1=Radiobutton(window, text="Cancer", variable=var, value="Cancer")
radbtn1.pack(side=LEFT)
radbtn1.place(x=20, y=220)
# Radiobutton for Influenza


radbtn2=Radiobutton(window, text="Influenza", variable=var, value="Influenza")
radbtn2.pack(side=LEFT)
radbtn2.place(x=20, y=240)
# Calculates the amount paid for treatment once pushed


cal_btn=Button(window, text="Calculate", command=sickness, bg='#808080', fg='black',)
cal_btn.pack(side = LEFT)
cal_btn.place(x = 20, y = 300)
# Function on the clear all button


def clear_all():
    sick_entry.delete(0,END)
    due_entry.delete(0,END)
    doc_entry.delete(0,END)
    scan_entry.delete(0,END)
#Clears everything when the button is pushed


clear_btn=Button(window, text="Clear", command=clear_all, bg='#808080', fg='black')
clear_btn.pack(side=RIGHT)
clear_btn.place(x=300, y=300)
exit_btn=Button(window, text="Exit", command=window.destroy, bg='#808080', fg='black').place(x=425, y=450)


window.mainloop()
