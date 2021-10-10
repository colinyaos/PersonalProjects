semi_annual_raise = 0.07
r = 0.04
down_proportion = 0.25
total_cost = 1000000
months_to_save = 36

down_payment = down_proportion * total_cost

annual_salary = float(input("Starting salary:"))
monthly_salary = annual_salary / 12

saving_rate_guess = 5000 #we'll need to cast between int / float later
previous_guess_low = 0
previous_guess_high = 10000
found_best_rate = False

temp_annual_salary = annual_salary

steps_search = 0
while found_best_rate == False:

    temp_annual_salary = annual_salary
    monthly_salary = annual_salary / 12
    amount_saved = 0

    for i in range(months_to_save):
        amount_saved *= (1 + r/12)
        amount_saved += monthly_salary * (saving_rate_guess / 10000)
        if i%6 == 5:
            temp_annual_salary *= (1 + semi_annual_raise)
            monthly_salary = temp_annual_salary / 12
        #print(i+1, amount_saved)
    #print()
    
    #print(previous_guess_low, saving_rate_guess, previous_guess_high, amount_saved, steps_search)

    if amount_saved < down_payment:
        previous_guess_low = saving_rate_guess
        saving_rate_guess = int(0.5 * (saving_rate_guess + previous_guess_high + 1))
        if saving_rate_guess == previous_guess_low or saving_rate_guess == previous_guess_high:
            found_best_rate = True
    elif amount_saved > down_payment:
        previous_guess_high = saving_rate_guess
        saving_rate_guess = int(0.5 * (saving_rate_guess + previous_guess_low))
        if saving_rate_guess == previous_guess_high or saving_rate_guess == previous_guess_low:
            found_best_rate = True
    else:
        found_best_rate = True
    steps_search += 1

    if previous_guess_low == previous_guess_high - 1:
        low_saved = 0
        high_saved = 0
        temp_temp_annual_salary = annual_salary
        temp_monthly_salary = temp_temp_annual_salary / 12

        for i in range(months_to_save):
            high_saved *= (1 + r/12)
            high_saved += temp_monthly_salary * (previous_guess_high / 10000)
            low_saved *= (1 + r/12)
            low_saved += temp_monthly_salary * (previous_guess_low / 10000)
            if i%6 == 5:
                temp_temp_annual_salary *= (1 + semi_annual_raise)
                temp_monthly_salary = temp_temp_annual_salary / 12
        
        if abs(down_payment - low_saved) > abs(down_payment - high_saved):
            saving_rate_guess = previous_guess_high
            break
        else:
            saving_rate_guess = previous_guess_low
            break    

if saving_rate_guess == 10000:
    found_best_rate = False

if found_best_rate == True:
    print("Optimum savings rate:", saving_rate_guess / 10000)
else:
    print("Not possible with this salary.")
print("Steps in search:", steps_search)
        