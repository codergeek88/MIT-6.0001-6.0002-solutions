#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:45:49 2020

@author: Kishan
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:39:29 2020

@author: Kishan
"""

## portion_down_payment = 0.25 (25%)
## current_savings begin at $0
## annual return on current_savings: r = 0.04
## monthly savings = (current_savings*r/12) + annual_salary/12

total_cost=input("What is the cost of your dream home? (The down payment will be 25%.)")
total_cost_float=float(total_cost)
annual_salary=input("What is your annual salary?")
annual_salary_float=float(annual_salary)
semi_annual_raise=input("You will receive a raise every six months. What percentage will that raise be? (please enter in decimal form)")
semi_annual_raise_float=float(semi_annual_raise)
print("You currently have $0 in your savings.")
print("Once you earn savings through your job, you will invest them with a monthly return of 4%.")
portion_saved=input("What percentage of your annual salary would you like to set aside for savings? (please enter in decimal form)")
portion_saved_float=float(portion_saved)
portion_down_payment = 0.25
r = 0.04
t = 0
current_savings = 0
while current_savings < total_cost_float*portion_down_payment:
    current_savings = current_savings + current_savings*r/12
    current_savings = current_savings + (portion_saved_float*annual_salary_float/12)
    t += 1
    if t % 6 == 0:
        annual_salary_float = annual_salary_float + annual_salary_float*semi_annual_raise_float
if t >=12:
    print("It will take you", t, "months (" + str(t//12), "years", str(t%12), "months) to earn enough money to purchase a down payment on your dream house.")
else:print("It will take you", t, "months to earn enough money to purchase a down payment on your dream house.")















