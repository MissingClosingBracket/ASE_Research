from audioop import mul
import pandas as pd

#Read the scraped data file
df = pd.read_csv('scrapedAuthorData1.csv')
occurrences = df.get('Occurrences')
interests = df.get("Interests").apply(eval)

assert len(occurrences) == len(interests)

lst = []

for x in range(0, len(occurrences)):
    multiplier = int(occurrences[x])
    listOfInterest = interests[x]
    if (len(listOfInterest) > 0):
        for interest in listOfInterest:
            lst += ([interest.lower()] * multiplier)

dfList = pd.DataFrame(lst)
dfList.to_csv('listOfInterests.csv', encoding='utf-8', index=False)
