import numpy as np
import pickle
import streamlit as st

classifier = pickle.load(open("C:/Users/admin/Desktop/Portfolio Projects/classification/credit_score_classification_model.sav", "rb"))

def credit_score_classifier(input):
    
    for i in range(len(input)):
        if input[i] == 'Female'  or input[i] == 'Single' or input[i] == 'single'  or input[i] == 'Rented':
            input[i] = 0
        else:
            if input[i] == 'Male' or input[i] == 'Married' or input[i] == 'married' or input[i] == 'Owned':
                input[i] = 1


    if input[3] == "High School Diploma" or input[3] == "Diploma":
        new_input = input + [0,0,0,1,0]
        del new_input[3]
    elif input[3] == "Master's Degree" or input[3] == "Master's":
        new_input = input + [0,0,0,0,1]
        del new_input[3]
    elif input[3] == "Bachelor's Degree" or input[3] == "Bachelor's":
        new_input = input + [0,1,0,0,0]
        del new_input[3]
    elif input[3] == "Doctorate":
        new_input = input + [0,0,1,0,0]
        del new_input[3]
    else:
        new_input = input + [1,0,0,0,0]
        del new_input[3]
        

    new_input = np.asarray(new_input)
    input_data_reshaped = new_input.reshape(1,-1)

    input_pred = classifier.predict(input_data_reshaped)

    if input_pred[0] == 0:
        return "Ooops, Your Credit Score is Low!"
    elif input_pred[0] == 1:
        return "Well Done, Your Credit Score is Average!"
    else:
        return "Superb, Your Credit Score is High!"
    
    
    
def main():
    
    # Setting page title
    st.title("Credit Score Web App")
    
    # Defining inputs required from user
    age = st.text_input("Age in Years")
    gender = st.text_input("Gender - 'Male' or 'Female'")
    income = st.text_input("Yearly Income")
    education = st.text_input("Highest Educational Qualification - 'Diploma' , 'Master\'s Degree', 'Bachelor's Degree', 'Associate\'s Degree' or 'Doctorate'")
    marital_status = st.text_input("Marital Status")
    n_children = st.text_input("Number of Children")
    home_ownership = st.text_input(" Home Ownership Status - 'Rented' or 'Owned'")
    
    # Initializing credit score
    credit_score = ""
    
    if st.button("Check Score"):
        credit_score = credit_score_classifier([age,gender,income,education,marital_status,n_children,home_ownership])
        
    st.success(credit_score)
    
    
    
if __name__ == '__main__':
    main()