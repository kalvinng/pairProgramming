import pandas as pd

def calculateTax(income):
    if income <= 85200:
        individual_mpf = 0
    elif income <= 360000:
        individual_mpf = income * 0.05
    else:
        individual_mpf = 18000

    net_income = income - individual_mpf - 132000

    if net_income < 0:
        net_income = 0

    tax = 0
    standard_tax = (income - individual_mpf) * 0.15
    if net_income <= 50000:
        tax = net_income * .02
    elif net_income <= 100000:
        tax = 1000 + .06 * (net_income - 50000)
    elif net_income <= 150000:
        tax = 4000 + .10 * (net_income - 100000)
    elif net_income <= 200000:
        tax = 9000 + .14 * (net_income - 150000)
    else:
        tax = 16000 + .17 * (net_income - 200000)

    if tax < standard_tax:
        tax = round(tax)
    else:
        tax = round(standard_tax)

    return [tax]
data = pd.DataFrame()
for x in range(0,2000100,10000):
    [tax]=calculateTax(x)
    data = data.append([[x,tax]],ignore_index=True)
print(data)
data.to_excel('singleData.xlsx', sheet_name='sheet1', index=False)
