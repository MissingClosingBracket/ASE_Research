from optparse import OptionConflictError
from scholarly import scholarly
from scholarly import ProxyGenerator
import json
import pandas as pd

#Read the scraped data file
df = pd.read_csv('scrapedData3.csv')

#The author list should be parsed as list of strings
authorIds = df.get('Author_Ids').apply(eval)

#For each row, read the authors and write to a map that counts occurrences for each author
occurrenceMap = dict()
for row in authorIds:
    for id in row:
        if id != "":
            if (occurrenceMap.get(id) == None):
                occurrenceMap[id] = 1
            else:
                occurrenceMap[id] = occurrenceMap.get(id) + 1    

#Now map each author id to the areas of interest scraped from Scholar
#Use a proxy. Change key if needed by making an account on ScraperAPI
pg = ProxyGenerator()
success = pg.ScraperAPI("59ba60d7689da54ebce79b65b2379baa")
#pg.FreeProxies()
scholarly.use_proxy(pg)

#Loop through collection and create another map
interestMap = dict()
for author in occurrenceMap:
    print(author)
    authObject = scholarly.search_author_id(author)
    interestMap[author] = {'name': authObject["name"] if "name" in authObject else '', 'interests': authObject["interests"] if "interests" in authObject else []}

#Now make new dict that combines all data: id:str, name:str, interests:[]
collectedData = list()
assert len(occurrenceMap) == len(interestMap)

for author in occurrenceMap:
    collectedData.append({'Id':author, 'Name': interestMap.get(author)['name'], 'Occurrences':occurrenceMap.get(author), 'Interests': interestMap.get(author)['interests']})

#Convert the list to csv
dfCollectedData = pd.DataFrame.from_dict(collectedData)
dfCollectedData.to_csv('scrapedAuthorData1.csv', encoding='utf-8', index=False)