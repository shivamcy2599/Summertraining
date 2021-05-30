target=float(input("Enter Years of Experience:"))

import pandas as pd
dataset = pd.read_csv("SalaryData.csv")
y = dataset["Salary"]
x = dataset["YearsExperience"]


from sklearn.linear_model import LinearRegression

model = LinearRegression()

x = x.values

x = x.reshape(30,1)

model.fit(x,y)

output = model.predict([[target]])

print(output)
