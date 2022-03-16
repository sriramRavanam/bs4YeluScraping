# Script to scrape Yelu.in

## Files
* test.py -> gets the _*list of links*_ from yelu.in/employment-agencies (_3026_ companies approx)
* readCompanyPage.py -> takes the links extracted, navigates to the sites and _*extracts data*_ to store as a json
* testCompany.py -> just a test file to try to *_extract data_* from one of the companyPages in yelu.in (Takes 4-5 hours to run! Phew!!)

* data.json -> output of test.py containing _*links*_
* test/
    * test.json -> contains the output of the company data scraped. Each of the *_outermost_* json object is a company.