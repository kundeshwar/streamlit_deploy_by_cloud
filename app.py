import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
#loading saved 
diabeties_load = pickle.load(open("C:/Users/kunde/all vs code/ml prject/web_page_multiple_dieses/diabeties.pkl", "rb"))
brest_load = pickle.load(open("C:/Users/kunde/all vs code/ml prject/web_page_multiple_dieses/breast_cancer.pkl", "rb"))

with st.sidebar:
    selected = option_menu("Multiple Disease Prediction System", 
    ["Diabetes Prediction", "Breast Cancer Prediction"],
    icons=["Activity", "Calendar heart fill"], default_index=1)

#first we will creat diabetes
if (selected== "Diabetes Prediction"):
    def diabetes_pred(input_data):
       #to will giv e reshape
        x_arra = np.asarray(input_data)
        x_reshape = x_arra.reshape(1, -1)
        predt_y = diabeties_load.predict(x_reshape)
        #print(predt_y)
        if predt_y[0] == 0:
            return "The person is not diabetes"
        else:
            return "The person is diabetes"
    #using and creating stramlit

    def main_d():
    #giving title
        st.title("DIABETES PREDICTION BY ML(KP MODEL)")

        #giting input values 
        Pregnancies = st.text_input("Number of Pregnancies")
        Glucose = st.text_input("Number of Glucose")
        BloodPressure = st.text_input("BloodPressure Level")
        SkinThickness = st.text_input("SkinThickness values ")
        Insulin = st.text_input("Insulin Level")
        BMI_i = st.text_input("BMI(body mass index)")
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction value")
        age = st.text_input("Age of you")

        # code of prediction 
        diagnosis = ""

        #creating button
        if st.button("Diabetes Test Result"):
            diagnosis = diabetes_pred([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI_i, DiabetesPedigreeFunction, age])
    
        st.success(diagnosis)
    if __name__=='__main__':
        main_d()


if (selected == "Breast Cancer Prediction"):
#third for brast cancer
    def breast_pred(input_data):
        #to will giv e reshape
        x_arra = np.asarray(input_data)
        x_reshape = x_arra.reshape(1, -1)
        predt_y = diabeties_load.predict(x_reshape)
        #print(predt_y)
        if predt_y[0] == 0:
            return "The person has melanoma cancer"
        else:
            return "The person has Breast cancer"

    def main_breast():
        #giving title
        st.title("BREAST CANCER DISEASE PREDICTION BY ML(kp)")
        #giting input values
        radius_mean             =  st.text_input( "radius_mean  of patient")
        texture_mean            =  st.text_input( "texture_mean of patient")
        perimeter_mean          =  st.text_input( "perimeter_mean of patient")
        area_mean               =  st.text_input( "area_mean of patient")
        smoothness_mean         =  st.text_input( "smoothness_mean of patient")
        compactness_mean        =  st.text_input( "compactness_mean of patient")
        concavity_mean          =  st.text_input( "concavity_mean of patient")
        concave_points_mean     =  st.text_input( "concave_points_mean  of patient")
        symmetry_mean           =  st.text_input( "symmetry_mean  of patient")
        fractal_dimension_mean  =  st.text_input( "fractal_dimension_mean of patient")
        radius_se               =  st.text_input( "radius_se of patient")
        texture_se              =  st.text_input( "texture_se of patient")
        perimeter_se            =  st.text_input( "perimeter_se  of patient")
        area_se                 =  st.text_input( "area_se  of patient")
        smoothness_se           =  st.text_input( "smoothness_se of patient")
        compactness_se          =  st.text_input( "compactness_se of patient")
        concavity_se            =  st.text_input( "concavity_se of patient")
        concave_points_se       =  st.text_input( "concave_points_se of patient")
        symmetry_se             =  st.text_input( "symmetry_se  of patient")
        fractal_dimension_se    =  st.text_input( "fractal_dimension_se of patient")
        radius_worst            =  st.text_input( "radius_worst of patient")
        texture_worst           =  st.text_input( "texture_worst of patient")
        perimeter_worst         =  st.text_input( " perimeter_worst of patient")
        area_worst              =  st.text_input( "area_worst of patient")
        smoothness_worst        =  st.text_input( "smoothness_worst of patient")
        compactness_worst       =  st.text_input( "compactness_worst of patient")
        concavity_worst         =  st.text_input( "concavity_worst of patient")
        concave_points_worst    =  st.text_input( "concave_points_worst of patient")
        symmetry_worst      =  st.text_input("symmetry_worst of patient")
        fractal_dimension_worst = st.text_input(" fractal_dimension_worst of patient")
        # code of prediction 
        diagnosis = ""

        #creating button
        if st.button("Breast Classification Result"):
            diagnosis = breast_pred([radius_mean, texture_mean, perimeter_mean, area_mean,smoothness_mean, compactness_mean, concavity_mean,
           concave_points_mean, symmetry_mean, fractal_dimension_mean,radius_se, texture_se, perimeter_se, area_se, smoothness_se,compactness_se, concavity_se, concave_points_se, symmetry_se,
           fractal_dimension_se, radius_worst, texture_worst,perimeter_worst, area_worst, smoothness_worst,compactness_worst, concavity_worst, concave_points_worst,symmetry_worst, fractal_dimension_worst])

        st.success(diagnosis)

    if __name__== "__main__":
        main_breast()










