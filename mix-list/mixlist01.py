#!/usr/bin/env python3

my_list = ["192.168.0.5",5060,"UP"]
new_list = [5060,"80",55,"10.0.0.1","10.20.30.1","ssh"]
print("The first item in the list (IP): " + my_list[0] )
print("The first item in the list (Port): " + str(my_list[1]) )
print("The first item in the list (State): " + my_list[2] )

print("When I " + str(new_list[5]) + " in to IP addresses " + str(new_list[3]) + " " + str(new_list[4]) + " I am unable to ping ports " + str(new_list[0]) + ", "  + str(new_list[1]) + ", or " +  str(new_list[2])  )

