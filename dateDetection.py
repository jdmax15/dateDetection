# Detects dates using regular expressions.
#TODO: Use pyperclip to paste dates from the clipboard instead of using dateString and copy to clipboard after. Turn into a batch file. 

import re, pyperclip

dateString = pyperclip.paste()

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

    # Any numbers 0 or less check
    if int(date[1]) <= 00 or int(date[2]) <= 00 or int(date[3]) <= 0000:
        validDate = False

    elif date[2] in ['04', '06', '09', '11'] and int(date[1]) <= 30:
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
        newDate = f'{day}-{month}-{year}'
        formattedMatches.append(newDate)
    else:
        print(f'{day}-{month}-{year} is NOT a valid date.')
    

formattedMatches = '\n'.join(formattedMatches)

print(formattedMatches)

pyperclip.copy(formattedMatches)



