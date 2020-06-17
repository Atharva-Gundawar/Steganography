from flask import *
from mysteganography import *
app=Flask(__name__)


@app.route("/")
def start():
    return render_template("Start.html")

@app.route("/encode",methods=["POST","GET"])
def encode1():
    return render_template("encode.html")
    
@app.route("/decode",methods=["POST","GET"])
def decode1():
    return render_template("decode.html")

@app.route("/encodesuccess",methods=["POST","GET"])
def encodesuccess():
    encodesuccess.text_to_b_hidden=str(request.form['lmao'])
    print(encodesuccess.text_to_b_hidden)
    encodesuccess.Key=str(request.form['Key'])
    print(encodesuccess.Key)
    f=request.files['file']
    encodesuccess.file_name=f.filename
    print(encodesuccess.file_name)
    f.save(encodesuccess.file_name)
    print("File saved")
    encode(encodesuccess.file_name,encodesuccess.text_to_b_hidden, encodesuccess.Key,encodesuccess.file_name)
    print("Succesfully Encodede \n")
    #return render_template("success.html",start=success.start_page,end=success.end_page,name=success.file_name)
    path='\\' +str(encodesuccess.file_name.split(".")[0])+".png"
    path=path[1:]
    print("splited")
    #C:\Users\Atharva\Desktop\MACHINE LERNING UDEMY\stegono\steganography\8e541e90-cce4-4e12-b281-04a7505bc47a.png
    #path="/"+str(encodesuccess.file_name)
    return send_file(path, as_attachment=True)
    """and render_template("Start.html")"""

@app.route("/decodesuccess",methods=["POST","GET"])
def decodesuccess():
    decodesuccess.Key=str(request.form['Key'])
    print(decodesuccess.Key)
    f=request.files['file']
    decodesuccess.file_name=f.filename
    print(decodesuccess.file_name)
    f.save(decodesuccess.file_name)
    decodetext=decode(decodesuccess.file_name,decodesuccess.Key)
    print(decodetext)
    #encode(decodesuccess.file_name,decodesuccess.text_to_b_hidden, decodesuccess.Key,success.file_name)
    #return render_template("success.html",start=success.start_page,end=success.end_page,name=success.file_name)
    return render_template("final.html",string_variable = decodetext)

if __name__ == "__main__" :
    app.run(debug=True)