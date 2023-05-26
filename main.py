import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

 
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# Creating a catalog with data from snowflake
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

df = pandas.DataFrame(my_catalog)
# streamlit.write(df)

color_list = df[0].values.tolist()
# print(color_list)

# Adding a color/style selection box
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

# Adding a description
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

## CONNECTION TEST
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';")
df2 = my_cur.fetchone()
streamlit.image(
df2[0],
width=400,
caption = product_caption
)
streamlit.write('Price: ', df2[1])
streamlit.write('Sizes Available: ',df2[2])
streamlit.write(df2[3])
