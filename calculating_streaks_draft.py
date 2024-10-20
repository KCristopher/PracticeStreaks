example_answers_by_dates = { '2024-10-16' : 'yes', '2024-10-17' : 'yes', '2024-10-18' : 'no', '2024-10-19' : 'yes', '2024-10-20' : 'yes', '2024-10-21' : 'no'  }

for k, v in example_answers_by_dates.items():
    pass
    #print(k, v)

answers_only = [ v for v in example_answers_by_dates.values() ]
#print(answers_only)

streak_value = 0

for p, n in zip(answers_only, answers_only[ 1 : ] ) :
    if p == n :
        streak_value += 1
    else :
        if n == 'yes' :
            streak_value = 1
        else :
            streak_value = 0
    
    #print(p, n, "Current streak value:", streak_value)


def calc_fixed_interval_streak_value(usr_answers_by_dates, step = 1, flexible_interval = True ) :
    
    answers_only = [ v for v in usr_answers_by_dates.values() ]
    streak_value = 0

    if ( len(answers_only) == 1 ) and (step == 1) and (answers_only[0] == 'yes') :
        return 1
    
    elif len(answers_only) == 0 :
        return 0

        

    for p, n in zip(answers_only[ 0 : : step ], answers_only[ 1 :  ] [ 0 : : step ] ) :

        if p == n :
            streak_value += 1
        else :
            if ( flexible_interval ) and ( [ p, n ].count('yes') >= step ) :
                streak_value += 1
            elif n == 'yes' :
                streak_value = 1
            else :
                streak_value = 0   

    return streak_value


#print(calc_fixed_interval_streak_value(example_answers_by_dates, 2))




print(calc_flexible_interval_streak_value(example_answers_by_dates, 7))

