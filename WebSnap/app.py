"""
Steps we will take to make this possible:
    we will be web scraping the Unsplash website
    https://unsplash.com/s/photos/{target_word}
    search for div: ripi6->figure->img: MorZF
"""
import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

st.header('WebSnap')
st.write('WebSnap is an innovative application designed to streamline image search and collection from the vast expanse of the internet.')

with st.form('Search'):
    keyword = st.text_input('Enter your key word!')
    search = st.form_submit_button('Search')

placeHolder = st.empty()
if keyword:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, 'lxml')
    rows = soup.find_all("div", class_="ripi6")
    col1, col2 = placeHolder.columns(2)

    for index, row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            div = figures[i].find("div", class_="MorZF")
            list = (div.find("img").attrs['src'].split("?"))

            anchor = figures[i].find("a", class_="rEAWd")
            print(anchor["href"])
            if i == 0:
                col1.image(list[0])
                btn1 = col1.button("Download", key=str(index)+str(i))
                if btn1:
                    webbrowser.open_new_tab("https://unsplash.com" + anchor["href"])
            else:
                col2.image(list[0])
                btn2 = col2.button("Download", key=str(index)+str(i))
                if btn2:
                    webbrowser.open_new_tab("https://unsplash.com" + anchor["href"])





