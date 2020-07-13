from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def home():
    
    return "Welcome home"

@app.route("/add")
def add():
        
    a = 10
    b = 20
    
    return str(a+b)

@app.route("/addparamget",methods=['GET'])
def add_param_get():
    
    a = request.args.get("a")
    b = request.args.get("b")
    
    return (str(int(a) + int(b)))

@app.route("/addparampost",methods=['POST'])
def add_param_post():
    
    a = request.form["a"]
    b = request.form["b"]
    
    return (str(int(a) + int(b)))

if __name__ == '__main__':
    app.run()