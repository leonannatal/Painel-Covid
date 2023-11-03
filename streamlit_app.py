import streamlit as st
import pandas as pd
import numpy as np
import json
import requests

st.title("Painel Covid")
url = "https://imunizacao-es.saude.gov.br/_search"

payload = json.dumps({
  "size": 10000
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k='
}

response = requests.request("POST", url, headers=headers, data=payload)
data = response.json()
data = pd.json_normalize(data['hits']['hits'])
data
st.bar_chart(data)
