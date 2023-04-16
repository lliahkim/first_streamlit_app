
#testing
import streamlit

streamlit.title("My parent new healthy diner")
streamlit.header("Breakfast Menu")
streamlit.text("🐔 Omelette - $5")
streamlit.text("🥑🍞 Avocado Toast - $6")
streamlit.text("🥣 Oatmeal and raisin - $5")
streamlit.text("Make your own smoothie")

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruit for your smoothie", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
