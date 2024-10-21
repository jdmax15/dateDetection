# Detects dates using regular expressions.

import re

dateString = '''It was a bright and sunny day on 12/05/2022, the kind that makes everyone feel like going out
 for a walk. Sarah had a dentist appointment scheduled for 07/11/2024, which she dreaded. She was reminded of 
 how, on 22/08/2019, she had forgotten an appointment and ended up with a hefty fine. Luckily, her brother's 
 wedding on 03/09/2020 had gone smoothly despite the heavy rain that morning. Looking back, Sarah couldn't 
 believe how fast time had passed since her trip to Paris on 14/04/2017. She still remembered the cherry 
 blossoms blooming near the Eiffel Tower.'''

# Regex pattern for finding dates.
dateRegex = re.compile(r'((\d{2})\/(\d{2})\/(\d{4}))')

matches = []
for groups in dateRegex.findall(dateString):
    matches.append(groups)

for date in matches:
    day = date[1]
    month = date[2]
    year = date[3]
    print(f"day: {day}\nmonth: {month}\nyear: {year}\n")
