from flask import Flask, render_template, request, jsonify
import requests 
from bs4 import BeautifulSoup 
app = Flask(__name__)


def web():
    url= 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=monster+high+dolls+g1&_sacat=0&_odkw=monster+high+dolls&_osacat=0'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        ebay = []
        d1 = soup.find('li', id="item5a1575ea09")
        l1 = d1.find("a", class_='s-item__link').get('href')
        d2 = soup.find('li', id="item36e246057f")
        l2 = d2.find("a", class_='s-item__link').get('href')
        d3 = soup.find('li', id="item2b5908a6f9")
        l3 = d3.find("a", class_='s-item__link').get('href')
        d4 = soup.find('li', id="item2b62d9c3a3")
        l4 = d4.find("a", class_='s-item__link').get('href')
        d5 = soup.find('li', id="item26def8c1df")
        l5 = d5.find("a", class_='s-item__link').get('href')

        ebay.append(l1)
        ebay.append(l2)
        ebay.append(l3)
        ebay.append(l4)
        ebay.append(l5)
        print(ebay)
@app.route('/web')
def grape():
    web()
    return{}
if __name__ == "__main__":
    app.run(debug=True)
    web()