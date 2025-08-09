import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Viz Demo")


# with open(r'C:\Users\hp\PycharmProjects\startup-dashboard\mlproject\pages\df.pkl', 'rb') as file:
data_dir=Path(__file__).parent
with open(data_dir / 'df.pkl', 'rb') as file:
    df = pickle.load(file)

# with open(r'C:\Users\hp\PycharmProjects\startup-dashboard\mlproject\pages\pipeline.pkl', 'rb') as file:
with open(data_dir / 'pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)


st.header('Enter your inputs')

# Add a default placeholder for each selectbox

property_type = st.selectbox('Property Type', ['Select Property Type', 'flat', 'house'])

sector = st.selectbox('Sector', ['Select Sector'] + sorted(df['sector'].unique().tolist()))

bedroom_opt = ['Select Bedrooms'] + sorted(df['bedRoom'].unique().tolist())
bedroom = st.selectbox('Number of Bedroom', bedroom_opt)

bathroom_opt = ['Select Bathrooms'] + sorted(df['bathroom'].unique().tolist())
bathroom = st.selectbox('Number of Bathrooms', bathroom_opt)

balcony_opt = ['Select Balconies'] + sorted(df['balcony'].unique().tolist())
balcony = st.selectbox('Balconies', balcony_opt)

property_age = st.selectbox('Property Age', ['Select Property Age'] + sorted(df['agePossession'].unique().tolist()))

built_up_area = st.number_input('Built Up Area')  # keep as is

servant_room = st.selectbox('Servant Room', ['Select Option', 0.0, 1.0])
store_room = st.selectbox('Store Room', ['Select Option', 0.0, 1.0])

furnishing_type = st.selectbox('Furnishing Type', ['Select Furnishing Type'] + sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category', ['Select Luxury Category'] + sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category', ['Select Floor Category'] + sorted(df['floor_category'].unique().tolist()))


if st.button('Predict'):

    # form a dataframe
    data = [[property_type, sector, bedroom, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    #st.dataframe(one_df)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # display
    st.text("The price of the flat is between {} Cr and {} Cr".format(round(low,2),round(high,2)))


