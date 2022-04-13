# import turtle

# t = turtle.Turtle()

# s = turtle.Screen()

# print(s.canvheight)
# s.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()

cases = PrettyTable()

table.field_names = ["FirstName", "LastName", "Country", "Age"]

table.add_rows([
    ["Didier", "Ukanda", "Congo", 45],
    ["Cathy", "Bonder", "Romania", 32],
    ["Iohana", "Ukanda-Bonder", "Belgique", 8],
    ["Imanuel", "Ukanda-Bonder", "Belgique", 6]
])


print(cases)
print(table)

import msvcrt as m
# récupère le caractère sous la forme de byte
char = m.getch()
# convertir de bytes en string
c = char.decode("ascii")