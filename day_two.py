print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill? $'))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
people_split = int(input('How many people to split the bill? '))
splited_total = total_bill * (tip_percentage/100 + 1) / people_split
print(f'Each person should pay: ${round(splited_total, 2)}')
