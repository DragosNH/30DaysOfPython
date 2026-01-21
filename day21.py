# --- Day 21: 30 Days of python programming ---
import statistics
from collections import Counter
import math

# 1. Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.


class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        if self.data:
            return len(self.data)
    
    def sum(self):
        if self.data:
            return sum(self.data)
    
    def min(self):
        if self.data:
            return min(self.data)

    def max(self):
        if self.data:
            return max(self.data)

    def range(self):
        if self.data:
            return self.max() - self.min()

    def mean(self):
        if len(self.data) > 0:
            return sum(self.data) / len(self.data)

    def median(self):
        if(self.data) and (len(self.data)>0):
            tmp_data = sorted(self.data)
            n = len(tmp_data)
            
            if(n%2 !=0):
                return (tmp_data[(n+1) // 2])
            else:
                a = tmp_data[n // 2]
                b = tmp_data[(n // 2) + 1]
                return ((a+b)/2)              

    def mode(self):
        c = Counter(self.data)
        return[k for k, v in c.items() if v == c.most_common(1)[0][1]]
    
    def var(self):
        mean = sum(self.data) / len(self.data)

        squared = list(map(lambda x: (x-mean)**2, self.data))
        
        return sum(squared) / (len(self.data) - 1)


    def std(self):
        if self.var():
            return(math.sqrt(self.var()))

    def freq_dist(self):
        if self.data:
            return set([(x, self.data.count(x)) for x in self.data])

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

# print('Count:', data.count()) # 25
# print('Sum: ', data.sum()) # 744
# print('Min: ', data.min()) # 24
# print('Max: ', data.max()) # 38
# print('Range: ', data.range()) # 14
# print('Mean: ', data.mean()) # 30
# print('Median: ', data.median()) # 29
# print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
# print('Standard Deviation: ', data.std()) # 4.2
# print('Variance: ', data.var()) # 17.5
# print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

# 2. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname = "John", lastname = "Doe", incomes = 2000):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes

    def person_info(self):
        return f"First name: {self.firstname}\nLast name: {self.lastname}\nIncomes: {self.incomes}"
        
class ExpensesProprietis(PersonAccount):
    def __init__(self, firstname="John", lastname="Doe", incomes=2000, extra_income=500, total_expense=1000):
        super().__init__(firstname, lastname, incomes)
        self.total_income = self.incomes + extra_income
        self.total_expense = total_expense
        self.account_info = self.total_income - self.total_expense
        self.passive_income = 0
        self.extra_expense = 0

    def add_income(self, income):
        self.passive_income += income

    def add_expense(self, expense):
        self.extra_expense += expense

    def account_balance(self):
        return (self.total_income + self.passive_income) - (self.total_expense + self.extra_expense)

    def person_info(self):
        return f"""First name: {self.firstname}\nLast name: {self.lastname}\nIncomes: {self.incomes}\nTotal Income: {self.total_income}\nPassive income: {self.passive_income}\nNew expenses: {self.extra_expense}\nAccount Balance: {self.account_balance()}
        """
    
    

    
# add_income, add_expense, account_balance

p1 = PersonAccount()
p2 = ExpensesProprietis("Bob", "Paris", 5000)
p2.add_income(200)
p2.add_expense(3000)
print(p2.person_info())