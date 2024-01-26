# https://python.gotrained.com/scrapy-tutorial-web-scraping-craigslist/

import streamlit as st
import requests, json
import  os, sys

# streamlit run streamlit_client.py

# Obtenir le dossier parent du dossier actuel
dossier_parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
dossier_parent = os.path.abspath(os.path.join(dossier_parent, os.pardir))
# Ajouter le dossier parent au chemin d'accès
sys.path.append(dossier_parent)
from email_test import send_email_log

serveur_url = "http://localhost:5000"

def get_server_data():
    response = requests.get(f"{serveur_url}/search", params={"query": query})  
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: ", response.status_code)

def random_quote():
    response = requests.get(f"{serveur_url}/random", params={"number": quote_number})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error: ", response.status_code)

st.header("Citations")
st.write("Barre de recherche")
query = st.text_input("Veuillez entrer votre recherche")
if st.button("Recherche"):
    server_data = get_server_data()
    if server_data:
        for result in server_data:
            st.write(result["quote"], "- ", result["author"])
        send_email_log()
    else:
        st.write("Aucune citation")

st.write("Citation aleatoire")
quote_number = st.slider("Veuillez choisir un nombre de citations", 1, 5, 1)
if st.button("Citation aleatoire"): 
        data = random_quote()
        if data:
            for result in data:
                st.write(result["quote"], "- ", result["author"])
        else:
            st.write("Aucune citation")
