from bs4 import BeautifulSoup
import requests
import json

main_url = 'https://yelu.in'

request = requests.get(main_url)


# soup = BeautifulSoup(request.text, 'html.parser')
soup = BeautifulSoup(request.content, 'lxml')

# if we want links categories, class = "icategories"

#for now get content of businesses link

# employment
employment = soup.find('a', {'class': 'cat_employment'})
emploment_path = employment['href']


request = requests.get(main_url + emploment_path)

employment_soup = BeautifulSoup(request.content, 'lxml')


# employment_soup is the variable having employment page content

# two classes for the company names. "company with_img g_0" and "company g_0" 
# since multiple pages, we need to use a while loop

links = []
company_names = []
address = []


arrow = employment_soup.find('a', {'class': 'pages_arrow'})
next_page = arrow['href']


while(arrow is not None):

    employment_soup = BeautifulSoup(request.content, 'lxml')

    current_page = employment_soup.find('span', {'class': 'pages_current'})


    arrow = employment_soup.find('a', {'class': 'pages_arrow','rel': 'next'})
    if(arrow is not None):
        next_page = arrow['href']

    for company in employment_soup.find_all('div', {'class': 'company with_img g_0'}):
        links.append(company.find('a')['href'])
        company_names.append(company.find('a').text)
        address.append(company.find('div', {"class":"address"}).text)
        

    for company in employment_soup.find_all('div', {'class': 'company g_0'}):
        links.append(company.find('a')['href'])
        company_names.append(company.find('a').text)
        address.append(company.find('div', {"class":"address"}).text)

    print("page "+ current_page.text + ": parsed") 


    request = requests.get(main_url + next_page)




print(len(links))
print(len(company_names))
print(len(address))

data = {}

list_jsons = []

for idx,name in enumerate(company_names):
    list_jsons.append({"name": name, "link_path": links[idx],"address": address[idx]})

data["employment_companies"] = list_jsons

with open('data.json','w') as   file:
    json.dump(data, file)
    file.close()
