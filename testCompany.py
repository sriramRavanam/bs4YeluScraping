from bs4 import BeautifulSoup
import requests
import json

from utils import camelCase


elementJSon = {}

url = "https://www.yelu.in/company/940975/alliance-international"

src = requests.get(url).text
soup = BeautifulSoup(src, 'lxml')

info = soup.findAll('div', {'class': 'info'})


elementJSon["url"] = url



# print(elementJSon)

for i in info:
    sub = i.find('div', {'class': 'label'})
    # nextSibling  = sub.find_next_siblings('div')
    # print(nextSibling[0].text)
    # print(sub) 

    

    if sub is not None:

        

        if sub.text == "Keywords":
            aList = sub.findNext('div').find_all('a')
            
            elementJSon["keywords"] = [a.text for a in aList]
            # elementJSon["keywords"] = aList.split(' ')
        
        elif sub.text == "Working hours":
            next = sub.findNext('div')
            # this div has a table
            table = next.find('table')
            # print(table)
            if table is not None:    
                # tbody = table.find('tbody')
                tr = table.find_all('tr')

                days = {}
                for row in tr:
                    day = row.find_all('td')
                    days[day[0].text] = day[1].text

                elementJSon["working_hours"] = days
                

        elif sub.text == "Listed in categories":
            catList  = sub.findNext('div').find_all('a')
            # print(catList)
            # elementJSon[camelCase(sub.text)] = catList
            elementJSon[camelCase(sub.text)] = [a.text for a in catList]

        else:
            elementJSon[camelCase(sub.text)] = sub.findNext('div').text
        
    # if sub is not None:
    #     next = sub.findNext('div')
    # print("________________________________________________________________________________________________________")
# 


for i in info:
    sub = i.find('span', {'class': 'label'})

    if sub is not None:
        # print(sub.text)

        if sub.text == "Working hours":
            # # print(camelCase(sub.text))
            # parent = sub.findParent()
            # hours = parent.contents[3].text
            # elementJSon["workingTimings"] = hours
            continue

        if(sub.text == "Share this listing"):
            continue

        if sub.text == "Company manager":
            # print(camelCase(sub.text))
            parent = sub.findParent()
            # print(parent.contents[1].text)
            elementJSon[camelCase(sub.text)] = parent.contents[1].text

        else :
            # print(camelCase(sub.text))
            # # print(sub.findNext().contents[1].text)
            # print(sub.findNext().text)
            elementJSon[camelCase(sub.text)] = sub.findNext().text

        

# with open('test/test.json','w') as f:
#     # dont use indent for actual cases, beneficial if on a single line
#     json.dump(elementJSon, f, indent=4)
#     f.close()