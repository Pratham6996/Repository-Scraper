import requests
import pandas as pd
from bs4 import BeautifulSoup
html_data = requests.get("https://github.com/topics/react").text
base_url = "https://github.com/topics/react?page="
url_list = []
lnk = 'https://github.com/'
for num in range(1, 8):
    url_list.append(base_url + str(num))
# print(url_list)
data_lst = []
i = 1
for url in url_list:
    html_data = requests.get(url).text
    soup = BeautifulSoup(html_data, 'lxml')
    all_divs = soup.find_all('article', class_='border rounded color-shadow-small color-bg-subtle my-4')
    for info in all_divs:
        Username = info.find('h3',class_='f3 color-fg-muted text-normal lh-condensed').get_text(strip=True)
        USERNAME = Username.split("/")
        Repos_name = info.find('a', class_='text-bold wb-break-word').get_text(strip=True)
        L = lnk + Username
        Stars = info.find('span', class_='Counter js-social-count').text.strip()
        # print(USERNAME[0])
        Link = info.find('a')['href']
        all_data_dict = {
            'SR. NO.' : i,
            'Username': USERNAME[0],
            'Repository name': Repos_name,
            'Stars': Stars,
            'URL': L
        }
        i += 1
        data_lst.append(all_data_dict)
df = pd.DataFrame(data_lst)
df.index = df.index + 1
trim = df.drop(index=[201,202,203,204,205,206,207,208,209,210], axis=1)
trimupdate = trim.reset_index(drop=True)
trimupdate.index = trimupdate.index + 1
print(trimupdate)
df.to_excel('Git_Pro_E2S_React.xlsx')