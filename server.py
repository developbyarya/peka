from flask import Flask, request, jsonify
import requests
import send_request
import analisis

app = Flask(__name__)

# Replace this with the actual OCR API URL

@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if the image is part of the request
    if 'url' not in request.form:
        return jsonify({'error': 'No url part'}), 400

    file = request.form['url']

    # If the user does not select a file, the browser submits an empty file
    if file == "" or file is None:
        return jsonify({'error': 'url empty'}), 400

    # Send the file to the OCR API
    try:
        as_dict, status_code = send_request.send_reqeust(file)

        # Return the response from the OCR API
        return jsonify(as_dict), status_code 
    except (requests.exceptions.RequestException, TypeError) as e :
        return jsonify({'error': str(e), 'gula': 0, 'lemak': 0, 'garam': 0}), 200

@app.route('/grade', methods=['GET'])
def grade():
    gula = int(request.args.get("sugar"))
    lemak = int(request.args.get("fat"))
    garam = int(request.args.get("garam"))

    if not gula or not lemak or not garam:
        return jsonify({"error": "paramter not complete"}), 400
    
    hasil = analisis.analisis(gula, lemak, garam) 
    return jsonify({"hasil": hasil}), 200
if __name__ == '__main__':
    app.run(debug=True)
