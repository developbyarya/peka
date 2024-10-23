import requests
import os
from dotenv import load_dotenv
import functions

load_dotenv()

API_KEY = os.environ.get("api_key") 
LINK = "https://api.ocr.space/parse/image"

def process_result_as_dict(lines):
    sugar = functions.get_sugar(lines)
    lemak = functions.get_fat(lines)
    garam = functions.get_natrium(lines)
    sugar = sugar if sugar is not None else 0
    lemak = lemak if lemak is not None else 0
    garam = garam if garam is not None else 0
    return {
        "sugar":  ((sugar[0] / 10.0) if sugar[1] == "mg" else sugar[0]) if sugar is not None else None,
        "lemak": ((lemak[0] / 10.0) if lemak[1] == "mg" else lemak[0]) if lemak is not None else None,
        "garam": ((garam[0] / 10.0) if garam[1] == "mg" else garam[0]) if garam is not None else None,
    } 

def send_reqeust(img_link):
    req = requests.post(LINK, headers={
        "apikey": API_KEY,
    }, data={"url": img_link, "OCREngine":2, "detectOrientation": True, "scale": True, "isOverlayRequired": True})
    req.raise_for_status()
    try:
        # Try to access the key in a safe way
        parsed_results = req.json().get("ParsedResults", [])
        
        if parsed_results and isinstance(parsed_results[0], dict):
            # Check if "TextOverlay" exists
            if "TextOverlay" in parsed_results[0]:
                lines = req.json().get("ParsedResults")[0].get("TextOverlay").get("Lines")
                return process_result_as_dict(lines), req.status_code
            else:
               return None, 500
        else:
            return None, 500
    except (IndexError, KeyError, TypeError) as e:
        print("An error occurred:", e)
        return None, 500

