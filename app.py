import streamlit as st
import Code
import pandas as pd
global data

def Start(data):
    Country = set(data.Country)
    # year = set(data.Year)
    region = set(data.region)
    Main=Code.main_class()
    st.title("Gapminder Analysis(Kaggle)")
    st.sidebar.title("Analysis Based On")
    Option=st.sidebar.selectbox("Select Option",("Select","Based On Country","Based On Region","General Overview"))
    if Option=="Select":
        Main.main(data,"Select")
    elif Option=="General Overview":
        st.header("General Overview(World)")
        Main.main(data,"General Overview")
    elif Option=="Based On Region":
        st.header("Based On Region(Overview)")
        Main.main(data,"region wise", None)
        region = st.sidebar.selectbox("Select Region", tuple(region))
        st.header("Analysis of "+region+ " region.")
        Main.main(data,"region wise", region)
    elif Option=="Based On Country":
        st.header("Based On Country")
        Country = st.sidebar.selectbox("Select Country", tuple(Country))
        st.header("Analysis of " + Country )
        Main.main(data,"Based On Country",Country)
        print("Done")

if __name__=="__main__":
    #streamlit run app.py
    # @st.cache
    def load_dataset():
        data = pd.read_csv("clean_data.csv")
        print("loaded")
        return data
    data = load_dataset()
    Start(data)