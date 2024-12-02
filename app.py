from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Hello_world():
    return render_template('index.html')
    # return "<p>Hello World!</p>"




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000") #to open webpage on mobile 
    #host="0.0.0.0" i.e to open webpage on mobile.