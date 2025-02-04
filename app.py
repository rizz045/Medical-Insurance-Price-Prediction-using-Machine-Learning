# App code

import numpy as np
import pickle 
import streamlit as st

#Load the model
with open("insurance_model.pkl","rb") as file:
    loaded_model = pickle.load(file)

def predict_charges(input_data):
    try:
        pred_in = 0
        inp_data_array = np.array(input_data, dtype=float)
        inp_data_reshape = inp_data_array.reshape(1, -1)
        pred_in = loaded_model.predict(inp_data_reshape)
        if pred_in == 0:
            return "Something went wrong try to put different values in the input field."
        else:
            return pred_in
    except:
        return "Invalid input. Please try re-enter the values for all the fields."

def main():
    st.title("An App That Predicts Insurance Amount")
    st.header("Enter the following details")

    #input values from the user
    age = st.text_input("Enter the age of a person (18-62)", value='25')
    bmi = st.text_input("BMI of a Person (15.96 - 53.13)", value='27')
    children = st.text_input("Enter the number of children (0-5)", value='0')
    smoker = st.text_input("0-NO or 1-YES", value='1')

    answer = ""

    if st.button("Predict Charges"):
        answer = predict_charges([age, bmi, children, smoker])
        st.success(f"The charges would be around : ${answer[0]:.2f}")

if __name__ == '__main__':
    main()
