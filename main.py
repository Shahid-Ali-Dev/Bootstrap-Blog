from flask import Flask,render_template
import requests
from datetime import datetime

year = datetime.now().year
app = Flask(__name__)   
response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
@app.route('/')
def home():
    return render_template('index.html', posts=response.json(), year=year)

@app.route('/about')
def about():
    return render_template('about.html', posts=response.json(), year=year)

@app.route('/contact')
def contact():
    return render_template('contact.html', posts=response.json(), year=year)

@app.route('/post/<int:post_id>')
def post(post_id):
    post_ = next((item for item in response.json() if item["id"] == post_id), None)
    return render_template('post.html', post_=post_, year=year)

if __name__ == "__main__":
    app.run(debug=True)