import streamlit

streamlit.title('My Diet Plan')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Beetroot juice')
streamlit.header('Lunch')
streamlit.text('🐔Brown Rice & chicken')
streamlit.header('Dinner')
streamlit.text('🥗Roti eggs')

streamlit.header('Hey Anu How are you?')
streamlit.text('Are you ok!!')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇') 
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)



