from flask import Flask, jsonify

import requests

app = Flask(__name__)


@app.route('/searchTopic/<string:topic>', methods=['GET'])
def searchByBookTopic(topic):
    req=requests.get("http://192.168.56.101:7000/search/{}".format(topic)) #send to catalog

    if req.status_code == 200:
        result=req.json() #content of json as dictionary

        return jsonify(result)

    elif req.status_code == 404:
        return 'The server has not found anything matching the given URL',404

    else:
        return 'Status code '+ str(req.status_code) +' indicates to something ERROR!',req.status_code


@app.route('/searchID/<int:id>', methods=['GET'])
def searchByBookId(id):
    req=requests.get("http://192.168.56.101:7000/info/{}".format(id))

    if req.status_code == 200:
        result=req.json() #content of json as dictionary

        return jsonify(result)

    elif req.status_code == 404:
        return 'The server has not found anything matching the given URL',404

    else:
        return 'Status code '+ str(req.status_code) +' indicates to something ERROR!',req.status_code

@app.route('/purchase/<int:id>', methods=['POST'])
def purchase(id):

    req = requests.get("http://192.168.65.103:9000/updateinfo/{}".format(id))

    if req.status_code == 200:
        result = req.json()  # content of json as dictionary
        return jsonify(result)

    elif req.status_code == 404:
        return 'The server has not found anything matching the URI given',404

    else:
        return 'Status code '+ str(req.status_code) +' indicates to something ERROR!',req.status_code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)
