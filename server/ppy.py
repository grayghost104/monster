from flask import Flask, render_template, request, jsonify
import requests 
# from urllib.request import Request, urlopen
from bs4 import BeautifulSoup 
app = Flask(__name__)

url = 'https://monsterhigh.fandom.com/wiki/Great_Scarrier_Reef_(TV_special)'
def news():
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")
        print(table)
    else:
        print('didnt work')

# table = soup.find("table", attrs={"id": "rankingstable"})
@app.route('/scrap')
def grape():
    # return(news())
    # healdlines = news()
    return{}
if __name__ == "__main__":
    news()


app.run(debug=True)

























































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