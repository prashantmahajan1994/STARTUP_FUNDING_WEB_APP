import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import time

df=pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

def load_overall_analysis():
    st.title('Overall Analysis')
   #Total Startup funded
    total_fund=round(df.amount.sum())
    #max Startup funded
    max_funded=round(df.amount.max())
    #avg startup funded
    avg_funded=round(df.amount.mean())
    #Total startup funded
    total_funded_startup=df.startup.nunique()

    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Toal",str(total_fund)+"Cr")
    with col2:
        st.metric("Toal" ,str(max_funded) + "Cr")
    with col3:
        st.metric("Toal",str(avg_funded) + "Cr")
    with col4:
        st.metric("Toal",str(total_funded_startup))

    st.header('MoM graph')
    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
        temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
        fig3, ax3 = plt.subplots()
        ax3.plot(temp_df['x_axis'], temp_df['amount'])

        st.pyplot(fig3)
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')









def load_investor_details(investor):
    st.title(investor)
    last5_df=df[df.investors == investor].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader("Most recent investment")
    st.dataframe(last5_df)
    big_series=df[df.investors.str.contains(investor)].groupby('startup').amount.sum().sort_values(ascending=False).head()

    col1,col2=st.columns(2)
    with col1:
        st.subheader("Biggest investment")
        st.dataframe(big_series)
        fig,ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)

    with col2:
        vertical_series=df[df.investors.str.contains(investor)].groupby('vertical').amount.sum().sort_values(
            ascending=False).head()
        fig1,ax1=plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index,autopct="%0.01f%%")
        st.pyplot(fig1)
    print(df.info())







st.sidebar.title("Startup Funding Analysis")
option=st.sidebar.selectbox('Select one',['Overall Analysis','StartUp','Investor'])
if option == 'Overall Analysis':
    bt1=st.sidebar.button("Find Overall Analysis")
    if bt1:
        load_overall_analysis()
elif option == 'StartUp':
    pass
else:
    selected_investor = st.sidebar.selectbox('Select one investors',df.investors.str.split(",").sum())
    btn2 = st.sidebar.button('Find Investors Details')
    if btn2:
        load_investor_details(selected_investor)



