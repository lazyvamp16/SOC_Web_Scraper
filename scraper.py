import requests
from bs4 import BeautifulSoup
import pandas as pd
from tenacity import retry, stop_after_attempt, wait_fixed

url = 'https://itc.gymkhana.iitb.ac.in/wncc/soc/'

# retry mechanism 
@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def fetch_url(url):
    response = requests.get(url)
    response.raise_for_status()  # to notice bad responses
    return response

try:
    response = fetch_url(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # section having all the project topics and details
    project_sections = soup.find_all('div', class_='shuffle-item')

    projects = []

    for project_section in project_sections:
        category = project_section.get('data-groups',[]) 
        link = project_section.find('a')
        title = project_section.find('p', class_='lead')

        if link and title:
            project_link = 'https://itc.gymkhana.iitb.ac.in' + link['href']
            project_title = title.text.strip()
            projects.append({
                'projects': project_title,
                'link to project': '=HYPERLINK("{}")'.format(project_link),
                'category': category
            })


    df = pd.DataFrame(projects)

    df.to_excel('projects2.xlsx', index=False)
    print("Data has been saved to projects2.xlsx")

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")