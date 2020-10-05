from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        input_text = request.form.get("input_text")
        print(input_text)
        return render_template('app.html')
    else:
        return render_template('app.html')
