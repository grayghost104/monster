from flask import Flask, render_template, request, jsonify
import requests 
# from urllib.request import Request, urlopen
from bs4 import BeautifulSoup 
app = Flask(__name__)

url = 'https://en.wikipedia.org/wiki/Monster_High_(web_series)'
def news():
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        test = soup.find("td", classname = "summary")
        # test  = soup.find("div", attrs={"class": "s-item_wrapper clearfix"})
        print(test)
    else:
        print('didnt work')

# table = soup.find("table", attrs={"id": "rankingstable"})
@app.route('/scrap')
def grape():
    # return(news())
    # healdlines = news()
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