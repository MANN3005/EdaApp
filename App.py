import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
from PIL import Image

st.set_option('deprecation.showPyplotGlobalUse', False)

# df = pd.read_csv('SampleSuperstore.csv')
st.title('Visualization App')
st.title('Upload your Data To analyze')

uploaded_file = st.file_uploader("Upload File")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
title = st.text_input('What are you Analyzing?', 'Name of Dataset')
st.title('Exploratory Data Analysis - {t}'.format(t=title))
st.text("Data Visualization App for a {t} Dataset".format(t=title))
StoreImage = Image.open("Superstore.jpg")
st.image(StoreImage, caption= "{t}".format(t=title), width = 500)
st.write("People who love to directly start train models can use this app to skip coding for EDA :sunglasses:")
st.write("\nThe Basic Structure of the Dataset")

Basic_Info = st.radio(
    " Select Any of this ",
    ('Shape of Dataset','Head of Dataset','Describe Dataset')    
)

if Basic_Info == 'Shape of Dataset':
    st.write("Shape of Dataset: ",df.shape)
    
elif Basic_Info == 'Head of Dataset':
    st.write(df.head())
    

elif Basic_Info == 'Describe Dataset':
    st.write(df.describe())
st.sidebar.header('Visualize Data According to your Need')

Column1 = st.sidebar.selectbox('Column-1',df.columns.tolist())
Column2 = st.sidebar.selectbox('Column-2',df.columns.tolist())

Type_Of_graph = st.sidebar.selectbox(
    'What Type of Graph Would You like to see?',
    ('LineGraph','BarGraph','AreaGraph','Histogram','PieChart','ScatterPlot','ViolinPlot','JitterPlot','KdePlot')
)

Submit_First = st.sidebar.button('Visualize {C1}'.format(C1=Column1),key ='first')
Submit_Second = st.sidebar.button('Visualize {C2}'.format(C2=Column2), key = 'second')
Submit_Both = st.sidebar.button("Visualize {C1} vs {C2}".format(C1=Column1,C2=Column2))

if Submit_First:
    if Type_Of_graph == 'LineGraph':
        st.line_chart(df[Column1])
    if Type_Of_graph == 'BarGraph':
        st.bar_chart(df[Column1])
    if Type_Of_graph == 'AreaGraph':
        st.area_chart(df[Column1])
    if Type_Of_graph == 'Histogram':
        st.write(plt.hist(df[Column1]))
        st.pyplot()
    if Type_Of_graph == 'PieChart':
        st.write(df[Column1].value_counts().plot.pie())
        st.pyplot()
    if Type_Of_graph == 'ScatterPlot':
        st.error('Needs two Variables, Try other Visualization')
        # st.write(plt.scatter(df[Column1]))
    if Type_Of_graph == 'ViolinPlot':
        st.write(sns.violinplot(df[Column1]))
        st.pyplot()
    if Type_Of_graph == 'JitterPlot':
        st.error('Needs two Variables, Try other Visualization')
    if Type_Of_graph == 'KdePlot':
        st.write(sns.kdeplot(df[Column1]))
        st.pyplot()

if Submit_Second:
    if Type_Of_graph == 'LineGraph':
        st.line_chart(df[Column2])
    if Type_Of_graph == 'BarGraph':
        st.bar_chart(df[Column2])
    if Type_Of_graph == 'AreaGraph':
        st.area_chart(df[Column2])
    if Type_Of_graph == 'Histogram':
        st.write(plt.hist(df[Column2]))
        st.pyplot()
    if Type_Of_graph == 'PieChart':
        st.write(df[Column2].value_counts().plot.pie())
        st.pyplot()
    if Type_Of_graph == 'ScatterPlot':
        st.error('Needs two Variables, Try other Visualization')
        # st.write(plt.scatter(df[Column1]))
    if Type_Of_graph == 'ViolinPlot':
        st.write(sns.violinplot(df[Column2]))
        st.pyplot()
    if Type_Of_graph == 'JitterPlot':
        st.error('Needs two Variables, Try other Visualization')
    if Type_Of_graph == 'KdePlot':
        st.write(sns.kdeplot(df[Column2]))
        st.pyplot()

if Submit_Both:
    if Type_Of_graph == 'LineGraph':
        Linb = alt.Chart(df).mark_line().encode(
            x=Column1,
            y=Column2,
        )
        st.altair_chart(Linb, use_container_width=True)
    if Type_Of_graph == 'BarGraph':
        graph = alt.Chart(df).mark_bar().encode(
        x = Column1, y = Column2 
        )
        st.altair_chart(graph, use_container_width=True)
    if Type_Of_graph == 'AreaGraph':
        area = alt.Chart(df).mark_area().encode(
            x = Column1, y = Column2
        )
        st.altair_chart(area, use_container_width=True)
    if Type_Of_graph == 'Histogram':
        area = alt.Chart(df).mark_bar().encode(
            x = Column1, y = Column2,
        )
        st.altair_chart(area, use_container_width=True)
    if Type_Of_graph == 'PieChart':
        st.error('Does not take more than One Argument')
        st.write(df[Column1].value_counts().plot.pie())
        st.pyplot()
        st.write(df[Column2].value_counts().plot.pie())
        st.pyplot()                    
    if Type_Of_graph == 'ScatterPlot':
        plt.scatter(df[Column1],df[Column2])
        st.pyplot()
    if Type_Of_graph == 'ViolinPlot':
        st.error('Does not take more than one variable')
        st.write(sns.violinplot(df[Column1]))
        st.pyplot()
        st.write(sns.violinplot(df[Column2]))
        st.pyplot()
    if Type_Of_graph == 'JitterPlot':
        sns.stripplot(x=Column1, y=Column2, data=df,jitter= True)
        st.pyplot()
    if Type_Of_graph == 'KdePlot':
        st.error('Does not take more than one variable')
        st.write(sns.kdeplot(df[Column1]))
        st.pyplot()
        st.write(sns.kdeplot(df[Column2]))    
        st.pyplot()
    
    