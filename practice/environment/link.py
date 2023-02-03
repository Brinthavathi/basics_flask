from flask import Flask,render_template
pract=Flask(__name__)
@pract.route("/")
@pract.route("/<name>")
def good(name):
 return render_template("index.html",data=name)

if __name__ =="__main__":
  pract.run(debug=True)