from flask import *
#from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

'''app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class encode(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    key = db.Column(db.String(20), nullable = False)
    #message = db.Column(db.String(100), nullable = False)
    ## Above is to store the users messages ... not recommended

'''
@app.route("/")
def start():
    return render_template("Start.html")

@app.route("/encode",methods=["GET","POST"])
def upload():
    return render_template("encode.html")
    if request.method == 'POST':
        text=request.form['text']
        key=request.form['key']
         

@app.route("/encodesuccess",methods=["POST"])
def success():
    success.text_to_b_hidden=str(request.form['lmao'])
    print(success.text_to_b_hidden)
    success.Key=int(request.form['Key'])
    print(success.Key)
    f=request.files['file']
    success.file_name=f.filename
    print(success.file_name)
    f.save(success.file_name)
    #return render_template("success.html",start=success.start_page,end=success.end_page,name=success.file_name)
    return render_template("Start.html")



if __name__ == "__main__" :
    app.run(debug=True)