# Lists, Tuples, Dictionaries,NumPy, Pandas, loops, if-else, and DataFrames.
# Student_Marks
marks=[78,45,89,92,67,34,55,80,99,60]

len(marks)

sum(marks)

# Highest Mark
highest = marks[0]

for i in marks:
    if i > highest:
        highest = i

print(highest)

# Lowest mark
lowest = marks[0]

for i in marks:
    if i < lowest:
        lowest = i

print(lowest)

# Average without mean 
mean = sum(marks)/len(marks)
mean

# even marks
for i in marks:
    if i % 2 == 0:
        print(i)

# odd marks
for i in marks:
    if i % 2 != 0:
        print(i)

# Summary 
summary = {
    "A+":0,
    "A":0,
    "B+":0,
    "B":0,
    "C":0,
    "Fail":0
}

for i in marks:
    if i >= 90:
        grade ="A+"
    elif i >= 80 :
        grade ="A"
    elif i >= 70 :
        grade = "B+"
    elif i >= 60:
        grade = "B"
    elif i >= 50 :
        grade = "C"
    else :
        grade = "Fail"
    print(f"Mark:{i},Grade:{grade}")
    summary[grade] += 1

# Grade Summary
print("Grade summary")
print(f"Total_Students:{len(marks)}")
print(f"A+: {summary['A+']}")
print(f"B+: {summary['B+']}")
print(f"B:  {summary['B']}")
print(f"C:  {summary['C']}")
print(f"Fail:{summary['Fail']}")

# Print's Marks Greater than 75
count = 0

for i in marks:
    if i > 75:
        count += 1
        print("\nMarks:",count,i)

# Passed Student's Count
count = 0

for i in marks:
    if i >= 35:
        count += 1
        print("\nPassed students:",count,i)

# Distinction Student's Count
count = 0

for i in marks:
    if i >= 75:
        count += 1
        print("\nDistinction:",count,i)

# Employee Salary
salary = [25000,40000,55000,32000,61000,48000]

len(salary)

# Salary Above 50000
for i in salary:
    if i > 50000:
        print(i)

# Salary Below 40000 Count
for i in salary:
    if i < 40000:
        print(i)

# 10% increment on Salary
for i in range(len(salary)):
    salary[i] = salary[i] + (salary[i] * 10 / 100)

print(salary)

# Sum of salary
total = sum(salary)

# Average Salary
average = sum(salary)/len(salary)

# Second Highesy Salary
second_highest = sorted(salary, reverse=True)[1]

# Five Percent tax on Salary
tax = [tax*5/100 for tax in salary]
print(tax)

# Patient Dictionary
patient = {'P101':{'Age':45,'Disease':'Diabetes'},
           'P102':{'Age':62,'Disease':'Cancer'},
           'P103':{'Age':28,'Disease':'Asthma'},
           'P104':{'Age':70,'Disease':'Diabetes'},
           'P105':{'Age':35,'Disease':'Cancer'}}

# Patient ID's List
print("Patient ID's:",list(patient.keys()))

# Patient Disease List
diseases = [det['Disease'] for det in patient.values()]
print("Diseases:", diseases)

# Total Patient Count
print("Total Patients:",len(patient))

# Age above 50
age_above_50 = {pid: details for pid, details in patient.items() if details['Age'] > 50}
print("Age > 50:", age_above_50)

# Oldest patient Detail
oldest = max(patient, key=lambda x: patient[x]['Age'])
print("Oldest Patient ID:", oldest)
print("Details:", patient[oldest])

# Adding new patient to Dictionary 
patient['P106'] = {'AGE':50,'Disease':'Heart Disease'}
print(patient)

# Updating Patient Record
patient['P104']['Disease']='Asthama'

# Removing Patient
del patient['P104']

# Tuples
cities =('Hyderabad','Bangalore','Chennai','Pune','Delhi')

# First city in Tuple
cities[0]

# Last city in Tuple
cities[-1]

# Loop in Cities
for i in cities:
    print(i)

# Length of cities
len(cities)

# if-else to search City
search = 'Hyderabad'

if search in cities:
    print("Found")
else:
    print("Not Found")

# startswith Method
for i in cities:
    if i.startswith("H"):
        print(i)

# Tuple to List  
cities = list(cities)
print(cities)

# Reversed List
cities[::-1]

# Reversed tuple
tuple(reversed(cities))

# Alternate Values
cities[::2]

for i in range(0, len(cities), 2):
    print(cities[i])

# Shopping Dictionary
Products={
     'Laptop':65000,
     'Mobile':25000,
     'Watch':3500,
     'Headphones':2000,
     'Keyboard':1500
}

# Expensive Item in Products
Expensive = max(Products,key=Products.get)
print(Products[Expensive])

# Cheapest Item in Products
cheapest = min(Products,key=Products.get)
print(Products[cheapest])

# Discount 
for item in Products:
    Products[item] = Products[item] * 0.9
    
print(Products)

# Updating Price 
Products['Laptop']=[66000]

# Adding Product
Products['Powerbank']=[5000]

# Removing Products
del Products['Powerbank']

# import Numpy
import numpy as np

# array
arr = np.array([67,89,45,90,56,77,88,92,61,35])

# Mean of array
np.mean(arr)

# Median of array
np.median(arr)

# Standard Deviation of array
np.std(arr)

# Variance of array
np.var(arr)

# Filtering array Greater than 80
filtered =arr[arr>80]

# Adding bonus
bonus = 5
new_arr = arr + bonus

print(new_arr)

# maximum in array
max(arr)

# minimum in array
min(arr)

# Replacing value in array
arr[arr==67] = 68

# numpy matrix
# (Jan, Feb, Mar)
sales = np.array([
    [100, 120, 130],
    [150, 140, 160],
    [200, 180, 210],
    [170, 190, 180]
])

# Sum of sales
np.sum(sales)

# sales Monthly sum
np.sum(sales,axis=0)

# sales total
np.sum(sales,axis=1)

# maximum sales
np.max(sales)

# minimum sales
np.min(sales)

# 20% increase in March
sale = sales[:,2]*1.20

# Filtering January Column
sales[:,0]

#Pandas Employee
import pandas as pd

# Pandas Dataframe 
Emp = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 28, 35, 26],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [40000, 55000, 50000, 60000, 45000]
})

print(Emp)

# head 
Emp.head()

# tail
Emp.tail()

# Selecting Columns
Emp[["Name","Department"]]

# Filtering Salary
Emp[Emp["Salary"]>50000]

# Filtering IT Employees
Emp[Emp["Department"]=="IT"]

# Average of salary
Emp["Salary"].mean()

# maximum salary 
Emp["Salary"].max()

# minimum salary
Emp["Salary"].min()

# Sorting age 
Emp["Age"].sort_values()

# Adding bonus Column
Bonus = Emp["Salary"]*0.10
Bonus

# Dropping the age column
emp = Emp.drop(columns=["Age"])

# Renaming Department
emp = Emp.rename(columns={"Department":"Dept"})

# Sales Analysis
Sale = pd.DataFrame({
    "Product": ["Laptop", "Mobile", "Laptop", "Tablet", "Mobile", "Tablet"],
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai", "Delhi"],
    "Sales": [50000, 30000, 45000, 25000, 35000, 20000]
})

# Total sales
Sale["Sales"].sum()

# City-wise sales Total
Sale.groupby("City")["Sales"].sum()

# Product-wise sales Total
Sale.groupby("Product")["Sales"].sum()

# Average Sales
Sale["Sales"].mean()

# sorting of sales
Sale["Sales"].sort_values()

#Hospital Analysis
Pat = pd.DataFrame({
    "Patient": ["Amit", "Riya", "John", "Sara", "Kiran"],
    "Age": [25, 40, 35, 60, 50],
    "Disease": ["Fever", "Diabetes", "Fever", "Cancer", "Diabetes"],
    "Bill": [5000, 15000, 7000, 30000, 12000]
})

# Patient count
Pat["Patient"].count()

# Average age
Pat["Age"].mean()

# Disease counts
Pat["Disease"].count()

# Aggregation of Patient
Pat["Bill"].agg([
    "sum","mean","max","min"
])

# Groupby to find total bill of patient
Pat.groupby("Patient")["Bill"].sum()

# Adding Age_Group Column in Patient
Pat["Age_Group"]=["Young" if age < 40 else "Senior" for age in Pat["Age"]]

# Exporting to csv
Pat.to_csv("Hospital.csv",index=False)

