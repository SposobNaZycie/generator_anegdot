{\rtf1\ansi\ansicpg1250\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import random\
import json\
\
# Wczytywanie bazy anegdot z pliku JSON\
def wczytaj_anekdoty():\
    try:\
        with open("anekdoty.json", "r") as file:\
            return json.load(file)\
    except FileNotFoundError:\
        return \{\
            "Zabawne": [],\
            "Inspiruj\uc0\u261 ce": [],\
            "Zaskakuj\uc0\u261 ce z puent\u261 ": [],\
            "Motywuj\uc0\u261 ce": []\
        \}\
\
# Zapisywanie bazy anegdot do pliku JSON\
def zapisz_anekdoty(anekdoty):\
    with open("anekdoty.json", "w") as file:\
        json.dump(anekdoty, file, indent=4)\
\
anekdoty = wczytaj_anekdoty()\
\
# Funkcja losuj\uc0\u261 ca anegdoty\
def losuj_anegdoty(kategoria, liczba):\
    if kategoria == "Wszystkie":\
        wszystkie_anegdoty = [anegdota for lista in anekdoty.values() for anegdota in lista]\
        return random.sample(wszystkie_anegdoty, min(liczba, len(wszystkie_anegdoty)))\
    elif kategoria not in anekdoty:\
        return ["Nie znaleziono anegdot w tej kategorii."]\
    return random.sample(anekdoty[kategoria], min(liczba, len(anekdoty[kategoria])))\
\
# Interfejs u\uc0\u380 ytkownika\
st.title("Generator Anegdot")\
st.markdown("Wybierz kategori\uc0\u281  i zobacz anegdoty z \u380 ycia wzi\u281 te!")\
\
# Wyb\'f3r kategorii\
kategorie = ["Wszystkie"] + list(anekdoty.keys())\
kategoria = st.selectbox("Wybierz kategori\uc0\u281  anegdot", kategorie)\
\
# Wyb\'f3r liczby anegdot\
liczba_anegdot = st.slider("Ile anegdot chcesz zobaczy\uc0\u263 ?", min_value=1, max_value=5, value=3)\
\
# Wy\uc0\u347 wietlanie anegdot i zapisywanie do pliku\
def zapisz_do_pliku(anegdoty):\
    with open("wygenerowane_anegdoty.txt", "w") as file:\
        for idx, anegdota in enumerate(anegdoty, 1):\
            file.write(f"\{idx\}. \{anegdota\}\\n")\
    st.success("Anegdoty zapisano do pliku 'wygenerowane_anegdoty.txt'")\
\
if st.button("Generuj anegdoty"):\
    wynik = losuj_anegdoty(kategoria, liczba_anegdot)\
    for idx, anegdota in enumerate(wynik, 1):\
        st.write(f"**\{idx\}.** \{anegdota\}")\
    if st.button("Zapisz do pliku"):\
        zapisz_do_pliku(wynik)\
\
# Sekcja dodawania anegdot\
def dodaj_anegdoty():\
    st.subheader("Dodaj w\uc0\u322 asn\u261  anegdot\u281 ")\
    nowa_kategoria = st.selectbox("Wybierz kategori\uc0\u281 ", list(anekdoty.keys()))\
    nowa_anegdota = st.text_area("Wpisz swoj\uc0\u261  anegdot\u281 ")\
    if st.button("Dodaj anegdot\uc0\u281 "):\
        if nowa_anegdota and len(nowa_anegdota.strip()) > 10:\
            anekdoty[nowa_kategoria].append(nowa_anegdota)\
            zapisz_anekdoty(anekdoty)\
            st.success("Anegdota zosta\uc0\u322 a dodana!")\
        elif len(nowa_anegdota.strip()) <= 10:\
            st.error("Anegdota jest zbyt kr\'f3tka. Wprowad\uc0\u378  co najmniej 10 znak\'f3w.")\
        else:\
            st.error("Prosz\uc0\u281  wpisa\u263  tre\u347 \u263  anegdoty.")\
\
dodaj_anegdoty()\
}