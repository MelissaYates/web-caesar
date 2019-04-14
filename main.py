from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBUG"] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            #textarea{
                margin: 30px 0px 10px 0px;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="" method="post">
            <label for="Rotation">Rotate by:</label>
            <input id="Rotation" type="text" name="rot" placeholder = "0">
            <input type="textarea" id= "textarea" name ="text">
            <input type="submit" name= "Submit Query" value="Submit Query">
        </form>
    </body>
</html>

"""
@app.route("/", methods= ["POST"])
def encrypt(rot, text):
    encrypt_text = rotate_string(rot,text)
    return "<h1>" + encrypted_text + "</h1>"

@app.route("/")
def index():
    return form

@app.route("/hello", methods=["POST"])
def hello():
    first_name = request.form["first_name"]
    return "<h1>Hello, " + first_name + "</h1>"


app.run()