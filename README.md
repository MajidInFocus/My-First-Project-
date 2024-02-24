# My-First-Project-
This my very first project that I worked on back in 2021 when I was preparing for IGCSE Computer science exam. I implemented the project in a series of steps from text-based program to GUI based.  The reference to the project is as follows; Cambridge IGCSE COMPUTER SCIENCE 0478/22 Paper 2 Problem-solving and Programming May/June 2021 PRE-RELEASE MATERIAL. 

The program is written in Python. The neccasary comments are provided. Please feel free to update the codes. 

The program starts here.-


#========================== TASK1 ==============================

train_up_time = [9,11,13,15]
train_down_time = [10,12,14,16]
train_up_ticket =[480]*4
train_down_ticket =[480,480,480,640]
train_up_money =[0.00]*4
train_down_money = [0.00]*4
train_up_passenger = [0]*4
train_down_passenger = [0]*4

def setup_screen():
        print("The available time and tickets for the trip Up and Down to and from the mountain ")
        print("Available time\t\t Available tickets \t\tTotal passenger \t\t Total money of the trip / $ \n")
        for i in range(0, 4):
                print(train_up_time[ i ], "\t\t\t", train_up_ticket[ i ], "\t\t\t",  train_up_passenger[ i ],"\t\t\t",train_up_money[ i ])
                print(train_down_time[ i ], "\t\t\t", train_down_ticket[ i ], "\t\t\t", train_down_passenger[ i ],"\t\t\t", train_down_money[ i ])
setup_screen()


#========================== TASK2 ===============================================

cost = 25.00
index_up = 0
index_down = 0
ticket_cost = 0
ticket_counter = 0

selling_ticket = int(input("Would you like buy ticket for the trip ? Enter 1 othersie enter -1 to close the system.  :  " ))
        
while selling_ticket == 1:

        time_up = int(input("What time would you like to buy for 9 11 13 15? :  "))
        while time_up != 9 and time_up != 11 and time_up != 13 and time_up != 15 :
                print("Error! please select the appropraite time from the available.")
                time_up = int(input("What time would you like buy for 9 11 13 15? :  "))
                
        time_down = int(input("What time would you like to return 10 12 14 16? :  "))
        while time_up > time_down or ( time_down != 10 and time_down != 12 and time_down != 14 and time_down  != 16) :
                print("Error! please select the appropraite time (you must not select the time below the departure)." )
                time_down = int(input("What time would you like to return 10 12 14 16? :  "))
                
        for count in range(0,4):
                if time_up == train_up_time[ count ]:
                        index_up = count
                if time_down == train_down_time[count]:
                        index_down = count

        for i in range(0, 4):
                if train_up_ticket [ index_up ] ==  "CLOSED":
                        train_up_ticket [ index_up ] = 0
                if train_down_ticket[ index_down ] == "CLOSED" :
                        train_down_ticket[ index_down ] = 0

        num_ticket = int(input("How many tickets would you like to buy? :  "))
        while  num_ticket > train_up_ticket[ index_up ] or num_ticket > train_down_ticket [ index_down ] :
                        print("Error! Please recheck the availability of the trian ticket")
                        num_ticket = int(input("How many tickets would you like to buy? :  "))
                                
        train_up_ticket [ index_up ] = train_up_ticket [ index_up ] -  num_ticket
        train_down_ticket[ index_down ] = train_down_ticket[ index_down ] - num_ticket
        if num_ticket >= 10:
                ticket_cost = cost * (num_ticket - (num_ticket//10) )
                print("Every 10th passenger is FREE!")
                print("Your total trip cost including the discount is:   ", "$", ticket_cost*2 )
        else:
                ticket_cost =(cost * num_ticket)
                print("Your total trip cost:   ", "$", ticket_cost*2 )

        train_up_money[ index_up ] = train_up_money[ index_up ] +  ticket_cost
        train_down_money[ index_down ] = train_down_money[ index_down ] + ticket_cost
        if train_up_ticket [ index_up ] ==  0:
                train_up_ticket [ index_up ] = "CLOSED"
        if train_down_ticket[ index_down ] == 0:
                train_down_ticket[ index_down ] = "CLOSED"
        train_down_passenger[ index_down ] = train_down_passenger[ index_down ] + num_ticket
        train_up_passenger[ index_up ] = train_up_passenger[ index_up ] + num_ticket
        setup_screen()
        selling_ticket = int(input("Would you like buy ticket for the trip ? Enter 1 otherwise enter -1 to close the system.  :  " ))

        
#========================== TASK3 ==================================================================

highest_passenger_time = 0
highest_passenger  = 0
passenger_up = [ 0 ]*4
passenger_down = [ 0 ]*4
total_passenger = 0
total_money = 0.0

if selling_ticket == -1 :
        for i in range(0, 4):
                if train_up_ticket [ index_up ] ==  "CLOSED":
                        train_up_ticket [ index_up ] = 0
                if train_down_ticket[ index_down ] == "CLOSED" :
                        train_down_ticket[ index_down ] = 0
                        
        for i in range(0, 4):
              passenger_up[ i ] = 480 -  train_up_ticket[ i ]
              if passenger_up[ i ] > highest_passenger :
                      highest_passenger  = passenger_up[ i ]
                      highest_passenger_time = train_up_time[ i ]
              print("Number of passenger: ", passenger_up[ i ], "Total money: ", train_up_money[ i ], "at  ", train_up_time[ i ], ": 00")
              
              passenger_down[ i ] = 480 -  train_down_ticket[ i ]
              if passenger_down[ i ] > highest_passenger :
                      highest_passenger  = passenger_down[ i ]
                      highest_passenger_time = train_down_time[ i ]
              print( "Number of passenger: ", passenger_down[ i ], "Total money: ", train_down_money[ i ], "at  ", train_down_time[ i ],": 00")

        passenger_up[ 3 ] = 480 -  train_up_ticket[ 3 ]
        print ("Number of passenger: ", passenger_up[ 3 ] , "Total money: ", train_up_money[3], "at  ", train_up_time[ 3 ],": 00" )
        passenger_down[ 3 ] = 640 -  train_down_ticket[ 3 ]
        print ( "Number of passenger: ", passenger_down[ 3 ] , "Total money: ", train_down_money[ 3 ], "at  ", train_down_time[ 3 ],": 00")
        if passenger_down[ 3 ] > highest_passenger :
                highest_passenger  = passenger_down[3]
                highest_passenger_time = train_down_time[ 3 ]
                      
        if passenger_up[ i ] > highest_passenger :
                highest_passenger  = passenger_up[ 3 ]
                highest_passenger_time = train_up_time[ 3 ]
      
        for i in range(0,4):
                total_passenger = total_passenger + passenger_up[ i ]
                total_money = total_money + 2*train_up_money[ i ]
       
        print("Total money of the day:  ", "$", total_money)
        print("Total passenger of the day:  ",  total_passenger )
        print ("Highest number of passengers", highest_passenger, " at   ", highest_passenger_time,": 00" )


-The program ends here.
             
