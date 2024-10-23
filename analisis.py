gula_min_category = {
    "A": 1,
    "B": 5,
    "C": 10,
    "D": 999
}

lemak_min_category = {
    "A": .7,
    "B": 1.2,
    "C": 2.8,
    "D": 999
}

code = ["A", "B", "C", "D"]

def analisis(gula, garam, lemak):
    gula_grade = lemak_grade = None
    if (gula <= gula_min_category["A"]):
        gula_grade = 0
    elif (gula <= gula_min_category["B"]):
        gula_grade = 1
    elif (gula <= gula_min_category["C"]):
        gula_grade = 2
    else:
        gula_grade = 3
    
    if (lemak <= lemak_min_category["A"]):
        lemak_grade = 0
    elif (lemak <= lemak_min_category["B"]):
        lemak_grade = 1
    elif (lemak <= lemak_min_category["C"]):
        lemak_grade = 2
    else:
        lemak_grade = 3
    
    final = max(gula_grade, lemak_grade)
    return code[final]
