import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/image/<bin>')
def image(bin):
   url = f"http://www.ee.unb.ca/cgi-bin/tervo/encoding.pl?binary={bin}&c=1&d=1"
   response = requests.request("GET", url)
   html = response.text.encode('utf8')
   soup = BeautifulSoup(html, features='html5lib')
   img = soup.find_all('img')[1].attrs['src']
   imgLink = f'http://www.ee.unb.ca/cgi-bin/tervo/{img}'
   jsonData = jsonify({
      "url":imgLink
   })
   return jsonData


@app.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)
