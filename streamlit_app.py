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
streamlit.dataframe(my_fruit_list)


