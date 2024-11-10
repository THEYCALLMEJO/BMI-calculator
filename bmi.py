import streamlit as st
# give a tile for out project 
st.title("Welcome to BMI Calaculator 👋")

# let's get the weight of a users in kgs
weight = st.number_input('Enter your weight(in kgs)')

# take height inpu 
# radio button to choice height format 
status = st.radio("Select your height format", ('cm', 'm', 'ft'))
bmi = -float('inf')
if status == 'cm':
    height = st.number_input('Enter your height in centimeters')
    try:
        bmi = weight / (height/100)**2
    except:
        st.text("Please enter valid height!")

elif status == 'm':
    height = st.number_input('Enter your height in meters')
    try:
        bmi = weight / (height)**2
    except:
        st.text("Please enter valid height!") 

else:
    height = st.number_input('Enter your height in feets')
    try:
        bmi = weight / (height/3.28084)**2
    except:
        st.text("Please enter valid height!")

st.write(f'') 
st.write(f'')
btn = st.button('Calculate BMI')

if btn:
    st.subheader(f'Your BMI is: {bmi:.1f}')

    if bmi < 18.5:
       st.error('You are Underweight')
    elif 18.5 <= bmi < 25:
        st.success("You're Healthy")
    elif 25 <= bmi < 30:
        st.warning("You are Overweight")
    else:
        st.error("You are Obese")

st.markdown('---')
st.write("Made by Eyosias Mulugeta © 2024")

 #https://github.com/THEYCALLMEJO/BMI-calculator.git
    










