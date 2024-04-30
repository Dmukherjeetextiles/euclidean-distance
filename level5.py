## A streamlit app to calculate the Euclidean distance between two points

import streamlit as st

def euclid(x1,y1, x2, y2):
    ## calculate the distance by using the formula
    distance = ((x1-x2)**2+(y1-y2)**2)**0.5
    return distance

def main():
    st.title("Euclidean distance Calculator")
    ## Input for the calculation
    coordinate1 = st.text_input("Enter your co-ordinates separated by comma, e.g. 1.2, 4", key='point 1')
    coordinate2 = st.text_input("Enter your co-ordinates separated by comma, e.g. 1.2, 4", key='point 2')
    ## Button to run the script
    if st.button("calculate"):
        ## try-except block to catch any ValueError
        try:
            x1, y1 = map(float, coordinate1.split(','))
            x2, y2 = map(float, coordinate2.split(','))
            result = euclid(x1, y1, x2, y2)
            st.write(result)
        except ValueError:
            st.write("Please enter valid co-ordinates")

if __name__=='__main__':
    main()