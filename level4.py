import streamlit as st

def euclid(a1, b1, a2, b2):
    d = ((a1-a2)**2 + (b1-b2)**2)**0.5
    return d

def main():
    st.title("Euclidean distance Calculator")
    coordinate1 = st.text_input("Enter your co-ordinates separated by comma, e.g. 1.2, 4", key='point 1')
    coordinate2 = st.text_input("Enter your co-ordinates separated by comma, e.g. 1.2, 4", key='point 2')
    x1, y1 = map(float, coordinate1.split(','))
    x2, y2 = map(float, coordinate2.split(','))
    result = euclid(x1, y1, x2, y2)
    st.write(result)

if __name__=='__main__':
    main()