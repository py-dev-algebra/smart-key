import tkinter as tk
from tkinter import messagebox

from constants.app_consts import (PADX, PADY)
from services.db_manager import (db_init,
                                 check_users_pin,
                                 get_all_users,
                                 get_user,
                                 delete_user,
                                 save_user)


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
    lbl_pin_message_var.set(init_pin_message)
    update_pin_labels(pin_value)

def on_pin_ce():
    lbl_pin_var.set('')
    lbl_pin_1_var.set('')
    lbl_pin_2_var.set('')
    lbl_pin_3_var.set('')
    lbl_pin_4_var.set('')
    lbl_pin_message_var.set(init_pin_message)

def pin(number: str):
    pin_value = lbl_pin_var.get()

    if len(pin_value) < 4:
        pin_value += number
        lbl_pin_var.set(pin_value)
        update_pin_labels(pin_value)
        if len(pin_value) == 4:
            user = check_users_pin(pin_value)
            if user != None:
                welcome_message = f'Dobro dosli!'
                welcome_message += f'{user[1]} {user[2]}'
                lbl_pin_message_var.set(f'{welcome_message}')
                frm_admin.pack(padx=PADX, pady=PADY)
                return
            else:
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
    

#endregion

#region ADMIN FUNCTIONS
def fill_users_listbox():
    users = get_all_users()
    lb_users.delete(0, tk.END)

    for user in users:
        lb_users.insert(tk.END, user)


def on_element_select(event):
    listbox_value = lb_users.get(lb_users.curselection())
    user = get_user(listbox_value[0])
    
    user_id_var.set(user[0])
    first_name_var.set(user[1])
    last_name_var.set(user[2])
    pin_form_var.set(user[3])
    is_active_var.set(user[4])


def on_save():
    first_name = first_name_var.get()
    last_name = last_name_var.get()
    pin = pin_form_var.get()
    is_active = is_active_var.get()

    save_user(pin_form_var.get(), first_name, last_name, pin, is_active)
    fill_users_listbox()
    

def on_cancel():
    lb_users.selection_clear(0, tk.END)
    
    user_id_var.set(0)
    first_name_var.set('')
    last_name_var.set('')
    pin_form_var.set('')
    is_active_var.set(0)

def on_delete():
    selected_user = lb_users.curselection()
    user = get_user(selected_user[0] + 1)
    
    delete_user(user[0])
    fill_users_listbox()
    on_cancel()

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

lb_users = tk.Listbox(frm_admin)
lb_users.grid(row=0, column=0, rowspan=5)
sc_lb_users = tk.Scrollbar(frm_admin,
                           orient=tk.VERTICAL,
                           command=lb_users.yview)
sc_lb_users.grid(row=0, column=1, rowspan=5)
lb_users.config(yscrollcommand=sc_lb_users.set)
fill_users_listbox()
lb_users.bind('<<ListboxSelect>>', on_element_select)

#region USERS FORM
user_id_var = tk.IntVar()
lbl_first_name = tk.Label(frm_admin, text='Ime')
lbl_first_name.grid(row=0, column=2, padx=PADX)
first_name_var = tk.StringVar()
entry_first_name = tk.Entry(frm_admin,
                            textvariable=first_name_var)
entry_first_name.grid(row=0, column=3, columnspan=2, padx=PADX)

lbl_last_name = tk.Label(frm_admin, text='Prezime')
lbl_last_name.grid(row=1, column=2, padx=PADX)
last_name_var = tk.StringVar()
entry_last_name = tk.Entry(frm_admin,
                            textvariable=last_name_var)
entry_last_name.grid(row=1, column=3, columnspan=2, padx=PADX)

lbl_pin = tk.Label(frm_admin, text='PIN (4 broja)')
lbl_pin.grid(row=2, column=2, padx=PADX)
pin_form_var = tk.StringVar()
entry_pin = tk.Entry(frm_admin,
                            textvariable=pin_form_var)
entry_pin.grid(row=2, column=3, columnspan=2, padx=PADX)

lbl_is_active = tk.Label(frm_admin, text='Aktivan')
lbl_is_active.grid(row=3, column=2, padx=PADX)

is_active_var = tk.IntVar()
cb_is_active = tk.Checkbutton(frm_admin, variable=is_active_var)
cb_is_active.grid(row=3, column=3, columnspan=2, padx=PADX)

#endregion

btn_save = tk.Button(frm_admin,
                     text='Spremi',
                     command=on_save)
btn_save.grid(row=4, column=2, padx=PADX, pady=PADY)

btn_cancel = tk.Button(frm_admin,
                     text='Odustani',
                     command=on_cancel)
btn_cancel.grid(row=4, column=3, padx=PADX, pady=PADY)

btn_delete = tk.Button(frm_admin,
                     text='Izbrisi',
                     command=on_delete)
btn_delete.grid(row=4, column=4, padx=PADX, pady=PADY)

#endregion



if __name__ == '__main__':
    main_window.mainloop()
