example_answers_by_dates = { '2024-10-16' : 'yes', '2024-10-17' : 'yes', '2024-10-18' : 'no', '2024-10-19' : 'yes' }

for k, v in example_answers_by_dates.items():
    print(k, v)

answers_only = [ v for v in example_answers_by_dates.values() ]
print(answers_only)

streak_value = 0

for p, n in zip(answers_only, answers_only[ 1 : ] ) :
    if p == n :
        streak_value += 1
    else :
        if n == 'yes' :
            streak_value = 1
        else :
            streak_value = 0
    
    print(p, n, "Current streak value:", streak_value)