from flask import Flask, flash, request, redirect, url_for,render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
from turbo_flask import Turbo
from Models import AllLeavesM


#---------------------------------------------------------------------------------

#Flask App Start

UPLOAD_FOLDER = 'imageinput'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
turbo = Turbo(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))



        print(os.listdir("imageinput"))
        return turbo.stream(turbo.update(render_template("index.html",pred="abc"),'pred'))
    return render_template("index.html")



if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.debug=True
    app.run()