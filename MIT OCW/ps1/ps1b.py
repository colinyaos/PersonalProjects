annual_salary = float(input("Annual salary:"))
portion_saved = float(input("Portion saved:"))
tot_cost = float(input("Total home cost:"))
semi_annual_raise = float(input("Semi-annual raise:"))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

monthly_salary = annual_salary / 12

months_saving = 0
while current_savings < (tot_cost * portion_down_payment):
    current_savings *= (1 + r/12)
    current_savings += monthly_salary * portion_saved
    months_saving += 1
    if months_saving%6 == 0:
        annual_salary *= (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12

print("Months saved:", months_saving)