from tkinter import*
screenTK = 0
screenMN = 0
cost = 25
total = 0
ticket_cost =0

def calculator():
        global  screenTK
        global screenMN
        global cost
        global total
        global ticket_cost

        
        price_display.delete(0.0, END)
        num_ticket = int(entry_ticket.get())
        time_up= int(var_options1.get())
        time_down = int(var_options2.get())
        ticket_cost = int(ticket_cost)

        if time_up != 9 and time_down < time_up or time_up != 11 and time_down < time_up or time_up != 13 and time_down < time_up or time_up != 15 and time_down < time_up :
                price_display.insert(0.0, "ERROR")

        if time_up == 9 and time_down > time_up or time_up == 11 and time_down > time_up or time_up == 13 and time_down > time_up or time_up == 15 and time_down > time_up :
                if num_ticket >= 10:
                        discount = num_ticket - int(num_ticket/10)
                        ticket_cost = cost *discount 
                else:
                        ticket_cost = cost * num_ticket
                        
                
                final_cost =  2*ticket_cost
                price_display.insert(0.0,  final_cost)
                
        total  = total  + final_cost
        ticket_cost = ticket_cost + ticket_cost
        ticket_cost = str(ticket_cost )
        screenTK = 480 - num_ticket
        if screenTK == 0:
                screenTK = "Closed"
        else:
                screenTK = str(480 - num_ticket)

                 
                        
                if time_up == 9:
                        screenTKup1 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = screenTK, bg = 'silver')
                        screenTKup1.grid(row = 2, column = 1, sticky = W)
                        screenMNYup1 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = ticket_cost, bg = 'silver')
                        screenMNYup1.grid(row = 2, column = 2, sticky = W)

                if time_up == 11:
                        screenTKup2 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = screenTK, bg = 'silver')
                        screenTKup2.grid(row = 3, column = 1, sticky = W)
                        screenMNYup2 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = ticket_cost, bg = 'silver')
                        screenMNYup2.grid(row = 3, column = 2, sticky = W)

                if time_up == 13:
                        screenTKup3 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = screenTK, bg = 'silver')
                        screenTKup3.grid(row = 4, column = 1, sticky = W)
                        screenMNYup3 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = ticket_cost, bg = 'silver')
                        screenMNYup3.grid(row = 4, column = 2, sticky = W)
                        
                if time_up == 15:
                        screenTKup4 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = screenTK, bg = 'silver')
                        screenTKup4.grid(row = 5, column = 1, sticky = W)
                        screenMNYup4 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = ticket_cost, bg = 'silver')
                        screenMNYup4.grid(row = 5, column = 2, sticky = W)
                        
                if time_down == 10:
                        screenTKdw1 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = screenTK, bg = 'silver')
                        screenTKdw1.grid(row = 6, column = 1, sticky = W)
                        screenMNYdw1 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = ticket_cost, bg = 'silver')
                        screenMNYdw1.grid(row = 6, column = 2, sticky = W)
          
                elif time_down == 12:
                        screenTKdw2 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text =screenTK, bg = 'silver')
                        screenTKdw2.grid(row = 7, column = 1, sticky = W)
                        screenMNYdw2 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text =ticket_cost, bg = 'silver')
                        screenMNYdw2.grid(row = 7, column = 2, sticky = W)
                        
                if time_down == 14:
                        screenTKdw3 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text =screenTK, bg = 'silver')
                        screenTKdw3.grid(row = 8, column = 1, sticky = W)
                        screenMNYdw3 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = ticket_cost, bg = 'silver')
                        screenMNYdw3.grid(row = 8, column = 2, sticky = W)
                        
                if time_down == 16:
                        screenTK = str(640 - num_ticket)
                        screenTKdw4 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = screenTK , bg = 'silver')
                        screenTKdw4.grid(row = 9, column = 1, sticky = W)
                        screenMNYdw4 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = ticket_cost, bg = 'silver')
                        screenMNYdw4.grid(row = 9, column = 2, sticky = W)
                        

        var_options1.set('Select:')
        var_options2.set('Select:')
        entry_ticket.delete(0, END)

def clearer():
        price_display.delete(0.0, END)
        entry_ticket.delete(0, END)
        var_options1.set('Select:')
        var_options2.set('Select:')

def reset():
        def quick2():
                window.destroy()
      #define the window
        window = Tk()
        #name a title for the icon
        window.title('Pre-released material')
        #define the geometry of the window and provide a configure colour
        window.geometry('320x490')
        window.configure(bg = 'silver')
        #frame for title lable
        title_frame = LabelFrame(window, width = 260, height = 35,  font =('times roman', 15, 'bold'),
                                 fg = 'dark blue', bg = 'white',
                                 text = 'TRIP TO THE MOUNTAIN' , bd = 3 )
        title_frame.pack()
        #title_frame.grid(row = 0, column = 0, columnspan = 3)
        lable_text = Label(window,   font =('times roman', 15, 'bold'), fg = 'black', bg = 'white',
                                 text = 'END OF THE DAY' , bd = 3 )
        lable_text.pack()
        #lable_text.grid(row = 1, column = 0, columnspan = 3)
        
        button_close2 = Button(window, width = 8, bd = 5, bg = 'silver', fg ='black', font = ('times roman', 10, 'bold'), text ='Quick', command = quick2)
        button_close2.pack()
        #button_close2.grid(row = 2, column = 1 )
        

def close():
        price_display.delete(0.0, END)
        price_display.insert(0.0, total)


def quick():
        window.destroy()

def clearer():
        price_display.delete(0.0, END)
        entry_ticket.delete(0, END)
        var_options1.set('Select:')
        var_options2.set('Select:')

            
#define the window
window = Tk()
#name a title for the icon
window.title('Pre-released material')
#define the geometry of the window and provide a configure colour
window.geometry('320x490')
window.configure(bg = 'silver')
#frame for title lable
title_frame = LabelFrame(window, width = 260, height = 35,  font =('times roman', 15, 'bold'),
                         fg = 'dark blue', bg = 'white',
                         text = 'TRIP TO THE MOUNTAIN' , bd = 3 ).grid(row = 0,
                                                                 column = 0, columnspan = 3)

#======================================================================

        
time_frame = Label(window, font =('times roman', 13, 'bold'), fg = 'dark blue', text ='TIME' , bg = 'silver')
time_frame.grid(row = 1, column = 0)
ticket_frame = Label(window, font =('times roman', 13, 'bold'), fg = 'dark blue', text ='TICKETS', bg = 'silver' )
ticket_frame.grid(row = 1, column = 1,  sticky =W)
money_frame = Label(window, font =('times roman', 13, 'bold'), fg = 'dark blue', text ='$', bg = 'silver' )
money_frame.grid(row = 1, column = 2,  sticky =W)

screenUPtime1 = Label(window, font = ('times roman', 12, 'bold'), fg = 'black', text = '9:00', bg = 'silver' )
screenUPtime1.grid(row =2, column =0)
screenUPtime2 = Label(window, font = ('times roman', 12, 'bold'), fg = 'black', text = '11:00', bg = 'silver')
screenUPtime2.grid(row =3, column =0)
screenUPtime3 = Label(window, font = ('times roman', 12, 'bold'), fg = 'black', text = '13:00', bg = 'silver')
screenUPtime3.grid(row =4, column =0)
screenUPtime4 = Label(window, font = ('times roman', 12, 'bold'), fg = 'black', text = '15:00', bg = 'silver')
screenUPtime4.grid(row =5, column =0)

screenDWtime1 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = '10:00', bg = 'silver')
screenDWtime1.grid(row = 6, column = 0)
screenDWtime2 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = '12:00', bg = 'silver')
screenDWtime2.grid(row = 7, column = 0)
screenDWtime3 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = '14:00', bg = 'silver')
screenDWtime3.grid(row = 8, column = 0)
screenDWtime4 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text = '16:00', bg = 'silver')
screenDWtime4.grid(row = 9, column = 0)

screenTKup1 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='480', bg = 'silver')
screenTKup1.grid(row = 2, column = 1, sticky = W)
screenTKup2 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='480', bg = 'silver')
screenTKup2.grid(row = 3, column = 1, sticky = W)
screenTKup3 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='480', bg = 'silver')
screenTKup3.grid(row = 4, column = 1, sticky = W)
screenTKup4 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='480', bg = 'silver')
screenTKup4.grid(row = 5, column = 1, sticky = W)

screenTKdw1 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='480', bg = 'silver')
screenTKdw1.grid(row = 6, column = 1, sticky = W)
screenTKdw2 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='480', bg = 'silver')
screenTKdw2.grid(row = 7, column = 1, sticky = W)
screenTKdw3 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='480', bg = 'silver')
screenTKdw3.grid(row = 8, column = 1, sticky = W)
screenTKdw4 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='640', bg = 'silver')
screenTKdw4.grid(row = 9, column = 1, sticky = W)

screenMNYup1 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='0.00', bg = 'silver')
screenMNYup1.grid(row = 2, column = 2, sticky = W)
screenMNYup2 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='0.00', bg = 'silver')
screenMNYup2.grid(row = 3, column = 2, sticky = W)
screenMNYup3 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='0.00', bg = 'silver')
screenMNYup3.grid(row = 4, column = 2, sticky = W)
screenMNYup4 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='0.00', bg = 'silver')
screenMNYup4.grid(row = 5, column = 2, sticky = W)

screenMNYdw1 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='0.00', bg = 'silver')
screenMNYdw1.grid(row = 6, column = 2, sticky = W)
screenMNYdw2 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='0.00', bg = 'silver')
screenMNYdw2.grid(row = 7, column = 2, sticky = W)
screenMNYdw3 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='0.00', bg = 'silver')
screenMNYdw3.grid(row = 8, column = 2, sticky = W)
screenMNYdw4 = Label(window, fg = 'black',  font = ('times roman', 12, 'bold'), text ='0.00', bg = 'silver')
screenMNYdw4.grid(row = 9, column = 2, sticky = W)

#======================================================================

#framelabel for selections 
broken_frame = Frame(window, width = 60, height = 45, bd = 3 )
broken_frame.grid(row = 10, column = 0, columnspan = 3)

#time up
departure_frame = LabelFrame(broken_frame, width  =  200, height  = 100,bg =
                        'white', fg = 'black', bd = 3,
                        text = "Departure Time",  font = ('times roman', 10, 'bold') )
departure_frame.grid(row = 0, column = 0,  sticky =W)
options1 = (9, 11,13,15)
var_options1 = IntVar()
var_options1.set('Select:')
menu = OptionMenu(departure_frame, var_options1, *options1)
menu.grid(row = 0, column = 0, pady = 3, sticky =W)

#time down
return_frame = LabelFrame(broken_frame, width  =  200, height  = 100,bg =
                        'white', fg = 'black', bd = 3,
                        text = "Return Time",  font = ('times roman', 10, 'bold') )
return_frame.grid(row = 0, column = 1,  sticky =W)
options2 = (10, 12,14,16)
var_options2 = IntVar()
var_options2.set('Select:')
menu = OptionMenu(return_frame, var_options2, *options2)
menu.grid(row = 0, column = 0, pady = 3, sticky =W)

#create a label and entry for the ticket widget
label_ticket = Label(broken_frame, font = ('times roman', 10, 'bold'), text =
                       "Ticket number  ").grid(row = 1, column = 0)
entry_ticket = Entry(broken_frame, bd = 6, bg = 'powder blue', font =
                       ('times roman', 13, 'bold'), width = 19)
entry_ticket.grid(row = 1, column = 1, columnspan = 2)

#======================================================================
#framelabel for buttons
button_frame =Frame(window, width = 60, height = 45, bd = 3 )
button_frame.grid(row = 11, column = 0, columnspan = 3  )
#create button that will call the function
calculate_button = Button(button_frame , width = 8, bd = 5, bg = 'silver', fg ='black',
                font = ('times roman', 10, 'bold'), text ='Calculate', command =calculator)
calculate_button.grid(row = 0, column = 0)
#create button that will call the function
button_clear = Button(button_frame , width = 8, bd = 5, bg = 'silver', fg ='black', font = ('times roman', 10, 'bold'), text ='Clear', command =clearer)
button_clear.grid(row = 1, column = 0)
button_end = Button(button_frame , width = 8, bd = 5, bg = 'silver', fg ='black', font = ('times roman', 10, 'bold'), text ='CLOSE', command =close)
button_end.grid(row = 1, column = 1)
button_reset = Button(button_frame , width = 8, bd = 5, bg = 'silver', fg ='black', font = ('times roman', 10, 'bold'), text ='Reset', command = reset)
button_reset.grid(row = 2, column = 0)
button_close = Button(button_frame , width = 8, bd = 5, bg = 'silver', fg ='black', font = ('times roman', 10, 'bold'), text ='Quick', command = quick)
button_close.grid(row = 2, column = 1 )

screen_price_l = Label(button_frame, font = ('times roman', 10, 'bold'), text = "Your cost  $:  ")
screen_price_l.grid(row = 0, column = 1)
price_display = Text(button_frame, width = 15, height = 6, bg  = 'white', fg = 'black',  font = ('times roman', 12, 'bold'))
price_display.grid(row = 0, column = 2, sticky = W, rowspan = 3)

button_reset = Button(button_frame , width = 8, bd = 5, bg = 'silver', fg ='black', font = ('times roman', 10, 'bold'), text ='Reset', command = reset)
button_reset.grid(row = 2, column = 0)
window.mainloop()
