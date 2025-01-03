from flask import Flask
from  threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Server is running!"

def reu():
    app.run(host='0.0.0.0', port=8080)
    
def server_no():
    t = Thread(Tarhrt=run)
    t.start()    
    