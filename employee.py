"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from ast import Try
class Employee:
    def __init__(self, name, monthly_salary=0,hourly_rate=0, hours=0, contract_rate=0, no_of_contracts=0, bonus=0):
        self.name = name
        self.monthly_salary=monthly_salary
        self.hourly_rate=hourly_rate
        self.hours=hours
        self.contract_rate=contract_rate
        self.no_of_contracts=no_of_contracts
        self.bonus=bonus
        


    def get_pay(self):
        self.pay=self.monthly_salary
        if self.hours!= 0:
            self.pay=self.pay+(self.hours*self.hourly_rate)
        if self.no_of_contracts!=0:
            self.pay=self.pay(self.no_of_contracts*self.contract_rate)
        if self.bonus!=0:
            self.pay=self.pay+self.bonus
        return self.pay

    def __str__(self):
        if self.hours!=0:
            if self.no_of_contracts!=0:
                return f"{self.name} works on a contract of {self.hours} hours at {self.hourly_rate}/hours and recived a commission for {self.no_of_contracts} contract(s) at {self.contract_rate}/contract.  Thier total pay is {self.get_pay()}"
            if self.bonus!=0:
                return f"{self.name} works on a contract of {self.hours} hours at {self.hourly_rate}/hours and receives a bonus commission of {self.no_of_contracts} contract(s) at {self.bonus}.  Thier total pay is {self.get_pay()}"
            else:
                return f"{self.name} works on a contract of {self.hours} hours at {self.hourly_rate}/hours.  Their total pay is {self.get_pay()}."
        if self.monthly_salary!=0:
            if self.no_of_contracts!=0:
                return f"{self.name} works on a monthly salary {self.monthly_salary} and recived a commission for {self.no_of_contracts} contract(s) at {self.contract_rate}/contract.  Thier total pay is {self.get_pay()}"
            if self.bonus!=0:
                return f"{self.name} works on a monthly salary {self.monthly_salary} and receives a bonus commission of {self.no_of_contracts} contract(s) at {self.bonus}.  Thier total pay is {self.get_pay()}"
            else:
                return f"{self.name} works on a monthly salary {self.monthly_salary}.  Their total pay is {self.get_pay()}."



        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', monthly_salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours=100, hourly_rate=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', monthly_salary=3000, no_of_contracts=4,contract_rate=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, hourly_rate=25, no_of_contracts=3,contract_rate=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', monthly_salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, hourly_rate=30, bonus=600)
