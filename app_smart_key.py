import tkinter as tk
from tkinter import messagebox

from constants.app_consts import (PADX, PADY)
from services.db_manager import (db_init,
                                 check_users_pin)


db_init()

main_window = tk.Tk()
main_window.title('Smart Key app')
main_window.geometry('500x900')

#region FUNCTIONS
#region BUTTON FUNCTIONS
def on_door_bell():
    lbl_message_var.set('Zvono se oglasilo!\nNetko ce Vam uskoro otvoriti vrata.')
    messagebox.showinfo('DoorBell', 'Zvono se oglasilo!\nNetko ce Vam uskoro otvoriti vrata.')

def on_unlock():
    frm_pins.pack(padx=PADX, pady=PADY)
    frm_admin.pack(padx=PADX, pady=PADY)
#endregion

#region PIN FUNCTIONS
def on_pin_1():
    pin('1')
    
def on_pin_2():
    pin('2')
    
def on_pin_3():
    pin('3')
    
def on_pin_4():
    pin('4')
    
def on_pin_5():
    pin('5')
    
def on_pin_6():
    pin('6')
    
def on_pin_7():
    pin('7')
    
def on_pin_8():
    pin('8')
    
def on_pin_9():
    pin('9')
    
def on_pin_0():
    pin('0')

def on_pin_c():
    pin_value = lbl_pin_var.get()
    if len(pin_value) == 1:
        pin_value = ''
        lbl_pin_var.set('')
        update_pin_labels(pin_value)

    pin_value = pin_value[ : -1 ]
    lbl_pin_var.set(pin_value)
    lbl_placeholder_admin_var.set(pin_value)
    lbl_pin_message_var.set(init_pin_message)
    update_pin_labels(pin_value)

def on_pin_ce():
    lbl_pin_var.set('')
    lbl_pin_1_var.set('')
    lbl_pin_2_var.set('')
    lbl_pin_3_var.set('')
    lbl_pin_4_var.set('')
    lbl_placeholder_admin_var.set('')
    lbl_pin_message_var.set(init_pin_message)

def pin(number: str):
    pin_value = lbl_pin_var.get()

    if len(pin_value) < 4:
        pin_value = lbl_pin_var.get()
        pin_value += number
        lbl_pin_var.set(pin_value)
        lbl_placeholder_admin_var.set(pin_value)
        update_pin_labels(pin_value)

    elif len(pin_value) == 4:
        lbl_pin_message_var.set(f'PIN: {pin_value} ne postoji u bazi')
        return


def update_pin_labels(pin_value):
    pin_lenght = len(pin_value)
    match pin_lenght:
        case 0:
            lbl_pin_1_var.set('')
            lbl_pin_2_var.set('')
            lbl_pin_3_var.set('')
            lbl_pin_4_var.set('')
                        
        case 1:
            lbl_pin_1_var.set(pin_value[0])
            lbl_pin_2_var.set('')
            lbl_pin_3_var.set('')
            lbl_pin_4_var.set('')
            
        case 2:
            lbl_pin_1_var.set(pin_value[0])
            lbl_pin_2_var.set(pin_value[1])
            lbl_pin_3_var.set('')
            lbl_pin_4_var.set('')
            
        case 3:
            lbl_pin_1_var.set(pin_value[0])
            lbl_pin_2_var.set(pin_value[1])
            lbl_pin_3_var.set(pin_value[2])
            lbl_pin_4_var.set('')
            
        case 4:
            lbl_pin_1_var.set(pin_value[0])
            lbl_pin_2_var.set(pin_value[1])
            lbl_pin_3_var.set(pin_value[2])
            lbl_pin_4_var.set(pin_value[3])            
            lbl_pin_message_var.set(f'PIN: {pin_value} ne postoji u bazi')
    

#endregion

#region ADMIN FUNCTIONS

#endregion

#endregion



#region FRAME BUTTONS
frm_buttons = tk.Frame(main_window,
                       borderwidth=5,
                       relief='raised',
                       width=400, height=150)
frm_buttons.pack(padx=PADX, pady=PADY)

lbl_message_var = tk.StringVar()
lbl_message = tk.Label(frm_buttons,
                       textvariable=lbl_message_var)
lbl_message.grid(row=0, column=0, columnspan=2,
                 padx=PADX, pady=PADY)

btn_doorbell = tk.Button(frm_buttons,
                         text='Pozvoni',
                         command=on_door_bell)
btn_doorbell.grid(row=1, column=0,
                  padx=PADX, pady=PADY)

btn_unlock = tk.Button(frm_buttons,
                       text='Otkljucaj',
                       command=on_unlock)
btn_unlock.grid(row=1, column=1,
                padx=PADX, pady=PADY)

#endregion

#region FRAME PINS
frm_pins = tk.Frame(main_window,
                    borderwidth=5,
                    relief='raised',
                    width=400, height=350)
frm_pins.columnconfigure(0, weight=1, minsize=20)
frm_pins.columnconfigure(1, weight=1, minsize=20)
frm_pins.columnconfigure(2, weight=1, minsize=20)
frm_pins.columnconfigure(3, weight=1, minsize=20)
frm_pins.columnconfigure(4, weight=4, minsize=80)

#region PIN LABELS
lbl_pin_var = tk.StringVar()
lbl_pin_var.set('')
lbl_pin_1_var = tk.StringVar()
lbl_pin_1 = tk.Label(frm_pins, textvariable=lbl_pin_1_var)
lbl_pin_1.grid(row=0, column=0, sticky='nesw')
lbl_pin_2_var = tk.StringVar()
lbl_pin_2 = tk.Label(frm_pins, textvariable=lbl_pin_2_var)
lbl_pin_2.grid(row=0, column=1, sticky='nesw')
lbl_pin_3_var = tk.StringVar()
lbl_pin_3 = tk.Label(frm_pins, textvariable=lbl_pin_3_var)
lbl_pin_3.grid(row=0, column=2, sticky='nesw')
lbl_pin_4_var = tk.StringVar()
lbl_pin_4 = tk.Label(frm_pins, textvariable=lbl_pin_4_var)
lbl_pin_4.grid(row=0, column=3, sticky='nesw')
#endregion

#region PIN BUTTONS
btn_pin_1 = tk.Button(frm_pins, text='1',
                      command=on_pin_1)
btn_pin_1.grid(row=1, column=0, sticky='nesw')
btn_pin_2 = tk.Button(frm_pins, text='2',
                      command=on_pin_2)
btn_pin_2.grid(row=1, column=1, sticky='nesw')
btn_pin_3 = tk.Button(frm_pins, text='3',
                      command=on_pin_3)
btn_pin_3.grid(row=1, column=2, sticky='nesw')
btn_pin_4 = tk.Button(frm_pins, text='4',
                      command=on_pin_4)
btn_pin_4.grid(row=2, column=0, sticky='nesw')
btn_pin_5 = tk.Button(frm_pins, text='5',
                      command=on_pin_5)
btn_pin_5.grid(row=2, column=1, sticky='nesw')
btn_pin_6 = tk.Button(frm_pins, text='6',
                      command=on_pin_6)
btn_pin_6.grid(row=2, column=2, sticky='nesw')
btn_pin_7 = tk.Button(frm_pins, text='7',
                      command=on_pin_7)
btn_pin_7.grid(row=3, column=0, sticky='nesw')
btn_pin_8 = tk.Button(frm_pins, text='8',
                      command=on_pin_8)
btn_pin_8.grid(row=3, column=1, sticky='nesw')
btn_pin_9 = tk.Button(frm_pins, text='9',
                      command=on_pin_9)
btn_pin_9.grid(row=3, column=2, sticky='nesw')
btn_pin_0 = tk.Button(frm_pins, text='0',
                      command=on_pin_0)
btn_pin_0.grid(row=4, column=1, sticky='nesw')
btn_pin_c = tk.Button(frm_pins, text='C',
                      command=on_pin_c)
btn_pin_c.grid(row=4, column=2, sticky='nesw')
btn_pin_ce = tk.Button(frm_pins, text='CE',
                      command=on_pin_ce)
btn_pin_ce.grid(row=4, column=0, sticky='nesw')
#endregion

init_pin_message = 'Za otkljucavanje vata upisite\ncetveroznamenskasti PIN'
lbl_pin_message_var = tk.StringVar()
lbl_pin_message_var.set(init_pin_message)
lbl_pin_message = tk.Label(frm_pins,
                           textvariable=lbl_pin_message_var)
lbl_pin_message.grid(row=0, column=4, rowspan=5, sticky='nesw')
#endregion

#region FRAME ADMIN
frm_admin = tk.Frame(main_window,
                     borderwidth=5,
                     relief='raised',
                     width=400, height=350)

lbl_placeholder_admin_var = tk.StringVar()
lbl_placeholder_admin = tk.Label(frm_admin,
                           text='PLACEHOLDER',
                           textvariable=lbl_placeholder_admin_var)
lbl_placeholder_admin.grid(row=0, column=0)
#endregion



if __name__ == '__main__':
    check_users_pin('1234')
    main_window.mainloop()
