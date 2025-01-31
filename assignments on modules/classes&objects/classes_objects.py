#Exercises: Level 1
class Statistics:
    def __init__(self, ages):
        self.ages = ages
    def mean(self):
        return sum(self.ages)/ len(self.ages)
    def median(self):
        n= len(self.ages)
        self.ages.sort()
        if n%2==0:
            return (self.ages[n//2]+self.ages[n//2-1])/2
        else:
            return self.ages[n//2]
    def mode(self):
        d ={}
        for i in self.ages:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                max_val=max(d.values())
                mode=[k for k,v in d.items() if v==max_val]
                return mode
    def range(self):
        return max(self.ages)-min(self.ages)
    def var(self):
        n=len(self.ages)
        mean= sum(self.ages)/n
        return sum((x-mean)**2 for x in self.ages)/n
    def std(self):
        return self.var()**0.5
    def min(self):
        return min(self.ages)
    def max(self):
        return max(self.ages)
    def count(self):
        return len(self.ages)
    def percentile(self,percent):
        n=len(self.ages)
        self.ages.sort()
        return self.ages[int(n*percent/100)]
    def freq_dist(self):
        d={}
        for i in self.ages:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                return d
    def sum(self):
        return sum(self.ages)
    def describe(self):
        print('Count:', self.count())
        print('Sum:', self.sum())
        print('Min:', self.min())
        print('Max:', self.max())
        print('Range:', self.range())
        print('Mean:', self.mean())
        print('Median:', self.median())
        print('Mode:', self.mode())
        print('Variance:', self.var())
        print('Standard Deviation:', self.std())
        print('Frequency Distribution:', self.freq_dist())
res=Statistics([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
)
print(res.describe())
#Exercises: Level 2
class PersonAccount:
    def __init__(self, first_name, last_name):
        self.first_name= first_name
        self.last_name= last_name
        self.income=[]
        self.expenses=[]
    def add_income(self,description,amount):
        self.income.append((description, amount))
    def add_expenses(self,description,amount):
        self.expenses.append((description, amount))
    def total_income(self):
        return sum(amount for _, amount in self.income)
    def total_expenses(self):
        return sum(amount for _, amount in self.expenses)
    def account_balance(self):
        return self.total_income()-self.total_expenses()
    def account_info(self):
        return f'{self.first_name} {self.last_name} {self.total_income()} {self.total_expenses()} {self.account_balance()}'
sample= PersonAccount('Li', 'Ban')
sample.add_income('salary', 120000)
sample.add_income('stipend', 25000)
sample.add_expenses('food',27000)
sample.add_expenses('transport',1023)
print(sample.account_info())

    
    