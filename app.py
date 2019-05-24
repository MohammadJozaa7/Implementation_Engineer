from flask import Flask, render_template, flash, redirect, url_for,request

app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True
# app.config['TEMPLATES_AUTO_RELOAD'] = True

# Home
@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
