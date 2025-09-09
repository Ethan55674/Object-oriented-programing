

#letter grade -> numeric value
grade_map = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "D-": 0.7,
    "F": 0.0
}

def letter_to_number(letter):
    
    #Convert a letter grade into a number.
    #Uses .upper() so input can be lowercase or uppercase.
    return grade_map.get(letter.upper())

def number_to_letter(num):
    
    #Convert a numeric average back into a letter grade.
    
    
    if num >= 3.7: 
        return "A"
    if num >= 3.3: 
        return "B+"
    if num >= 3: 
        return "B"
    if num >= 2.7: 
        return "B-"
    if num >= 2.3: 
        return "C+"
    if num >= 2: 
        return "C"
    if num >= 1.7: 
        return "C-"
    if num >= 1.3: 
        return "D+"
    if num >= 1: 
        return "D"
    if num >= .7: 
        return "D-"
    if num < .7: 
        return "F"
