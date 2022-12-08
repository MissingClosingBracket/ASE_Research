from scholarly import scholarly
from scholarly import ProxyGenerator
import json
import pandas as pd

#Use a proxy. Change key if needed by making an account on ScraperAPI
pg = ProxyGenerator()
success = pg.ScraperAPI("59ba60d7689da54ebce79b65b2379baa")
scholarly.use_proxy(pg)


#Get the relevant article
article = scholarly.search_single_pub("the five dysfunctions of a team, Lencioni 2006", True)

#Read the cited article
errCount = 0

test = [
    {
        'Type': data["container_type"] if "container_type" in data else "",
        'Title': data['bib']['title'] if "title" in data['bib'] else "",
        'Authors': data['bib']['author'] if "author" in data['bib'] else [],
        'Year': data['bib']['pub_year'] if "pub_year" in data['bib'] else "",
        'Venue': data['bib']['venue'] if "venue" in data['bib'] else "",
        'Abstract': data['bib']['abstract'] if "abstract" in data['bib'] else "",
        'Url': data['pub_url'] if "pub_url" in data else "",
        'Author_Ids': data['author_id'] if "author_id" in data else [],
        'Scholar_Url': data['url_scholarbib'] if 'url_scholarbib' in data else "",
        'Citations': data['num_citations'] if "num_citations" in data else -1,
    } 
    for data in scholarly.citedby(article)]

#Convert the list to csv
df = pd.DataFrame.from_dict(test)
df.to_csv('scrapedData3.csv', encoding='utf-8', index=False)



