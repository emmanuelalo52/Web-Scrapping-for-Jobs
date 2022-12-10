import time
from bs4 import BeautifulSoup
import requests
#create an input function for a user to identify the suitable jobs based on skills
print("Put Unfamiliar Skill")
unfamiliar_skill = input('>')
print(f'Filtering Out {unfamiliar_skill}')
#requests information from a specified website
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        publish_date = job.find('span',class_='sim-posted').span.text
        #condition if it is met
        if 'few' in publish_date:
            #search for the specified element
            company_name = job.find('h3',class_='joblist-comp-name').text.replace(' ','')#replace space with nothing
            #skill requirement
            skill = job.find('span',class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skill:
                #save as files
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name:{company_name.strip()}\n")#strip is to removed the irrelevant spacings
                    f.write(f"Required Skills:{skill.strip()}\n")
                    f.write(f'More Info:{more_info}\n')
                    print(f'file saved:{index}')

if __name__=="__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait*60)