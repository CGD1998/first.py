from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


#@app.route('/hello')
def hello():

    return '你好，明天更好'


app.add_url_rule('/hello', view_func=hello)


app.run(host='0.0.0.0', debug=True)

