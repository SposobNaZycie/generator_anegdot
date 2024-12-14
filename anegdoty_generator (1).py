import streamlit as st
import openai

# Konfiguracja klucza API OpenAI
openai.api_key = "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"  # Wstaw tutaj swój klucz API

def generuj_anegdote(tematyka):
    """Generowanie anegdoty przy użyciu OpenAI API."""
    prompt = (
        f"Wygeneruj anegdotę na temat '{tematyka}'. Anegdota powinna mieć maksymalnie 3-4 zdania, być zabawna, inspirująca lub mieć niespodziewaną puentę."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Aktualizacja modelu
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,  # Zwiększenie, by uniknąć ucięcia
            temperature=0.7
        )
        # Ucinamy wynik do 3-4 zdań
        anegdota = response.choices[0].message.content.strip()
        zdania = anegdota.split(". ")
        return ". ".join(zdania[:4]).strip() + ("." if not anegdota.endswith(".") else "")
    except Exception as e:
        return f"Wystąpił błąd podczas generowania anegdoty: {e}"

def main():
    st.title("Generator Anegdot na Podstawie Tematyki")
    st.write("Wybierz tematykę, a sztuczna inteligencja wygeneruje anegdotę specjalnie dla Ciebie!")

    # Lista tematyk
    tematyki = ["Zabawne", "Inspirujące", "Zaskakujące z puentą", "Motywujące"]
    tematyka = st.selectbox("Wybierz tematykę anegdoty:", tematyki)

    # Przycisk generowania
    if st.button("Generuj Anegdotę"):
        st.write("Generowanie anegdoty...")
        anegdota = generuj_anegdote(tematyka)
        st.success("Oto Twoja anegdota:")
        st.write(anegdota)

        # Tworzenie pliku tekstowego do pobrania
        if anegdota:
            plik = f"anegdota_{tematyka.lower()}.txt"
            st.download_button(
                label="Pobierz anegdotę jako plik",
                data=anegdota,
                file_name=plik,
                mime="text/plain"
            )

if __name__ == "__main__":
    main()
