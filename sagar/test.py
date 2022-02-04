class pizza:

    def __init__(self, money):

        self.money = money

    def a(self):
        self.money=3
        self.r = 1

obj=pizza(99)

obj.amount=4

obj.total=2
obj.a()

print(obj.amount+len(obj.__dict__))
