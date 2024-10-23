from flask import Flask, request, jsonify
import requests
import send_request
import analisis

app = Flask(__name__)

# Replace this with the actual OCR API URL

@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if the image is part of the request

    # Send the file to the OCR API
    try:
        if 'url' not in request.form:
            return jsonify({'error': 'No url part'}), 400

        file = request.form['url']

        # If the user does not select a file, the browser submits an empty file
        if file == "" or file is None:
            return jsonify({'error': 'url empty'}), 400
        as_dict, status_code = send_request.send_reqeust(file)

        # Return the response from the OCR API
        return jsonify(as_dict), status_code 
    except (requests.exceptions.RequestException, TypeError) as e :
        return jsonify({'error': str(e), 'gula': 0, 'lemak': 0, 'garam': 0}), 200

@app.route('/grade', methods=['GET'])
def grade():
    try:
        gula = float(request.args.get("sugar"))
        lemak = float(request.args.get("fat"))
        garam = float(request.args.get("garam"))
    except (TypeError, ValueError):
        return jsonify({"error": "parameters must be numbers"}), 400

    try:
        hasil = analisis.analisis(gula, lemak, garam)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return the exception message
    
    return jsonify({"hasil": hasil}), 200

if __name__ == '__main__':
    app.run(debug=True)
