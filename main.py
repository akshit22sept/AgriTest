from flask import Flask, render_template, request, flash, redirect, url_for
import os
from Models import Predict
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = 'a'
app.config['SESSION_TYPE'] = 'filesystem'

AL = 'static/files/AllLeaves'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['AL'] = AL


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('layout_1.html')


@app.route("/Predictions/All/", methods=['GET', 'POST'])
def predAll():
    if request.method == 'POST':

        if 'image' not in request.files:

            flash('No file part')

            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = "tbp.png"
            file.save(os.path.join(app.config['AL'], filename))
            pred,dis=Predict("static/files/AllLeaves/tbp.png")
            return redirect(url_for('output', pred=pred,dis = dis))


    return render_template("layout_2.html")

@app.route("/solutions/")
def solutions():
    return render_template("Solutions.html")

@app.route("/solutions/apple_scab")
def apple_scab():
    return render_template("apple_scab.html")

@app.route("/solutions/black_rot")
def black_rot():
    return render_template("black_rot.html")

@app.route("/solutions/cedar_apple_rust")
def cedar_apple_rust():
    return render_template("cedar_apple_rust.html")

@app.route("/solutions/healthy")
def healthy():
    return render_template("healthy.html")

@app.route("/output/<pred>+<dis>")
def output(pred,dis):
    print(pred,dis)
    return render_template("pred2.html", pred=pred, dis=dis)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
