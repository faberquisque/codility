def solution(S, C):
    # write your code in Python 3.6
    list_sep = '; '
    name_sep = ' '
    email_sep = '.'
    hyphen = '-'
    last_max_chars = 8
    at_company_com = '@' + C.lower() + '.com'
    
    names = S.split(list_sep)
    emails = {}
    
    for name in names:
        # Split first, middle and last name and lower case them
        splitted_name = name.split(name_sep)
        first = splitted_name[0].lower()
        last = splitted_name[-1].lower()
        # Remove the hyphens
        last = last.replace(hyphen,'')
        # Slice the first 8 characters
        last = last[:last_max_chars]
        # compose email
        email = first + email_sep + last + at_company_com
        # check availability. time ineficiency espected
        i = 1
        while email in emails:
            i += 1
            # compose new email 
            email = first + email_sep + last + str(i) + at_company_com
        # Add new email to list
        emails[email] = True
    
    return list_sep.join(emails.keys())
