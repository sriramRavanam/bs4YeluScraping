import json
from bs4 import BeautifulSoup
import requests

from utils import camelCase

main_url = 'https://yelu.in'

with open("data.json","r") as f:
    data = json.load(f)
    f.close()

company_data = []
idx = 0

for element in data["employment_companies"]:
    idx+=1

    if idx == 50:
        break
    elementJson = {}
    elementJson["name"] = element["name"]
    elementJson["url"] = main_url + element["link_path"]
    elementJson["seoPath"] = element["link_path"]

    request = requests.get(elementJson["url"])
    elementSoup = BeautifulSoup(request.content, 'lxml')

    info = elementSoup.findAll('div', {'class': 'info'})


    



    # print(elementJson)


    # once for all div 
    for i in info:
        sub = i.find('div', {'class': 'label'})
        # nextSibling  = sub.find_next_siblings('div')
        # print(nextSibling[0].text)
        # print(sub) 

        

        if sub is not None:

            

            if sub.text == "Keywords":
                aList = sub.findNext('div').find_all('a')
                
                elementJson["keywords"] = [a.text for a in aList]
                # elementJson["keywords"] = aList.split(' ')
            
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

                    elementJson["working_hours"] = days
                    

            elif sub.text == "Listed in categories":
                catList  = sub.findNext('div').find_all('a')
                # print(catList)
                # elementJson[camelCase(sub.text)] = catList
                elementJson[camelCase(sub.text)] = [a.text for a in catList]

            else:
                elementJson[camelCase(sub.text)] = sub.findNext('div').text
            
        # if sub is not None:
        #     next = sub.findNext('div')
        # print("________________________________________________________________________________________________________")
    # 

    # for spans in info
    for i in info:
        sub = i.find('span', {'class': 'label'})

        if sub is not None:
            # print(sub.text)

            if sub.text == "Working hours":
                # # print(camelCase(sub.text))
                # parent = sub.findParent()
                # hours = parent.contents[3].text
                # elementJson["workingTimings"] = hours
                continue

            if(sub.text == "Share this listing"):
                continue

            if sub.text == "Company manager":
                # print(camelCase(sub.text))
                parent = sub.findParent()
                # print(parent.contents[1].text)
                elementJson[camelCase(sub.text)] = parent.contents[1].text

            else :
                # print(camelCase(sub.text))
                # # print(sub.findNext().contents[1].text)
                # print(sub.findNext().text)
                elementJson[camelCase(sub.text)] = sub.findNext().text

    print("company {} done".format(idx))
    company_data.append(elementJson)

print(str(len(company_data)) + " companies scraped")        

with open('test/test.json','w') as f:
    # dont use indent for actual cases, beneficial if on a single line
    json.dump(company_data, f)
    f.close()


