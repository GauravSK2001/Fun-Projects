class Category:
    def __init__(self,name):
        self.ledger=[]
        self.name=name

    def __str__(self):
        title = str(self.name.center(30, '*'))
        items = f""
        for entry in self.ledger:
            description = entry['description'][:23].ljust(23)
            aa=entry['amount']
            amount = f"{aa:.2f}".rjust(7)
            items += description+amount+'\n'
        total = f"Total: {self.get_balance():.2f}"
        return title+'\n'+items+total

    def deposit(self,amount,description=''):
        (self.ledger).append({'amount': amount, 'description': description})

    def withdraw(self,amount,description=''):
        
        if self.check_funds(amount):
            (self.ledger).append({'amount': -1*amount, 'description': description})
            return True
        else:
            return False
        
    def get_balance(self):
        total=0
        for i in self.ledger:
            total+=i['amount']
        return total
    

    def transfer(self,amount,ccategory):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {ccategory.name}')
            ccategory.deposit(amount, f'Transfer from {self.name}')

            return True
        else:
            return False
        
        
    def check_funds(self,amount):
        return amount <= self.get_balance()




#takes a list of categories as an argument. It should return a string that is a bar chart.
def create_spend_chart(categories):
    # Calculate the total spending in each category
    total_spending = 0
    category_spending = []
    for category in categories:
        spending = sum(-entry['amount'] for entry in category.ledger if entry['amount'] < 0)
        print((category.name, spending))
        category_spending.append((category.name, spending))
        total_spending += spending
    
    # Calculate spending percentages
    category_percentages = [(name, (spending / total_spending) * 100) for name, spending in category_spending]
    





    chart='Percentage spent by category\n'
    input=''

    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}| "
        for name, percentage in category_percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
     # Add the horizontal line
    chart += "    -" + "---" * len(categories) + "\n"
    
    max_name_length = max(len(name) for name, _ in category_percentages)
    for i in range(max_name_length):
        chart += "     "
    
        for name, _ in category_percentages:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i<max_name_length-1:
            chart+='\n'
        
    # print(category_percentages)
    # print(chart)
    return chart




A=Category('Business')

B=Category('Food')
C=Category('Entertainment')


A.deposit(10000,'dep1')
# A.deposit(1000,'dep31')
B.deposit(10400,'dep3')
B.withdraw(105.55,'wdep3')
A.withdraw(10.99,'wdep3')
# A.deposit(2000000,'depddddddjhjhjhjhhjhjhjhjhjhjhjhjhjhjhddddddddd')
C.deposit(10400,'dep3')
C.withdraw(33.4,'wdep3')

# print(A)
# print(B)
# print(C)


print(create_spend_chart([A,B,C]))


