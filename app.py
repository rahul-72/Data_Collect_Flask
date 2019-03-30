from flask import Flask,render_template,request
import json,csv

app=Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit/',methods=['post'])
def submit():
    name=request.form['name']
    course=request.form['language']
    email=request.form['email']
    ph_no=request.form['ph_no']
    collegename=request.form['collegename']
    batchdate=request.form['batchdate']
    d=(name,course,email,ph_no,collegename,batchdate)
    f=open('static/data/student.csv','a',newline='')
    writer=csv.writer(f)
    writer.writerow(d)
    f.close()
    return render_template('submit.html')

if __name__ == "__main__":
    app.run('localhost',5000,debug=True)