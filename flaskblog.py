from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Narendra Modi',
        'title': 'Winning election',
        'content': 'I am winning all elections',
        'date posted': 'May 14, 2014'
    },
    {
        'author': 'Rahul Gandhi',
        'title': 'Loosing all the elections',
        'content': 'I am loosing all elections. I am a looser!',
        'date posted': 'May 15, 2014'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)