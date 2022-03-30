# import turtle

# t = turtle.Turtle()

# s = turtle.Screen()

# print(s.canvheight)
# s.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["FirstName", "LastName", "Country", "Age"]

table.add_rows([
    ["Didier", "Ukanda", "Congo", 45],
    ["Cathy", "Bonder", "Romania", 32],
    ["Iohana", "Ukanda-Bonder", "Belgique", 8],
    ["Imanuel", "Ukanda-Bonder", "Belgique", 6]
])

print(table)