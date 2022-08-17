# # import turtle

# # t = turtle.Turtle()

# # s = turtle.Screen()

# # print(s.canvheight)
# # s.exitonclick()
# from prettytable import PrettyTable
# table = PrettyTable()

# cases = PrettyTable()

# table.field_names = ["FirstName", "LastName", "Country", "Age"]

# table.add_rows([
#     ["Didier", "Ukanda", "Congo", 45],
#     ["Cathy", "Bonder", "Romania", 32],
#     ["Iohana", "Ukanda-Bonder", "Belgique", 8],
#     ["Imanuel", "Ukanda-Bonder", "Belgique", 6]
# ])


# print(cases)
# print(table)

# import msvcrt as m
# # récupère le caractère sous la forme de byte
# char = m.getch()
# # convertir de bytes en string
# c = char.decode("ascii")

class Bank_account():
    def __init__(self, account_number, credit_line, balance):
        self.account_number = account_number
        self.credit_line = credit_line
        self.balance = balance
        self.owner = Person()
    
    def get_balance(self):
        return self.balance
    
    def get_birthdate(self):
        return (self.birthdate)