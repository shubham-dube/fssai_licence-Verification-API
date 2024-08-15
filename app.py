from flask import Flask, jsonify, Response, make_response, request
import requests

from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)


@app.route("/api/v1/get_fssai_details", methods=["POST"])
def get_fssai_details():
    try:
        url = "https://foscos.fssai.gov.in/gateway/commonauth/commonapi/getsearchapplicationdetails/1"
        licenceNumber = request.json.get("licenceNumber")
        session = requests.Session()

        session.verify = False

        postBody = {
            "flrsLicenseNo": licenceNumber
        }

        response = session.post(url, json=postBody)

        return jsonify(response.json())
    
    except Exception as e:
        print(e)
        return jsonify({"error": "Error in fetching fssai licence Details"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(asgi_app, host='0.0.0.0', port=5001)
    