from flask import Flask, request
from cesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Шифр Цезаря</title>
        
        <style>
            #page {{
                margin: 0 100px;
                padding-top: 20px;
            }}
            
            header {{
                color: blue;
            }}
            
            table {{
                width: 100%;
            }}
            
            table, td {{
                text-align: center;
            }}
            
            #two > #r {{
                width: 30px;
            }}
            
            #two > #t {{
                width: 170px;
                margin-left: 5px;
                text-align: center;
            }}
            
            #two > #button {{
                margin-top: 5px;
            }}
        </style>
    </head>
    <body>
        <div id="page">
            <header>
                <h1>Legion</h1>
                <hr/>
            </header>
            <form action ="/" method="POST">
                <table>
                    <td id="one" width="40">
                        <textarea autofocus rows="30" cols="60" name="in" id="inputText" placeholder="input"></textarea>
                    </td>
                    <td id="two">
                        <input type="text" id="r" placeholder="ROT" readonly>
                        <input type="text" name="rot" id="t" placeholder="Text i">
                        
                        <div id="button">
                            <input type="submit" name="enc" id="button1" value="Зашифровать">
                            <input type="submit" name="dec" id="button2" value="Расшифровать">
                        </div>
        
        
                    </td>
                    <td id="three" width="40">
                        <textarea ng-model="outputText" autofocus rows="30" cols="60" id="outputText" placeholder="output">{0}</textarea>
                    </td>
                </table>
            </form>
        </div>
    </body>
</html>"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    rot_text = str(request.form['in'])
    enc_dec_text = rotate_string(rot_text, rot)
    return form.format(enc_dec_text)
app.run()
