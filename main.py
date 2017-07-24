from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        link = request.form['link']
        return redirect(link)


app.run(port = 8081)
