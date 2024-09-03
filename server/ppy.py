from flask import Flask, render_template, request, jsonify
import requests 
from bs4 import BeautifulSoup 
app = Flask(__name__)

def news():
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=monster+high+dolls+g1&_sacat=0&_odkw=monster+high+dolls&_osacat=0'
    response = requests.get(url)
    if response.status_code == 200:
        soup= BeautifulSoup(response.text, "html.parser")
        ebay = []
        b1 = soup.find('li', id="item5a1575ea09")
        b2 = soup.find('li', id="item36e246057f")
        b3 = soup.find('li', id="item2b5908a6f9")
        b4 = soup.find('li', id="item2b62d9c3a3")
        b5 = soup.find('li', id="item26def8c1df")
        b6 = soup.find('li', id="item34b2681cde")
        b7 = soup.find('li', id="item472fe7ed45")
        ebay.extend(b1,b2,b3,b4,b5,b6,b7)
        # print(b1)
        # print(b2)
        # print(b3)
        # print(b4)
        # print(b5)
        # print(b6)
        # print(b7)
        print(ebay)
    else:
        print('didnt work')
@app.route('/scrap')
def grape():
    news()
    return{}
if __name__ == "__main__":
    app.run(debug=True)
    news()

























































# def scrape_news():
#     url = "https://monsterhigh.fandom.com/wiki/Monster_High_Wiki"
#     table = soup.find('table', class_='article table').text.strip() if soup.find('table') else None
#     div = soup.div.text.strip() if soup.find('p') else None
#     text = soup.find('text').text.strip() if soup.find('text') else None 
#     ol = soup.find('ol', class_ ='').text.strip() if soup.find('ol') else None 
#     print(table)
#     print(div)
#     print(text[2])
#     print(ol)
#     return jsonify({'h2': h2, 'div': div,
#      'em': em, 'ol':ol
#      })

# @app.route("/")
# def home():
#     # headlines = scrape_news()
#     return render_template("index.html")