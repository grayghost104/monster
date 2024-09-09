from flask import Flask, render_template, request, jsonify
import requests 
from bs4 import BeautifulSoup 
app = Flask(__name__)


def web():
    url= 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=monster+high+dolls+g1&_sacat=0&_odkw=monster+high+dolls&_osacat=0'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # p1 = soup.find('div', classname='s-item_image')
        a2 = soup.find('li', id="item26df79b39f")
        print(a2)

@app.route('/web')
def grape():
    web()
    return{}
if __name__ == "__main__":
    app.run(debug=True)
    web()