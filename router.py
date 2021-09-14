from flask import Flask
from flask.templating import render_template
import movieapi as ma
import temp as tm

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", movies=ma.callMovieApi(), nowtemp=tm.callTempData())  

if __name__ == "__main__":
    app.run(debug=True)