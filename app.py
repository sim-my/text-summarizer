from flask import Flask, render_template, request
from model import main
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        input_text = request.form.get("input_text")       
        final_summary=main(input_text)
        return render_template('app.html',summary=final_summary, input_text=input_text)
    else:
        return render_template('app.html')



