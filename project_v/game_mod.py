import random
import graphic as g
import credentials as cred


print("Welcome to HAND CRICKET")

u_name = input("Enter your username: ")
pword = input("Enter your password: ")
cred.register(u_name, pword)

'''g.print_teams()
n = int(input("Enter your team choice:"))
print("Your team is:",g.teams[n-1])'''
