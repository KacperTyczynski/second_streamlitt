import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def get_sweatsuit_data(this_cloth_choice):
  cloth_response = requests.get("https://uni-klaus.s3.us-west-2.amazonaws.com/clothing" +this_cloth_choice)
  cloth_normalized = pandas.json_normalize(cloth_response.json())
  return cloth_normalized

streamlit.header('ZENA S AMAZING ATHLEISURE CATALOG')
try:
  cloth_choice = streamlit.text_input('Pick a sweatsuit color or style:')
  if not cloth_choice:
    streamlit.error("Please select a sweatsuit")
  else:  
    back_from_function = get_sweatsuit_data(cloth_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()

  
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# Creating a catalog with data from snowflake
my_catalog = my_cure.fetchall()

df = pandas.DataFrame(my_catalog)
streamlit.write(df)

## CONNECTION TEST
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)
