from flask import Flask, jsonify, Response, make_response, request
import requests

app = Flask(__name__)

url = "https://foscos.fssai.gov.in/gateway/commonauth/commonapi/getsearchapplicationdetails/1"

@app.route("/api/v1/get_fssai_details", methods=["POST"])
def get_fssai_details():
    try:
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
    app.run()