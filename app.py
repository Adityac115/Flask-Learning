from flask import Flask,request,render_template
import os
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/score',methods=['POST'])
def score():
    # Phy=request.form['phy']
    # Chem=request.form['chem']
    # Math=request.form['math']
    # scores={'Physics':Phy, 'Chemistry':Chem,'Math':Math}
    return render_template('score_table.html',results=request.form)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)