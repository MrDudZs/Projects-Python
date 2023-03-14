#============================#
# Dehydration Diagnosis Bot
#============================#

# Prompts
Welcome_prompt = "Welcome, what would you like to do? \n -To list all patients, press 1 \n -To run a new diagnosis, press 2\n -To quit, press Q\n"

Name_prompt = "What is the patient's name?\n"

Option_prompt = "How is the patients's general apperance? \n 1: Normal apperance \n 2: Irritable or lethargic \n Q: Return to menu \n"

Eye_prompt = "How are the patients eyes? \n - 1: Eyes normal or slightly sunken \n - 2: Eyes very sunken \n"

Skin_prompt = "How is the skin when pinched? \n - 1: Normal skin pinch \n - 2: Slow skin pinch \n "

# Results:
severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"

# Shows stored paitents and diagnosis
patients_and_diagnoses = [
    "Bill: Severe dehydration",
    "Lilly: Some dehydration",
    "Adri: No dehydration\n"
]


# Main option 1
def list_patients():
    for patient in patients_and_diagnoses:
        print(patient)

# Saves new diagnosis and patients name
def save_new_diagnosis(Name, diagnosis):
    if Name == "" or diagnosis == "": 
        print("Could not save patient and diagnosis due to invalid input")
        return
    
    final_diagnosis = Name + " - " + diagnosis
    patients_and_diagnoses.append(final_diagnosis)
    print("Final diagnosis:", final_diagnosis, "\n")


# Assessments
def assess_eyes(eyes):
    if eyes == "1":
        return no_dehydration
    
    elif eyes == "2":
        return severe_dehydration
    
    # Returns empty string if in put != 1 or 2
    else:
        return ""
    
def assess_skin(skin):
    if skin == "1":
        return some_dehydration
    
    elif skin == "2":
        return severe_dehydration
    
    # Returns empty string if in put != 1 or 2
    else:
        return ""


# Assess apperiance
def assess_appearance():
    apperance = input(Option_prompt)
    if apperance == "1":
        # Assess eyes
        eyes = input(Eye_prompt)
        return assess_eyes(eyes)

    elif apperance == "2":
        # Assess skin
        skin = input(Skin_prompt)
        return assess_skin(skin)
    
    else:
        # Returns empty string if in put != 1 or 2
        return ""


# Main option 2
def start_new_diagnosis():
    Name = input(Name_prompt)
    diagnosis = assess_appearance()
    save_new_diagnosis(Name, diagnosis)


# Prints opening selection
def main():
    while(True):
        selcetion = input(Welcome_prompt)
        if selcetion == "1":
            # List all patients
            list_patients()
        elif selcetion == "2":
            # Start a new diagnosis
            start_new_diagnosis()
        elif selcetion == "Q":
            return

main()
