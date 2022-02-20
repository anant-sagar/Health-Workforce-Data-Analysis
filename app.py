import streamlit as st

import pandas as pd
from visualization import *
from AnalyseData import Analyse


st.title('Health Workforce Analysis')
st.text("")
st.text("")
st.image("logo.jpg")
st.markdown("---")
sidebar = st.sidebar
sidebar.title('Health Workforce Analysis')


analyseDoctors = Analyse(path='datasets/medicalDoctors.csv')
analyseNurse = Analyse(path='datasets/nursingAndMidwife.csv')
analysePharmacist = Analyse(path='datasets/pharmacists.csv')
analyseDentist = Analyse(path='datasets/dentists.csv')


def viewDataset():

    with st.spinner("Loading Data..."):
        dataframes = [analyseDoctors.getDataframe(), analyseNurse.getDataframe(
        ), analyseDentist.getDataframe(), analysePharmacist.getDataframe()]
        for dataframe, name in zip(dataframes, ['Medical Doctors Dataset', 'Nurses and Midwives Dataset', 'Pharmacists Dataset', 'Dentists Dataset']):
            st.markdown('# ')
            st.header(f"Details of {name}")
            st.markdown('---')
            st.dataframe(dataframe)

            st.markdown('---')
            cols = st.beta_columns(4)
            cols[0].markdown("### No. of Rows :")
            cols[1].markdown(f"# {dataframe.shape[0]}")
            cols[2].markdown("### No. of Columns :")
            cols[3].markdown(f"# {dataframe.shape[1]}")
            st.markdown('---')

            st.header('Summary')
            st.dataframe(dataframe.describe())
            st.markdown('---')

            types = {'object': 'Categorical',
                     'int64': 'Numerical', 'float64': 'Numerical'}
            types = list(map(lambda t: types[str(t)], dataframe.dtypes))
            st.header('Dataset Columns')
            for col, t in zip(dataframe.columns, types):
                st.markdown(f"### {col}")
                cols = st.beta_columns(4)
                cols[0].markdown('#### Unique Values :')
                cols[1].markdown(f"# {dataframe[col].unique().size}")
                cols[2].markdown('#### Type :')
                cols[3].markdown(f"## {t}")


def doctorAnalysis():
    st.header('Medical Doctors Analysis')

    n = st.select_slider("Select No.", [10, 20, 40, 60, 100, 194])

    st.plotly_chart(plotBar(analyseDoctors.getTopTooltop(n),
                            title='Leading Countries in no. of Medical Doctors per 10,000 population (Average)', xlabel='Country Name', ylabel='No. of Doctors'))

    st.plotly_chart(plotBar(analyseDoctors.getBottomTooltop(n),
                            title='Countries having minimum no. of Medical Doctors per 10,000 population (Average)', xlabel='Country Name', ylabel='No. of Doctors'))

    loc = st.selectbox("Select Location", analyseDoctors.getLocations())
    st.plotly_chart(plotLine(analyseDoctors.getTopYearData(loc, n),
                             title='Change in No. of Medical Doctors over years', xlabel='Year', ylabel='No. of Doctors'))

    year = st.selectbox("Select Year", analyseDoctors.getYears())
    st.plotly_chart(plotBar(analyseDoctors.getTopLocationData(year, n),
                            title='Leading Countries in no. of Medical Doctors per 10,000 population', xlabel='Country Name', ylabel='No. of Doctors'))

    st.plotly_chart(plotBar(analyseDoctors.getBottomLocationData(year, n),
                            title='Countries having minimum no. of Medical Doctors per 10,000 population', xlabel='Country Name', ylabel='No. of Doctors'))

    st.plotly_chart(plotChloropeth(analyseDoctors.getMapData(
        year), title="Medical Doctor No. per 10,000 of Population in world"))


def nurseAnalysis():
    st.header('Nurses and Midwives Analysis')

    n = st.select_slider("Select No.", [10, 20, 40, 60, 100, 194])

    st.plotly_chart(plotBar(analyseDoctors.getTopTooltop(n),
                            title='Leading Countries in no. of Nurses and Midwives per 10,000 population (Average)', xlabel='Country Name', ylabel='No. of Nurses'))

    st.plotly_chart(plotBar(analyseDoctors.getBottomTooltop(n),
                            title='Countries having minimum no. of Nurses and Midwives per 10,000 population (Average)', xlabel='Country Name', ylabel='No. of Nurses'))

    loc = st.selectbox("Select Location", analyseDoctors.getLocations())
    st.plotly_chart(plotLine(analyseDoctors.getTopYearData(loc, n),
                             title='Change in No. of Nurses and Midwives over years', xlabel='Year', ylabel='No. of Nurses'))

    year = st.selectbox("Select Year", analyseDoctors.getYears())
    st.plotly_chart(plotBar(analyseDoctors.getTopLocationData(year, n),
                            title='Leading Countries in no. of Nurses and Midwives per 10,000 population', xlabel='Country Name', ylabel='No. of Nurses'))

    st.plotly_chart(plotBar(analyseDoctors.getBottomLocationData(year, n),
                            title='Countries having minimum no. of Nurses and Midwives per 10,000 population', xlabel='Country Name', ylabel='No. of Nurses'))

    st.plotly_chart(plotChloropeth(analyseDoctors.getMapData(
        year), title="Nurses and Midwvies No. per 10,000 of Population in world"))


def dentistAnalysis():
    st.header('Dentists Analysis')

    n = st.select_slider("Select No.", [10, 20, 40, 60, 100, 194])

    st.plotly_chart(plotBar(analyseDoctors.getTopTooltop(n),
                            title='Leading Countries in no. of Dentists per 10,000 population (Average)', xlabel='Country Name', ylabel='No. of Dentists'))

    st.plotly_chart(plotBar(analyseDoctors.getBottomTooltop(n),
                            title='Countries having minimum no. of Dentists per 10,000 population (Average)', xlabel='Country Name', ylabel='No. of Dentists'))

    loc = st.selectbox("Select Location", analyseDoctors.getLocations())
    st.plotly_chart(plotLine(analyseDoctors.getTopYearData(loc, n),
                             title='Change in No. of Dentists over years', xlabel='Year', ylabel='No. of Dentists'))

    year = st.selectbox("Select Year", analyseDoctors.getYears())
    st.plotly_chart(plotBar(analyseDoctors.getTopLocationData(year, n),
                            title='Leading Countries in no. of Dentists per 10,000 population', xlabel='Country Name', ylabel='No. of Dentists'))

    st.plotly_chart(plotBar(analyseDoctors.getBottomLocationData(year, n),
                            title='Countries having minimum no. of Dentists per 10,000 population', xlabel='Country Name', ylabel='No. of Dentists'))

    st.plotly_chart(plotChloropeth(analyseDoctors.getMapData(
        year), title="Dentists No. per 10,000 of Population in world"))


def pharmacistAnalysis():
    st.header('Pharmacists Analysis')

    n = st.select_slider("Select No.", [10, 20, 40, 60, 100, 194])

    st.plotly_chart(plotBar(analyseDoctors.getTopTooltop(n),
                            title='Leading Countries in no. of Pharmacists per 10,000 population (Average)', xlabel='Country Name', ylabel='No. of Pharmacists'))

    st.plotly_chart(plotBar(analyseDoctors.getBottomTooltop(n),
                            title='Countries having minimum no. of Pharmacists per 10,000 population (Average)', xlabel='Country Name', ylabel='No. of Pharmacists'))

    loc = st.selectbox("Select Location", analyseDoctors.getLocations())
    st.plotly_chart(plotLine(analyseDoctors.getTopYearData(loc, n),
                             title='Change in No. of Pharmacists over years', xlabel='Year', ylabel='No. of Pharmacists'))

    year = st.selectbox("Select Year", analyseDoctors.getYears())
    st.plotly_chart(plotBar(analyseDoctors.getTopLocationData(year, n),
                            title='Leading Countries in no. of Pharmacists per 10,000 population', xlabel='Country Name', ylabel='No. of Pharmacists'))

    st.plotly_chart(plotBar(analyseDoctors.getBottomLocationData(year, n),
                            title='Countries having minimum no. of Pharmacists per 10,000 population', xlabel='Country Name', ylabel='No. of Pharmacists'))

    st.plotly_chart(plotChloropeth(analyseDoctors.getMapData(
        year), title="Pharmacist No. per 10,000 of Population in world"))


sidebar.header('Choose Your Option')
options = ['View Dataset', 'Analyse Doctors',
           'Analyse Nurses', 'Analyse Dentists', 'Analyse Pharmacists']
choice = sidebar.selectbox(options=options, label="Choose Action")

with st.spinner("Please Wait for Some Time..."):

    if choice == options[0]:
        viewDataset()
    elif choice == options[1]:
        doctorAnalysis()
    elif choice == options[2]:
        nurseAnalysis()
    elif choice == options[3]:
        dentistAnalysis()
    elif choice == options[4]:
        pharmacistAnalysis()
