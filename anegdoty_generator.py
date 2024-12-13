import streamlit as st
import random

# Baza anegdot
anekdoty = {
    "Zabawne": [
        "Podczas sesji zdjęciowej pies modelki zdecydował, że to on będzie gwiazdą. Skoczył na plan i zaczął pozować jak profesjonalista!",
        "Klient poprosił o retusz zdjęcia. Wysłałem mu wersję z poprawkami, a on odpisał: 'Super, ale możesz usunąć jeszcze ten most w tle?'. Problem w tym, że to był Golden Gate Bridge.",
        "Próbowałem uchwycić idealny moment na weselu, kiedy nagle babcia Pary Młodej zaczęła tańczyć breakdance. Zdjęcie? Bezcenne!"
    ],
    "Inspirujące": [
        "Kiedyś fotografowałem dzieci na ulicy w Afryce. Jedno z nich zapytało mnie: 'Dlaczego świat jest taki piękny?'. Zrozumiałem, że piękno tkwi w perspektywie.",
        "Pewien młody artysta zapytał mnie, jak zdobyć klientów. Odpowiedziałem: 'Najpierw rób to, co kochasz, a potem znajdź ludzi, którzy to pokochają'.",
        "Na mojej drodze spotkałem wiele trudności, ale każda z nich była cegiełką, z której zbudowałem swoją karierę."
    ],
    "Zaskakujące z puentą": [
        "Klient zapytał mnie, czy mogę wyretuszować jego zdjęcie tak, żeby wyglądał jak Brad Pitt. Po godzinach pracy wysłałem mu efekt, a on napisał: 'To zdjęcie jest świetne, ale wygląda jak... Brad Pitt?'",
        "Podczas zdjęć plenerowych zapomniałem baterii do aparatu. Zamiast wrócić do domu, postanowiłem zrobić zdjęcia telefonem. Efekt? Klient powiedział, że to moje najlepsze zdjęcia.",
        "Raz zostałem poproszony o sfotografowanie bardzo drogiego zegarka. Okazało się, że zegarek to podróbka, a sesja była na potrzeby... aukcji internetowej."
    ],
    "Motywujące": [
        "Każdy wielki projekt zaczyna się od małego kroku. Moje pierwsze zdjęcia robiłem na starym aparacie analogowym. Dziś współpracuję z międzynarodowymi markami.",
        "Nie ważne, ile razy ci się nie uda, ważne, ile razy spróbujesz ponownie.",
        "Sukces to nie przypadek. To wynik ciężkiej pracy, nauki na błędach i wytrwałości."
    ]
}

# Funkcja losująca anegdoty
def losuj_anegdoty(kategoria, liczba):
    if kategoria == "Wszystkie":
        wszystkie_anegdoty = [anegdota for lista in anekdoty.values() for anegdota in lista]
        return random.sample(wszystkie_anegdoty, min(liczba, len(wszystkie_anegdoty)))
    elif kategoria not in anekdoty:
        return ["Nie znaleziono anegdot w tej kategorii."]
    return random.sample(anekdoty[kategoria], min(liczba, len(anekdoty[kategoria])))

# Interfejs użytkownika
st.title("Generator Anegdot")
st.markdown("Wybierz kategorię i zobacz anegdoty z życia wzięte!")

# Wybór kategorii
kategorie = ["Wszystkie"] + list(anekdoty.keys())
kategoria = st.selectbox("Wybierz kategorię anegdot", kategorie)

# Wybór liczby anegdot
liczba_anegdot = st.slider("Ile anegdot chcesz zobaczyć?", min_value=1, max_value=5, value=3)

# Wyświetlanie anegdot i zapisywanie do pliku
def zapisz_do_pliku(anegdoty):
    with open("wygenerowane_anegdoty.txt", "w") as file:
        for idx, anegdota in enumerate(anegdoty, 1):
            file.write(f"{idx}. {anegdota}\n")
    st.success("Anegdoty zapisano do pliku 'wygenerowane_anegdoty.txt'")

if st.button("Generuj anegdoty"):
    wynik = losuj_anegdoty(kategoria, liczba_anegdot)
    for idx, anegdota in enumerate(wynik, 1):
        st.write(f"**{idx}.** {anegdota}")
    if st.button("Zapisz do pliku"):
        zapisz_do_pliku(wynik)

# Sekcja dodawania anegdot
def dodaj_anegdoty():
    st.subheader("Dodaj własną anegdotę")
    nowa_kategoria = st.selectbox("Wybierz kategorię", list(anekdoty.keys()))
    nowa_anegdota = st.text_area("Wpisz swoją anegdotę")
    if st.button("Dodaj anegdotę"):
        if nowa_anegdota and len(nowa_anegdota.strip()) > 10:
            anekdoty[nowa_kategoria].append(nowa_anegdota)
            st.success("Anegdota została dodana!")
        elif len(nowa_anegdota.strip()) <= 10:
            st.error("Anegdota jest zbyt krótka. Wprowadź co najmniej 10 znaków.")
        else:
            st.error("Proszę wpisać treść anegdoty.")

dodaj_anegdoty()
