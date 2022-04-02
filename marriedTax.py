husband_income = int(input("Please enter husband's total income: $"))
wife_income = int(input("Please enter wife's total income: $"))
total_income = round(husband_income + wife_income)

if husband_income <= 85200:
    husband_mpf=0
elif husband_income <= 360000:
    husband_mpf=husband_income*0.05
else:
    husband_mpf=18000

if wife_income <= 85200:
    wife_mpf=0
elif wife_income <= 360000:
    wife_mpf=wife_income*0.05
else:
    wife_mpf=18000

husband_net_income = husband_income - husband_mpf - 132000
wife_net_income = wife_income - wife_mpf - 132000
total_net_income = husband_net_income + wife_net_income

if husband_net_income < 0:
    husband_net_income = 0

husband_tax = 0
husband_standard_tax=(husband_income - husband_mpf) * 0.15
if husband_net_income <= 50000:
    husband_tax = husband_net_income * .02
elif husband_net_income <= 100000:
    husband_tax = 1000 + .06 * (husband_net_income - 50000)
elif husband_net_income <= 150000:
    husband_tax = 4000 + .10 * (husband_net_income - 100000)
elif husband_net_income <= 200000:
    husband_tax = 9000 + .14 * (husband_net_income - 150000)
else:
    husband_tax = 16000 + .17 * (husband_net_income - 200000)

if husband_tax < husband_standard_tax:
    husband_tax = husband_tax
else:
    husband_tax = husband_standard_tax

if wife_net_income < 0:
    wife_net_income = 0

wife_tax = 0
wife_standard_tax=(wife_income - wife_mpf) * 0.15
if wife_net_income <= 50000:
    wife_tax = wife_net_income * .02
elif wife_net_income <= 100000:
    wife_tax = 1000 + .06 * (wife_net_income - 50000)
elif wife_net_income <= 150000:
    wife_tax = 4000 + .10 * (wife_net_income - 100000)
elif wife_net_income <= 200000:
    wife_tax = 9000 + .14 * (wife_net_income - 150000)
else:
    wife_tax = 16000 + .17 * (wife_net_income - 200000)

if wife_tax < wife_standard_tax:
    wife_tax = wife_tax
else:
    wife_tax = wife_standard_tax

if total_net_income < 0:
    total_net_income = 0

total_tax = 0
total_standard_tax = (total_income - husband_mpf - wife_mpf) * 0.15
if total_net_income <= 50000:
    total_tax = total_net_income * .02
elif total_net_income <= 100000:
    total_tax = 1000 + .06 * (total_net_income - 50000)
elif total_net_income <= 150000:
    total_tax = 4000 + .10 * (total_net_income - 100000)
elif total_net_income <= 200000:
    total_tax = 9000 + .14 * (total_net_income - 150000)
else:
    total_tax = 16000 + .17 * (total_net_income - 200000)

if total_tax < total_standard_tax:
    total_tax = total_tax
else:
    total_tax = total_standard_tax

standard_tax=(husband_income - husband_mpf) + (wife_income - wife_mpf) * 0.15

husband_mpf = round(husband_mpf)
wife_mpf = round(wife_mpf)

husband_tax = round(husband_tax)
wife_tax = round(wife_tax)

total_tax = round(total_tax)

print(f"The husband MPF is ${husband_mpf}.")
print(f"The wife MPF is ${wife_mpf}.")

print(f"The husband tax is ${husband_tax}.")
print(f"The wife tax is ${wife_tax}.")

total_separate_tax = round(husband_tax + wife_tax)
print (f"The total tax payable under Separate Taxation is ${total_separate_tax}.")

print(f"The total tax payable under Joint Assessment is ${total_tax}.")

if total_separate_tax < total_tax:
    print("Separate Taxation is better.")
elif total_separate_tax > total_tax:
    print("Joint Assessment is better.")
