import streamlit as st
import requests as rq
import json
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

pickup_datetime = st.datetime_input('Pickup Datetime')
pickup_longitude = st.number_input('Pickup longitude',value=-73)
pickup_latitude = st.number_input('Pickup latitude',value=40)
dropoff_longitude = st.number_input('Dropoff longitude',value=-75)
dropoff_latitude = st.number_input('Dropoff latitude',value=40)
passenger_count = st.number_input('Passenger count',step=1,min_value=1)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''
if st.button('Make a prediction'):
    url = f'https://taxifare.lewagon.ai/predict?pickup_datetime={pickup_datetime.strftime('%Y-%m-%d+%H:%M:%S')}&pickup_longitude={pickup_longitude}&pickup_latitude={pickup_latitude}&dropoff_longitude={dropoff_longitude}&dropoff_latitude={dropoff_latitude}&passenger_count={passenger_count}'

    response = rq.get(url)
    response.raise_for_status()
    response = json.loads(response.content.decode("utf-8"))

    st.metric("Prediction result",response['fare'])
    df = pd.DataFrame(
        [[pickup_longitude,pickup_latitude],[dropoff_longitude,dropoff_latitude]],
        columns=["lon", "lat"]
    )
    st.map(df,latitude='lat',longitude='lon')
