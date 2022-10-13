"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from ast import Try 
class Employee:
    def __init__(self, name,hourly,hourly_rate, no_of_hours, monthly, monthly_rate,commission,no_of_commision,price_of_commission, bonus_commission, price_of_bonus_commission):
        self.name = name
        self.hourly=hourly
        self.hourly_rate=hourly_rate
        self.no_of_hours=no_of_hours
        self.monthly=monthly
        self.monthly_rate=monthly_rate
        self.commission=commission
        self.no_of_commission=no_of_commision
        self.price_of_commission=price_of_commission
        self.bonus_commission=bonus_commission
        self.price_of_bonus_commision=price_of_bonus_commission
        self.pay=None
        


    def get_pay(self):
        if self.monthly==True:
            if self.getCommission()==True:
                self.pay=self.getMonthlyRate()+(self.getNumberofCommissions()*self.getPriceOfCommissions())
            elif self.getBonusCommission():
                self.pay=self.getMonthlyRate()+self.getPriceOfBonusCommission()
            else:
                self.pay=self.getMonthlyRate
            return self.pay
        elif self.hourly==True:
            if self.getCommission()==True:
                self.pay=(self.getHourlyRate()*self.getNumberOfHours())+(self.getNumberofCommissions()*self.getPriceOfCommissions())
            elif self.getBonusCommission()==True:
                self.pay=((self.getHourlyRate()*self.getNumberOfHours())+self.getPriceOfBonusCommission())
            else:
                self.pay=(self.getHourlyRate()*self.getNumberOfHours())
            return self.pay

    def __str__(self):
        if self.hourly==True:
            if self.commission==True:
                return f"{self.name} works on a contract of {self.no_of_hours} hours at {self.hourly_rate}/hour and receives a commission for {self.no_of_commission} contract(s) at {self.price_of_commission}/contract.  Their total pay is {self.get_pay()}."
            elif self.bonus_commission==True:
                return f"{self.name} works on a contract of {self.no_of_hours} hours at {self.hourly_rate}/hour receives a bonus commission of {self.price_of_bonus_commision}.  Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.no_of_hours} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."
        else:
            if self.commission==True:
                return f"{self.name} works on a monthly salary of {self.monthly_rate} and receives a commission for {self.no_of_commission} contract(s) at {self.price_of_commission}/contract.  Their total pay is {self.get_pay()}."
            elif self.bonus_commission==True:
                return f"{self.name} works on a monthly salary of {self.monthly_rate} receives a bonus commission of {self.price_of_bonus_commision}.  Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} work on a monthly salary of {self.hourly_rate} hours.  Their total pay is {self.get_pay()}."
    def getHourlyRate(self):
        return self.hourly_rate
    def getNumberOfHours(self):
        return self.no_of_hours
    def getMonthlyRate(self):
        return self.monthly_rate
    def getNumberofCommissions(self):
        return self.no_of_commission
    def getPriceOfCommissions(self):
        return self.price_of_commission
    def getPriceOfBonusCommission(self):
        return self.price_of_bonus_commision
    def getBonusCommission(self):
        return self.bonus_commission
    def getCommission(self):
        return self.commission


        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',False,0,0,True,4000,False,0,0,False,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',True,25,100,False,0,False,0,0,False,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',False,0,0,True,3000,True,4,200,False,0)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',True,25,150,False,0,True,3,220,False,0)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',False,0,0,True,2000,False,0,0,True,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',True,30,120,False,0,False,0,0,True,600)

