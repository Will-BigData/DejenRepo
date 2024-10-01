from flask import Flask, request

app: Flask = Flask(__name__)

# @app.route connects this route to the method
# the first argument is the url, you add it to the end of Flasks provided domain name and port
# the second argument sets the verb for the route (can instead do @app.get)
count = 0

data_set = {"1": "some data", "2": "more data"}  # we will use this with our query route later on

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello World"




# you can add path paramaters to the route by placing them inside <> brackets
# this is useful for accessing specific information
@app.route("/greeting/<name>", methods=["GET"])
def greeting(name: str):  # make sure to pass them in the method
    return f"Hello {name}!"  # you can then work with them like a regular variable


@app.route("/<num1>/add/<num2>", methods=["GET"])
def addition(num1: str, num2: str):
    result = int(num1) + int(num2)
    return str(result)  # notice we had to cast the int as a string here, else we would have gotten an error


# routes with bodies can not access them in the url: you have to retrieve them from the body of the request
@app.route("/login", methods=["POST"])
def login():
    credentials = request.get_json()  # flask includes this handy method for us: sets our variable to the JSON dictionary values
    # you need to make sure the key values match what is in the json
    username = credentials["username"]
    password = credentials["password"]
    if username == "good" and password == "correct":  # in a real application you would have more robust validation, actually log in, etc
        return "your credentials are good!"
    else:
        return "your credentials are bad!"
    
# Added this Delete method by my self
@app.route("/greeting/<name>", methods=["DELETE"])
def delete_greeting(name: str):
    # Placeholder logic for deleting a greeting (usually you'd interact with a database here)
    return f"Deleted greeting for {name}!" # 200 status code for success




# you can also use your routes to affect stored data (think a database) and return data that you want
@app.route("/count", methods=["PATCH"])
def add_count():
    global count  # this route adds one to the count variable we set up at the start
    count +=1 # this route adds one to the count variable we set up at the start
    return f"The count is now {count}" # we can then see how many times we have called the route


# you can use query parameters to filter the data you access
@app.get("/data")  # route will look like this: http://domain:port/data?query_param=value
# you can use the & symbol to make multiple query params
def query_database():
    # instead off getting the whole database we will be getting only the part we specify in the query param
    # if no param is provided we get the whole set
    query = request.args["DB"]
    if query == "":  # don't do this in an actual app: use a path param to get all the data
        return data_set
    else:
        return data_set[query]
    

    #try creating flask app on your own for practice


app.run()