import os
import streamlit as st
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI

# Milestone 1: Initialize API and Models
# Activity 1.1: Set up Google GenAI API credentials
genai.configure(api_key='AIzaSyC57ekJI6-i1S6MjxMMYi2nDOH2Rh9gyP0')

# Activity 1.2: Print available models for verification
model = genai.list_models()
for model in model:
  print(model)

# Activity 1.3: Initialize the Google Generative AI model
llm = GoogleGenerativeAI(model="models/gemini-1.5-pro-latest", google_api_key='AIzaSyC57ekJI6-i1S6MjxMMYi2nDOH2Rh9gyP0', temperature=1.0)


# Milestone 3: Define Prompt Template for Nutritional Information
# Activity 3.1: Create prompt template for nutritional information
nutritional_info_template = PromptTemplate(
  input_variables=["food_items"],
  template="""Provide detailed nutritional information for the following food items: {food_items}.
  Include macronutrients (protein, fat, carbohydrates), micronutrients (vitamins, minerals), and calorie content."""
)


# Milestone 4: Collect User Inputs
# Activity 4.1: Collect food items input from user
def get_food_items_input():
  with st.form("food_items_input_form"):
    food_items = st.text_area("Enter Food Items (separate by commas):", "")
    submitted = st.form_submit_button("Get Nutritional Information")
    if submitted:
      return {"food_items": food_items}

# Milestone 5: Generate AI Response
# Activity 5.1: Generate nutritional information response based on input data
def get_nutritional_info_response(input_data):
  if input_data is None:
    return "Error: No food items provided."

  prompt = nutritional_info_template.format(**input_data)
  response = llm(prompt)
  return response

# Milestone 6: Build Streamlit User Interface
# Activity 6.1: Create main Streamlit application title
st.title("NutriAI - Instant Nutritional Information")

# Activity 6.2: Collect food items and display nutritional information
input_data = get_food_items_input()
if input_data:
  with st.spinner("Fetching nutritional information..."):
    response = get_nutritional_info_response(input_data)
    st.subheader("Nutritional Information:")
    st.write(response)
