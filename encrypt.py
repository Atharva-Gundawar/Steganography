from flask import *

app=Flask(__name__)


@app.route("/")
def start():
    return render_template("Start.html")

@app.route("/encode",methods=["POST"])
def upload():
    return render_template("encode.html")

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