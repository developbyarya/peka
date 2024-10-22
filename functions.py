import json, re

payload = """
{
  "ParsedResults": [
    {
      "Overlay": {
        "Lines": [
          {
            "LineText": "Nutrition Facts",
            "Words": [
              {
                "WordText": "Nutrition",
                "Left": 108,
                "Top": 113,
                "Height": 45,
                "Width": 284
              },
              {
                "WordText": "Facts",
                "Left": 419,
                "Top": 113,
                "Height": 45,
                "Width": 177
              }
            ],
            "MaxHeight": 45,
            "MinTop": 113
          },
          {
            "LineText": "Serving Size 212 g",
            "Words": [
              {
                "WordText": "Serving",
                "Left": 101,
                "Top": 171,
                "Height": 23,
                "Width": 78
              },
              {
                "WordText": "Size",
                "Left": 187,
                "Top": 171,
                "Height": 19,
                "Width": 45
              },
              {
                "WordText": "212",
                "Left": 239,
                "Top": 172,
                "Height": 18,
                "Width": 39
              },
              {
                "WordText": "g",
                "Left": 285,
                "Top": 176,
                "Height": 18,
                "Width": 12
              }
            ],
            "MaxHeight": 23,
            "MinTop": 171
          },
          {
            "LineText": "Amount Per Serving",
            "Words": [
              {
                "WordText": "Amount",
                "Left": 100,
                "Top": 218,
                "Height": 15,
                "Width": 81
              },
              {
                "WordText": "Per",
                "Left": 189,
                "Top": 218,
                "Height": 15,
                "Width": 35
              },
              {
                "WordText": "Serving",
                "Left": 230,
                "Top": 218,
                "Height": 18.5,
                "Width": 79
              }
            ],
            "MaxHeight": 18.5,
            "MinTop": 218
          },
          {
            "LineText": "Calories 257",
            "Words": [
              {
                "WordText": "Calories",
                "Left": 101,
                "Top": 242,
                "Height": 19,
                "Width": 105
              },
              {
                "WordText": "257",
                "Left": 216,
                "Top": 243,
                "Height": 18,
                "Width": 39
              }
            ],
            "MaxHeight": 19,
            "MinTop": 242
          },
          {
            "LineText": "Total Fat 9.4g",
            "Words": [
              {
                "WordText": "Total",
                "Left": 100,
                "Top": 298,
                "Height": 18,
                "Width": 64
              },
              {
                "WordText": "Fat",
                "Left": 174,
                "Top": 298,
                "Height": 18,
                "Width": 40
              },
              {
                "WordText": "9.4g",
                "Left": 224,
                "Top": 298,
                "Height": 23,
                "Width": 45
              }
            ],
            "MaxHeight": 23,
            "MinTop": 298
          },
          {
            "LineText": "Saturated Fat 1.1g",
            "Words": [
              {
                "WordText": "Saturated",
                "Left": 122,
                "Top": 328,
                "Height": 18,
                "Width": 101
              },
              {
                "WordText": "Fat",
                "Left": 232,
                "Top": 329,
                "Height": 18,
                "Width": 33
              },
              {
                "WordText": "1.1g",
                "Left": 275,
                "Top": 328,
                "Height": 23,
                "Width": 43
              }
            ],
            "MaxHeight": 23,
            "MinTop": 328
          },
          {
            "LineText": "Cholesterol Omg",
            "Words": [
              {
                "WordText": "Cholesterol",
                "Left": 101,
                "Top": 361,
                "Height": 18,
                "Width": 147
              },
              {
                "WordText": "Omg",
                "Left": 259,
                "Top": 361,
                "Height": 22,
                "Width": 44
              }
            ],
            "MaxHeight": 22,
            "MinTop": 361
          },
          {
            "LineText": "Sodium 41 mg",
            "Words": [
              {
                "WordText": "Sodium",
                "Left": 101,
                "Top": 393,
                "Height": 18,
                "Width": 94
              },
              {
                "WordText": "41",
                "Left": 206,
                "Top": 393,
                "Height": 18,
                "Width": 22
              },
              {
                "WordText": "mg",
                "Left": 233,
                "Top": 397,
                "Height": 19,
                "Width": 31
              }
            ],
            "MaxHeight": 19,
            "MinTop": 393
          },
          {
            "LineText": "Potassium 400mg",
            "Words": [
              {
                "WordText": "Potassium",
                "Left": 101,
                "Top": 425,
                "Height": 18,
                "Width": 132
              },
              {
                "WordText": "400mg",
                "Left": 244,
                "Top": 425,
                "Height": 23,
                "Width": 72
              }
            ],
            "MaxHeight": 23,
            "MinTop": 425
          },
          {
            "LineText": "Calories from Fat 84",
            "Words": [
              {
                "WordText": "Calories",
                "Left": 386,
                "Top": 242,
                "Height": 19,
                "Width": 86
              },
              {
                "WordText": "from",
                "Left": 478,
                "Top": 242,
                "Height": 19,
                "Width": 46
              },
              {
                "WordText": "Fat",
                "Left": 533,
                "Top": 243,
                "Height": 18,
                "Width": 34
              },
              {
                "WordText": "84",
                "Left": 575,
                "Top": 242,
                "Height": 19,
                "Width": 26
              }
            ],
            "MaxHeight": 19,
            "MinTop": 242
          },
          {
            "LineText": "Total Carbohydrates 39.8g",
            "Words": [
              {
                "WordText": "Total",
                "Left": 100,
                "Top": 457,
                "Height": 18,
                "Width": 64
              },
              {
                "WordText": "Carbohydrates",
                "Left": 174,
                "Top": 457,
                "Height": 23,
                "Width": 187
              },
              {
                "WordText": "39.8g",
                "Left": 372,
                "Top": 457,
                "Height": 23,
                "Width": 58
              }
            ],
            "MaxHeight": 23,
            "MinTop": 457
          },
          {
            "LineText": "Dietary Fiber 10.0g",
            "Words": [
              {
                "WordText": "Dietary",
                "Left": 123,
                "Top": 487,
                "Height": 23,
                "Width": 73
              },
              {
                "WordText": "Fiber",
                "Left": 204,
                "Top": 487,
                "Height": 18,
                "Width": 53
              },
              {
                "WordText": "10.0g",
                "Left": 267,
                "Top": 487,
                "Height": 23,
                "Width": 56
              }
            ],
            "MaxHeight": 23,
            "MinTop": 487
          },
          {
            "LineText": "Sugars 2.1g",
            "Words": [
              {
                "WordText": "Sugars",
                "Left": 122,
                "Top": 517,
                "Height": 23,
                "Width": 74
              },
              {
                "WordText": "2.1g",
                "Left": 205,
                "Top": 517,
                "Height": 23,
                "Width": 45
              }
            ],
            "MaxHeight": 23,
            "MinTop": 517
          },
          {
            "LineText": "Protein 8.0g",
            "Words": [
              {
                "WordText": "Protein",
                "Left": 101,
                "Top": 550,
                "Height": 18,
                "Width": 91
              },
              {
                "WordText": "8.0g",
                "Left": 204,
                "Top": 550,
                "Height": 22,
                "Width": 45
              }
            ],
            "MaxHeight": 22,
            "MinTop": 550
          },
          {
            "LineText": "Vitamin A",
            "Words": [
              {
                "WordText": "Vitamin",
                "Left": 100,
                "Top": 593,
                "Height": 18,
                "Width": 77
              },
              {
                "WordText": "A",
                "Left": 184,
                "Top": 593,
                "Height": 18,
                "Width": 17
              }
            ],
            "MaxHeight": 18,
            "MinTop": 593
          },
          {
            "LineText": "Calcium 3%",
            "Words": [
              {
                "WordText": "Calcium",
                "Left": 101,
                "Top": 620,
                "Height": 19,
                "Width": 83
              },
              {
                "WordText": "3%",
                "Left": 192,
                "Top": 620,
                "Height": 19,
                "Width": 33
              }
            ],
            "MaxHeight": 19,
            "MinTop": 620
          },
          {
            "LineText": "Nutrition Grade A",
            "Words": [
              {
                "WordText": "Nutrition",
                "Left": 102,
                "Top": 659,
                "Height": 18,
                "Width": 111
              },
              {
                "WordText": "Grade",
                "Left": 223,
                "Top": 659,
                "Height": 18,
                "Width": 76
              },
              {
                "WordText": "A",
                "Left": 307,
                "Top": 659,
                "Height": 18,
                "Width": 19
              }
            ],
            "MaxHeight": 18,
            "MinTop": 659
          },
          {
            "LineText": "% Daily Value*",
            "Words": [
              {
                "WordText": "%",
                "Left": 447,
                "Top": 273,
                "Height": 16,
                "Width": 18
              },
              {
                "WordText": "Daily",
                "Left": 474,
                "Top": 274,
                "Height": 18.5,
                "Width": 52
              },
              {
                "WordText": "Value*",
                "Left": 532,
                "Top": 273,
                "Height": 15,
                "Width": 69
              }
            ],
            "MaxHeight": 18.5,
            "MinTop": 273
          },
          {
            "LineText": "140/0",
            "Words": [
              {
                "WordText": "140/0",
                "Left": 548,
                "Top": 298,
                "Height": 19,
                "Width": 53
              }
            ],
            "MaxHeight": 19,
            "MinTop": 298
          },
          {
            "LineText": "60/0",
            "Words": [
              {
                "WordText": "60/0",
                "Left": 562,
                "Top": 330,
                "Height": 19,
                "Width": 38
              }
            ],
            "MaxHeight": 19,
            "MinTop": 330
          },
          {
            "LineText": "0%",
            "Words": [
              {
                "WordText": "0%",
                "Left": 562,
                "Top": 360,
                "Height": 20,
                "Width": 38
              }
            ],
            "MaxHeight": 20,
            "MinTop": 360
          },
          {
            "LineText": "20/0",
            "Words": [
              {
                "WordText": "20/0",
                "Left": 562,
                "Top": 392,
                "Height": 20,
                "Width": 38
              }
            ],
            "MaxHeight": 20,
            "MinTop": 392
          },
          {
            "LineText": "110/0",
            "Words": [
              {
                "WordText": "110/0",
                "Left": 548,
                "Top": 425,
                "Height": 19,
                "Width": 53
              }
            ],
            "MaxHeight": 19,
            "MinTop": 425
          },
          {
            "LineText": "40%",
            "Words": [
              {
                "WordText": "40%",
                "Left": 547,
                "Top": 489,
                "Height": 19,
                "Width": 54
              }
            ],
            "MaxHeight": 19,
            "MinTop": 489
          },
          {
            "LineText": "Vitamin C",
            "Words": [
              {
                "WordText": "Vitamin",
                "Left": 446,
                "Top": 593,
                "Height": 18,
                "Width": 78
              },
              {
                "WordText": "C",
                "Left": 532,
                "Top": 593,
                "Height": 18,
                "Width": 16
              }
            ],
            "MaxHeight": 18,
            "MinTop": 593
          },
          {
            "LineText": "Iron 14%",
            "Words": [
              {
                "WordText": "Iron",
                "Left": 509,
                "Top": 620,
                "Height": 19,
                "Width": 38
              },
              {
                "WordText": "14%",
                "Left": 557,
                "Top": 620,
                "Height": 19,
                "Width": 44
              }
            ],
            "MaxHeight": 19,
            "MinTop": 620
          }
        ],
        "HasOverlay": true,
        "Message": "Total lines: 26"
      },
      "FileParseExitCode": 1,
      "TextOrientation": "0",
      "ParsedText": "Nutrition Facts\r\nServing Size 212 g\r\nAmount Per Serving\r\nCalories 257\r\nTotal Fat 9.4g\r\nSaturated Fat 1.1g\r\nCholesterol Omg\r\nSodium 41 mg\r\nPotassium 400mg\r\nCalories from Fat 84\r\nTotal Carbohydrates 39.8g\r\nDietary Fiber 10.0g\r\nSugars 2.1g\r\nProtein 8.0g\r\nVitamin A\r\nCalcium 3%\r\nNutrition Grade A\r\n% Daily Value*\r\n140/0\r\n60/0\r\n0%\r\n20/0\r\n110/0\r\n40%\r\nVitamin C\r\nIron 14%\r\n",
      "ErrorMessage": "",
      "ErrorDetails": ""
    }
  ],
  "OCRExitCode": 1,
  "IsErroredOnProcessing": false,
  "ProcessingTimeInMilliseconds": 1.453,
  "SearchablePDFURL": "Searchable PDF not generated as it was not requested."
}
"""
data = json.loads(payload, strict=False)
text_raw = data.get("ParsedResults")[0].get("Overlay").get("Lines")

def extract_unit(text):
  match = re.search(r'(\d+\.?\d*)\s*(\w+)', text)
  if match:
      unit = match.group(2)   # The unit (e.g., g, mg)
      return unit
  return None

def extract_number(text):
  # Use a regex pattern to extract the number part
  match = re.search(r'(\d+(?:[\.,]\d+)?)\s*(g|mg|%)', text)

  # Check if a match is found and extract the number
  if match:
      number = match.group(1)
      return float(number)
  else:
    return None

def correct_misread(text):
  # Correct 'O' or 'o' to '0' when followed by 'g', 'mg', or '%'
  corrected_text = re.sub(r'\b[oO](?=\s*(g|mg|%))', '0', text)

  # Correct 'l' or 'I' to '1' when followed by 'g', 'mg', or '%'
  corrected_text = re.sub(r'\b[lI](?=\s*(g|mg|%))', '1', corrected_text)

  return corrected_text

def get_fat(lines):
  target = r'\b(saturated\s*fat|saturated\s*fats|saturated\s*fatty\s*acids|total\s*saturated\s*fat|saturates|lemak\s*jenuh|lemak\s*jenuh\s*total|asam\s*lemak\s*jenuh|total\s*lemak\s*jenuh|lemak\s*trans)\b' 
  found = None
  for line in lines:
      if (bool(re.search(target, line.get("LineText"), re.IGNORECASE))):
          if (grams := extract_number(correct_misread(line.get("LineText")))):
             return grams, extract_unit(correct_misread(line.get("LineText")))
          line_pos_h = line.get("Words")[0].get("Top")
          # Find closest element by height
          found = None;
          last_check_dist = float('inf')
          for sub_line in lines: 
              if (sub_line.get("LineText") == line.get("LineText")):
                  continue
              found_pos_h = sub_line.get("Words")[0].get("Top")
              if (found is None or abs(line_pos_h - found_pos_h) < last_check_dist  ):
                  found = sub_line.get("Words")[0]
                  last_check_dist = abs(line_pos_h - found_pos_h)
          break
      
  if (not found is None):
    corrected_text = correct_misread(found.get("WordText"))
    if bool(re.search(r"\b(\d+\.?\d*)\s*(g|mg|%)\b", corrected_text)):
      return extract_number(corrected_text), extract_unit(corrected_text)

def get_sugar(lines):
  target = r'\b(gula|glukosa|sugar|glucose|sugars|glucoses)\b'; 
  found = None
  for line in lines:
      if (bool(re.search(target, line.get("LineText"), re.IGNORECASE))):
          print ("found", line)
          if (grams := extract_number(correct_misread(line.get("LineText")))):
             return grams, extract_unit(correct_misread(line.get("LineText")))
          line_pos_h = line.get("Words")[0].get("Top")
          # Find closest element by height
          found = None;
          last_check_dist = float('inf')
          for sub_line in lines: 
              if (sub_line.get("LineText") == line.get("LineText")):
                  continue
              found_pos_h = sub_line.get("Words")[0].get("Top")
              if (found is None or abs(line_pos_h - found_pos_h) < last_check_dist  ):
                  found = sub_line.get("Words")[0]
                  last_check_dist = abs(line_pos_h - found_pos_h)
          break
      
  if (not found is None):
    corrected_text = correct_misread(found.get("WordText"))
    if bool(re.search(r"\b(\d+\.?\d*)\s*(g|mg|%)\b", corrected_text)):
      return extract_number(corrected_text), extract_unit(corrected_text)


def get_natrium(lines):
  target = r'\b(sodium|natrium|salt|na|sodium chloride|table salt|garam|sodium bicarbonate|baking soda)\b'
  found = None
  for line in lines:
      if (bool(re.search(target, line.get("LineText"), re.IGNORECASE))):
          if (grams := extract_number(correct_misread(line.get("LineText")))):
             return grams, extract_unit(correct_misread(line.get("LineText")))
          line_pos_h = line.get("Words")[0].get("Top")
          print("found", line)
          # Find closest element by height
          found = None;
          last_check_dist = float('inf')
          for sub_line in lines: 
              if (sub_line.get("LineText") == line.get("LineText")):
                  continue
              found_pos_h = sub_line.get("Words")[0].get("Top")
              if (found is None or abs(line_pos_h - found_pos_h) < last_check_dist  ):
                  found = sub_line.get("Words")[0]
                  last_check_dist = abs(line_pos_h - found_pos_h)
          
          break
      
  if (not found is None):
    corrected_text = correct_misread(found.get("WordText"))
    if bool(re.search(r"\b(\d+\.?\d*)\s*(g|mg|%)\b", corrected_text)):
      return extract_number(corrected_text), extract_unit(corrected_text)

# print(get_natrium(text_raw))