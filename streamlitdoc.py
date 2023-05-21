import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title="Startup Analysis",layout="wide")
st.title('Startup Dashboard')
st.header("I am learning Straamlit")
st.subheader("And i am loving it")
st.write('Always writing')

st.markdown("""### My_faviourte_Movies
-Hamshakla
-Race 3
-Housefull
""")
st.markdown('''My_faviourte_Movies
-Hamshakla
-Race 3
-Housefull''')
st.code("""
def normailis(input):
    return input**2
x=normalise(2)
""")

st.latex("(X^2+Y^2)^2=23")
df=pd.DataFrame({
    "name":["Prashant","Pooja","Ashok","Savita","Rajveer"],
    "Marks":[76,67,88,88,98]
})
st.dataframe(df)

col1,col2,col3=st.columns(3)

with col1:
    st.image("IMG_20211121_110717.jpg")

with col2:
    st.image('IMG_20211121_110717.jpg')
with col3:
    st.image('IMG_20211121_110717.jpg')
st.error("Loginf failed")
st.info("Loginf failed")
st.text_input("Enter a number")
st.number_input("ENTER THE MOBILE")
st.date_input("Enter date")
