
!pip install -q streamlit
import streamlit as st
st.write("Largest of three numbers")
def main():
  st.title("find the largest number")
  st.write("Enter three numbers and clikc the buttonto find the largerst number.")
import pandas as pd
import numpy as np
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
 largest = num1
elif (num2 >= num1) and (num2 >= num3):
 largest = num2
else:
 largest = num3
print("The largest number between",num1,",",num2,"and",num3,"is",largest)
