#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:51:27 2020

@author: Kishan
"""


## portion_down_payment = 0.25 (25%)
## current_savings begin at $0
## annual return on current_savings: r = 0.04
## monthly savings = (current_savings*r/12) + annual_salary/12

print("Your dream house costs $1M.")
total_cost_float=1000000
print("You will receive semi-annual raises of 7% at your job.")
semi_annual_raise_float=0.07
print("You currently have $0 in your savings.")
print("Once you earn savings through your job, you will invest them with a monthly return of 4%.")
annual_salary=input("What is your starting annual salary?")
annual_salary_float=float(annual_salary)
portion_down_payment = 0.25
r = 0.04
current_savings = 0
cost_down_payment = portion_down_payment*total_cost_float

# checking if 36 month down payment is possible with given salary
for t in range(0,36):
    current_savings = current_savings + current_savings*r/12
    current_savings = current_savings + (1*annual_salary_float/12)
    t += 1
    if t % 6 == 0:
        annual_salary_float = annual_salary_float + annual_salary_float*semi_annual_raise_float

if current_savings>cost_down_payment:
    current_savings=0
    annual_salary_float=float(annual_salary)
    
    low=0
    high=10000
    epsilon=100
    guess=(high+low)//2
    portion_saved_float=guess/10000
    n=1
    
    
    for t in range(0,36):
        current_savings = current_savings + current_savings*r/12
        current_savings = current_savings + (portion_saved_float*annual_salary_float/12)
        t += 1
        if t % 6 == 0:
            annual_salary_float = annual_salary_float + annual_salary_float*semi_annual_raise_float
    
    while abs(current_savings-cost_down_payment)>=100:
        if current_savings<cost_down_payment:
            low=guess
        else:
            high=guess
        guess=(high+low)//2
        portion_saved_float=guess/10000
        current_savings=0
        annual_salary_float=float(annual_salary)
        for t in range(0,36):
            current_savings = current_savings + current_savings*r/12
            current_savings = current_savings + (portion_saved_float*annual_salary_float/12)
            t += 1
            if t % 6 == 0:
                annual_salary_float = annual_salary_float + annual_salary_float*semi_annual_raise_float
        n+=1
        
    print("Best savings rate:", str(portion_saved_float*100)+"%")
    print("Steps in bisection search:", n)
    
else:
    print("It is not possible to pay for a down payment in three years.")
    
    
    
    
    
    