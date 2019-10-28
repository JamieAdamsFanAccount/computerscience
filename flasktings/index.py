from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def parse_request():
    data = request.form  # data is empty
    # need posted data here
    if data["test"]:
        print (data["test"])
    return "Hello"

app.run(debug=True)