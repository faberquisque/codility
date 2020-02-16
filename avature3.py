def solution(S):
    # write your code in Python 3.6
    # Definitions
    log_sep = ','
    num_sep = '-'
    time_sep = ':'
    # Initialization
    from collections import defaultdict
    # defaultdict initialize missing key to default value -> 0
    bill = defaultdict(int)
    total = defaultdict(int)
    calls = S.splitlines()
    maximal = 0
    free_number = 0
    
    for call in calls:
        # Parsing values
        hhmmss, number = call.split(log_sep)
        hh, mm, ss = hhmmss.split(time_sep)
        hh, mm, ss = int(hh), int(mm), int(ss)
        number = int(number.replace(num_sep,''))
        # Call duration calculations
        minutes = mm + hh * 60
        seconds = ss + minutes * 60
        # Free number Rule
        total[number] += seconds
        if total[number] > maximal:
            # new maximal
            maximal = total[number]
            free_number = number
        elif total[number] == maximal:
            # in case of a tie...
            free_number = min(number,free_number)
        # Billing Rule
        if minutes < 5:
            bill[number] += seconds * 3
        else:
            if ss > 0:
                started = 1
            else:
                started = 0
            bill[number] += (minutes + started) * 150
    # Free number Rule enforcement
    bill[free_number] = 0
    return sum(bill.values())
