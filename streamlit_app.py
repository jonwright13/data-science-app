import streamlit as st
import utils
import pandas as pd

options_select = ("Interrogate Dataset", "Missing Values", "Feature Engineering")
analysis_btns = ("Interrogate Columns", "Classify Columns", "Show Stats", "Show Uniques")


# Setting basic configs
st.set_page_config(
    page_title="EDA App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto"
    )


upload_file = st.sidebar.file_uploader(
    "Upload File", 
    accept_multiple_files=False, 
    key='uploader'
    )


if upload_file:

    # Select option
    analysis_select = st.sidebar.selectbox(
        label="Select Analysis Type",
        options=options_select
    )

    # Setting title
    st.title(analysis_select)

    df = pd.read_csv(upload_file)

    if options_select.index(analysis_select) == 0:

        obj = utils.interrogate_single_dataset(df)

        radio = st.sidebar.radio(
            label="Options",
            options=analysis_btns
        )
        
        if analysis_btns.index(radio) == 0:
            st.dataframe(obj.table, use_container_width=True)
        elif analysis_btns.index(radio) == 1:
            st.write(obj.columns)
        elif analysis_btns.index(radio) == 2:
            st.dataframe(data=obj.stats.T, use_container_width=True)
        elif analysis_btns.index(radio) == 3:

            col1, col2 = st.columns(2)

            column_select = col1.selectbox(
                label="Select Column",
                options=obj.columns['Categorical']
            )

            col2.write(obj.show_uniques(column_select))



