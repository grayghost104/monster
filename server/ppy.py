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
        d1 = soup.find('li', id="item5a1575ea09")
        d2 = soup.find('li', id="item36e246057f")
        d3 = soup.find('li', id="item2b5908a6f9")
        d4 = soup.find('li', id="item2b62d9c3a3")
        d5 = soup.find('li', id="item26def8c1df")
        d6 = soup.find('li', id="item34b2681cde")
        d7 = soup.find('li', id="item472fe7ed45")

        a1 = soup.find('li', id="item5772d2585c")
        a2 = soup.find('li', id="item5772d2574e")

        ebay.append(a1)
        ebay.append(a2)
        ebay.append(d1)
        ebay.append(d2)
        ebay.append(d3)
        ebay.append(d4)
        ebay.append(d5)
        ebay.append(d6)
        ebay.append(d7)
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