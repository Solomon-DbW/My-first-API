from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>") #type http://127.0.0.1:5000/get-user/123?extra=hello
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Joey",
        "email": "random@email.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

# GET = request data from a specified resource
# POST = Create a resource
# PUT = Update a resource
# DELETE = Delete a resource

if __name__ == "__main__":
    app.run(debug=True)