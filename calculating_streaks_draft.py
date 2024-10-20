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


def calc_streak_value(usr_answers_by_dates, step = 1, flexible_interval = True ) :

    """ 
    Given a dict whose keys are dates and values are 'yes'/'no' answers
    calculates the user's streak of 'yes' answers.
    
    Parameters
    ----------
    usr_answers_by_dates : dict. 
        A dictionary of user's answers by dates.
    step : int. 
        The number of days between each answer. Should be at least 1.
    flexible_interval : bool. 
        If True, the streak will continue if the user performs the activity at least once in the interval of {step} days.
        If False, the streak will only continue if the user performs the activity exactly every {step} days.
    
    Returns
    -------
    int. The streak value of the user's answers.

    Notes
    -----
    The function is meant to calculate the practie streak of a single user,
    where each day the user is asked whether he/she performed the activity or not. 
    The 'yes'/'no' answered is then stored in a dictionary with the date as the key.
    The function expects this data to be provided via the usr_answers_by_dates parameter.

    Please be noted that the function will return 0 if the user has not answered questions yet.
    The user will have the option to answer about the dates in the past since the last logg in.

    Examples
    --------
    >>> example_answers_by_dates = { '2024-10-16' : 'yes', '2024-10-17' : 'yes', '2024-10-18' : 'no', '2024-10-19' : 'yes', '2024-10-20' : 'yes', '2024-10-21' : 'no'  }
    
    >>> print( calc_streak_value(example_answers_by_dates, 2, flexible_interval = False) )
        
        0
    
    >>> print( calc_streak_value(example_answers_by_dates, 2, flexible_interval = True) )
        
        3
    >>> print( calc_streak_value(example_answers_by_dates, 3, flexible_interval = True) )

        2
    """

    
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
            if ( flexible_interval ) and ( [ p, n ].count('yes') >= 1 ) :
                streak_value += 1
            elif n == 'yes' :
                streak_value = 1
            else :
                streak_value = 0   
        print(p, n, "Current streak value:", streak_value)

    return streak_value







example_answers_by_dates = { '2024-10-16' : 'yes', '2024-10-17' : 'yes', '2024-10-18' : 'no', '2024-10-19' : 'yes', '2024-10-20' : 'yes', '2024-10-21' : 'no'  }

print( calc_streak_value(example_answers_by_dates, 3, flexible_interval = True) )