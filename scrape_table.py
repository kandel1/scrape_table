from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urlopen(wiki)

soup = BeautifulSoup(page, "lxml")

tab_le = soup.find_all('table', class_='wikitable sortable plainrowheaders')

# We Need To Extract Information To the DataFrame so we need to iterate through each row (tr) and then assign each element of tr (td) to a variable and append it to a list.

A = []
B = []
C = []
D = []
E = []
F = []
G = []
for row in tab_le.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(cells) == 6:

        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
df = pd.DataFrame(A, columns=['Number'])
df['State/UT'] = B
df['Admin_Capital'] = C
df['Legislative_Capital'] = D
df['Judiciary_Capital'] = E
df['Year_Capital'] = F
df['Former_Capital'] = G
