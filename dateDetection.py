# Detects dates using regular expressions.
#TODO: Use pyperclip to paste dates from the clipboard instead of using dateString and copy to clipboard after. Turn into a batch file. 

import re

monthDict = {'01': 'JAN',
             '02': 'FEB',
             '03': 'MAR',
             '04': 'APR',
             '05': 'MAY',
             '06': 'JUN',
             '07': 'JUL',
             '08': 'AUG',
             '09': 'SEP',
             '10': 'OCT',
             '11': 'NOV',
             '12': 'DEV'}

dateString = '''It was a bright and sunny day on 12-02-2022, the kind that makes everyone feel like going out
 for a walk. Sarah had a dentist appointment scheduled for 32_11_2024, which she dreaded. She was reminded of 
 how, on 22/08/2019, she had forgotten an appointment and ended up with a hefty fine. Luckily, her brother's 
 wedding on 03/13/2020 had gone smoothly despite the heavy rain that morning. Looking back, Sarah couldn't 
 believe how fast time had passed since her trip to Paris on 14 04 2017. She still remembered the cherry 
 blossoms blooming near the Eiffel Tower. 29/02/2001 29/02/2000 30/02/2000'''

# Regex pattern for finding dates.
dateRegex = re.compile(r'''
                       ((\d{2})     # Days
                       .            # Any separator
                       (\d{2})      # Months
                       .            # Any separator
                       (\d{4})      # Years
                       )''', re.VERBOSE)

matches = []
formattedMatches = []
for groups in dateRegex.findall(dateString):
    matches.append(groups)

for date in matches:
    validDate = None
    if date[2] in ['04', '06', '09', '11'] and int(date[1]) <= 30:
        day, month, year = date[1], date[2], date[3]
        validDate = True
    
    # Leap year Feb check
    elif date[2] == '02' and int(date[3]) % 4 == 0 and int(date[1]) <= 29:
        day, month, year = date[1], date[2], date[3]
        validDate = True

    # Non leap year Feb check
    elif date[2] == '02' and int(date[1]) <= 28:
        day, month, year = date[1], date[2], date[3]
        validDate = True

    elif date[2] in ['01', '03', '05', '07', '08', '12'] and int(date[1])<= 31:
        day, month, year = date[1], date[2], date[3]
        validDate = True

    else:
        day, month, year = date[1], date[2], date[3]
        validDate = False

    if validDate:
        newDate = f'{day}-{monthDict[month]}-{year}'
        formattedMatches.append(newDate)
    else:
        print(f'{day}-{month}-{year} is NOT a valid date.')
    

print('\n'.join(formattedMatches))
