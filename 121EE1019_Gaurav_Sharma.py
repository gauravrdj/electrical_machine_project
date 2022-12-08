from tkinter import *
from math import *
from tkinter import messagebox
root=Tk()
root.geometry("900x550")
root.title("Effect of interpole winding on Torque and efficiency of machine: ")
def torque():
              ple=float(poleentry.get())
              cnd=float(conductorentry.get())
              wind=str(windingentry.get())
              if(wind=="wave"):
                                wnd=2
              else:
                  wnd=ple

              flx=float(fluxentry.get())
              ires=float(interresentry.get())
              armcurr=wnd * float(currententry.get())
              emf=float(Eentry.get())
              volt=float(voltageentry.get())
              ra=float(armresentry.get())
              V=emf+ armcurr * ra
              deflux=(flx/emf)*(V-volt)
              old_torque=((ple * cnd)/(60 * wnd)) * (flx-deflux) * armcurr
              new_torque = ((ple * cnd)/(60 * wnd)) * (flx) * armcurr
              heat=(armcurr * armcurr * ires)/60000

              ans = Frame(root, borderwidth=6, relief=SUNKEN)
              ans.pack(side=RIGHT, padx=10)
              flux_name=Label(ans, text="Demagnetising Flux: ", font="timesnewroman 16 bold", fg="purple")
              flux_name.grid()
              old_name=Label(ans, text="Torque without interpole winding: ", font="timesnewroman 16 bold", fg="purple")
              old_name.grid(row=1, column=0)
              new_name=Label(ans, text="Torque after using interpole winding: ", font="timesnewroman 16 bold", fg="purple")
              new_name.grid(row=2, column=0)
              heatloss=Label(ans, text="Heat loss in interpole winding: ", font="timesnewroman 16 bold", fg="purple")
              heatloss.grid(row=3, column=0)
              label_old=Label(ans)
              label_new=Label(ans)
              label_heat=Label(ans)
              label_flux=Label(ans)
              label_flux.configure(text='' + f"{deflux}" + " Wb", font=" timesnewroman 15 bold", fg="red")
              label_flux.grid(row=0, column=1)
              label_old.configure(text='' + f"{old_torque}" + " N-m", font=" timesnewroman 15 bold", fg="red")
              label_old.grid(row=1, column=1)
              label_new.configure(text='' + f"{new_torque}" + " N-m", font=" timesnewroman 15 bold", fg="red")
              label_new.grid(row=2, column=1)
              label_heat.configure(text='' + f"{heat}" + " kVA-h", font=" timesnewroman 15 bold", fg="red")
              label_heat.grid(row=3, column=1)

f1= Frame(root, borderwidth=2, relief=SUNKEN)
f1.pack(side=TOP)
l1=Label(f1, text="Effect of Interpole winding on Torque in a DC Series motor: ", font="cambria 15 bold", fg="purple")
l1.grid(padx=15, pady=25)

button_frame=Frame(root, bg="#FCF9BE", borderwidth=3, relief=SUNKEN)
button_frame.pack(side=BOTTOM, pady=100)
b1=Button(button_frame, fg="red", text="Click here to get the Torque with interpole", font="cambria 15 bold",command=torque)
b1.pack(side=BOTTOM)


#input details
input_frame=Frame(root, borderwidth=5, relief=SUNKEN)
input_frame.pack(side=LEFT)
pole=Label(input_frame, text="Poles: ", font="helvetica 16 bold", fg="green")
pole.grid(pady=4)
conductor=Label(input_frame, text="No. of Conductors: ", font="helvetica 16 bold", fg="green")
conductor.grid(row=1, column=0,pady=4)
winding=Label(input_frame, text="Lap/Wave(just type lap/wave in smallcase): ", font="helvetica 16 bold", fg="green")
winding.grid(row=2, column=0,pady=4)
flux=Label(input_frame, text="Flux per pole (in Wb): ", font="helvetica 16 bold", fg="green")
flux.grid(row=3, column=0,pady=4)
current=Label(input_frame, text="Current through each conductor (at full load in Amp):  ", font="helvetica 16 bold", fg="green")
current.grid(row=4, column=0,pady=4)
E=Label(input_frame, text="Vopen circuit(Eb (Volt)): ", font="helvetica 16 bold", fg="green")
E.grid(row=5, column=0,pady=4)
voltage=Label(input_frame, text="Full load voltage(Volt): ", font="helvetica 16 bold", fg="green")
voltage.grid(row=6, column=0,pady=4)
armres=Label(input_frame, text="Armature resistance (ohm): ", font="helvetica 16 bold", fg="green")
armres.grid(row=7, column=0,pady=4)
interres=Label(input_frame, text="Interpole winding resistance (ohm): ", font="helvetica 16 bold", fg="green")
interres.grid(row=8, column=0,pady=4)
#taking input from user
polevalue=IntVar()
conductorvalue=IntVar()
windingvalue=StringVar()
fluxvalue=DoubleVar()
currentvalue=DoubleVar()
Evalue=DoubleVar()
voltagevalue=DoubleVar()
armresvalue=DoubleVar()
interresvalue=DoubleVar()

#entry
user_frame=Frame(root, borderwidth=5, relief=SUNKEN)
user_frame.pack(side=LEFT)
poleentry=Entry(user_frame, textvariable=polevalue, borderwidth=6, font="comicsansms 15 bold", relief=SUNKEN)
poleentry.grid(row=0, column=1)
conductorentry=Entry(user_frame, textvariable=conductorvalue, borderwidth=6, font="comicsansms 15 bold", relief=SUNKEN)
conductorentry.grid(row=1, column=1)
windingentry=Entry(user_frame, textvariable=windingvalue, borderwidth=6, font="comicsansms 15 bold", relief=SUNKEN)
windingentry.grid(row=2, column=1)
fluxentry=Entry(user_frame, textvariable=fluxvalue, borderwidth=6, font="comicsansms 15 bold", relief=SUNKEN)
fluxentry.grid(row=3, column=1)
currententry=Entry(user_frame, textvariable=currentvalue, borderwidth=6, font="comicsansms 15 bold", relief=SUNKEN)
currententry.grid(row=4, column=1)
Eentry=Entry(user_frame, textvariable=Evalue, borderwidth=6, font="comicsansms 15 bold", relief=SUNKEN)
Eentry.grid(row=5, column=1)
voltageentry=Entry(user_frame, textvariable=voltagevalue, borderwidth=6, font="comicsansms 15 bold", relief=SUNKEN)
voltageentry.grid(row=6, column=1)
armresentry=Entry(user_frame, textvariable=armresvalue, borderwidth=6, font="comicsansms 15 bold", relief=SUNKEN)
armresentry.grid(row=7, column=1)
interresentry=Entry(user_frame, textvariable=interresvalue, borderwidth=6, font="comicsansms 15 bold", relief=SUNKEN)
interresentry.grid(row=8, column=1)

#my detail
myname=Label(f1, text="By- Gaurav Sharma, Roll no.- 121EE1019", font="comicsansms 15 bold", fg="#FF6D28")
myname.grid(row=1, column=0)
root.mainloop()