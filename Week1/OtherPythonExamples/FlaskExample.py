from flask import Flask, request 

app: Flask = Flask(__name__)

#@app.route connects this route to the method
# the first argument is the URL, you add it to the end of Flasks to provided domain name and port
#second argument sets the verb for the route

count=0

data_set = {"1": "some data", "2": "more data"}

@app.route("/",methods=["GET"])
def hello_world():
    return "Hello World" # the return must be a string, dict, tuple, responsive instance

#you can add path parameters to the route by placing them inside <> brackets
@app.route("/greeting/<name>",methods=["GET"])
def greeting(name:str):
    return f"Hello {name}"

@app.route("/<num1>/add/<num2>", methods=["GET"])
def addition(num1: str, num2: str):
    result = int(num1) +int(num2)
    return str(result)

#routes with bodies can not access them in the url: you have to retrieve them from the body of the request
@app.route("/login",methods=["POST"])
def login():
    credentials = request.get_json() #flask includes this handy method for us: sets out variable to the JSON
    #dictionary value
    username = credentials["username"]
    password = credentials["password"]
    if username == "good" and password == "correct":
        return "your credentials are good!"
    else:
        return "your credentials are bad!"
    

# you can also use your routes to affect stored data (think a database) and return data that you want
@app.route("/count",methods=["PATCH"])
def add_count():
    global count
    count += 1
    return f"the count is not {count}"

# you can use query parameters to filter the data you access
@app.get("/data") #route will look like this: http://domain:port/data?query_param=value
def query_database():
    query = request.args["DB"]
    if query == "":
        return data_set
    else:
        return data_set[query]




app.run()


    