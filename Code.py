import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st



class plot:
    def Count_Record(self,data):
        sns.set(font_scale=1.5)
        st.header("Overview of dataset.")
        st.write(data.head(10))
        fig, ax = plt.subplots(figsize=(15,10))
        region_count = sns.countplot(data=data, x="region")
        region_count.set_xticklabels(region_count.get_xticklabels(), rotation=20)
        st.pyplot(fig)

    def General_Overview(self,data):
        sns.set(font_scale=1.0)
        fig, ax = plt.subplots(5, 1, figsize=(30, 40), )
        col = ['fertility', 'life', 'population', 'child_mortality', 'gdp']
        for index, col1 in enumerate(col):
            print(index, col1)
            mean1 = data.groupby("Year")[col1].mean()
            mean_plt = sns.barplot(x=mean1.index, y=mean1.values, ax=ax[int(index)])
            mean_plt.set(xlabel="Year")
            mean_plt.set_ylabel(col1, fontsize=50)
            mean_plt.set_yticklabels(mean_plt.get_ylabel(),size = 10)
            plt.setp(mean_plt.get_xticklabels(), rotation=45)
            fig.tight_layout(pad=2.0)
            print("")
        st.pyplot(fig)


    def Region_vs_All(self,data,Name=None):
        sns.set(font_scale=1)
        if Name==None:
            fig, ax = plt.subplots(5, 1, figsize=(25, 35))
            col = ['fertility', 'life', 'population', 'child_mortality', 'gdp']
            for index, col1 in enumerate(col):
                print(index, col1)
                mean1 = data.groupby("region")[col1].mean()
                mean_plt = sns.barplot(x=mean1.index, y=mean1.values, ax=ax[int(index)])
                mean_plt.set_ylabel(col1, fontsize=50)
                plt.setp(mean_plt.get_xticklabels(), rotation=10)
                fig.tight_layout(pad=2.0)
            st.pyplot(fig)
        else:
            sub_data = data.loc[data.region == Name]
            fig, ax = plt.subplots(5, 1, figsize=(30, 40))
            col = ['fertility', 'life', 'population', 'child_mortality', 'gdp']
            for index, col1 in enumerate(col):
                print(index, col1)
                mean1 = sub_data.groupby("Year")[col1].mean()
                mean_plt = sns.barplot(x=mean1.index, y=mean1.values, ax=ax[int(index)])
                mean_plt.set_ylabel(col1, fontsize=50)
                plt.setp(mean_plt.get_xticklabels(), rotation=45)
                fig.tight_layout(pad=2.0)
            st.pyplot(fig)


    def Region_vs_Box(self,data):
        print("Provide some indication of the data's symmetry and skewness." +
              "Unlike many other methods of data display.\nBoxplots show outliers")
        col = ['fertility', 'life', 'population', 'child_mortality', 'gdp']
        fig, ax = plt.subplots(5, 1, figsize=(15, 25))
        for index, col1 in enumerate(col):
            sns.boxplot(data=data, x="region", y=col1, orient="v", ax=ax[index])

    def County_wise_Analysis(self,data, Name):
        # sns.set(font=30)
        sns.set(font_scale=3)
        sub_data = data.loc[data.Country == Name]
        if sub_data.shape[0] == 0:
            return st.write("Please check the spelling of country..")
        fig, ax = plt.subplots(3, 2, figsize=(30, 35))

        sns.lineplot(data=sub_data, x="Year", y="fertility", ax=ax[0][0])
        sns.lineplot(data=sub_data, x="Year", y="life", ax=ax[0][1])
        sns.lineplot(data=sub_data, x="Year", y="population", ax=ax[1][0])
        sns.lineplot(data=sub_data, x="Year", y="child_mortality", ax=ax[1][1])
        sns.lineplot(data=sub_data, x="Year", y="gdp", ax=ax[2][0])

        st.pyplot(fig)
        # sns.set(font_scale=None)
class main_class:
    def main(self,data,input1=None,input2=None):
        try:
            obj=plot()
            if input1=="Select":
                return obj.Count_Record(data)
            if input1=="General Overview":
                return obj.General_Overview(data)
            elif input1 == "region wise":
                return obj.Region_vs_All(data,input2)
            elif input1 == "Based On Country":
                return obj.County_wise_Analysis(data,input2)
        except Exception as e:
            st.write("Exception",e)

