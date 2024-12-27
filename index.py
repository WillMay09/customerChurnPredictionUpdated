from flask import Flask,jsonify
#routes

app = Flask(__name__)



@app.route('/index', methods=['GET'])
def return_Messag():
    return jsonify({

        'message':"Hello World"
    })

if __name__ == "__main__":
    app.run(debug=True)