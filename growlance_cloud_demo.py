
import streamlit as st

st.set_page_config(page_title="Growlance – Demo", layout="centered")
st.title("🌱 Growlance – Beta-Demo")

email = st.text_input("✉️ E-Mail (Demo)", placeholder="max@example.com")

if email:
    st.success(f"Willkommen, {email.split('@')[0].capitalize()}!")

    paket = st.selectbox("🔐 Dein Paket", ["Basic", "Pro", "Family"])
    max_konten = {"Basic": 1, "Pro": 3, "Family": 7}[paket]
    st.markdown(f"👤 Du kannst bis zu **{max_konten} Konten** verwalten.")

    ziel = st.number_input("🎯 Sparziel (€)", value=1000)
    einnahmen = st.number_input("💰 Einnahmen (€)", value=950)
    ausgaben = st.number_input("💸 Ausgaben (€)", value=500)
    differenz = einnahmen - ausgaben
    fortschritt = min(100, int(100 * differenz / ziel)) if ziel > 0 else 0

    st.progress(fortschritt, text=f"{fortschritt}% deines Ziels erreicht")

    if paket == "Basic":
        st.warning("📄 Steuerrechner nur in Pro & Family verfügbar.")
    else:
        steuer = st.number_input("📄 Jahreseinkommen (Demo)", value=12000)
        steuerlast = int(steuer * 0.14)
        st.info(f"🧾 Geschätzte Steuer: {steuerlast} €")

    if paket != "Basic":
        st.success("🤖 KI-Challenge: 5 Tage keine Online-Bestellung!")

    st.markdown("✅ CSV-Export ist in allen Versionen enthalten.")

    if "saved" not in st.session_state:
        st.session_state["saved"] = False

    if st.button("💾 Speichern (Demo)"):
        st.session_state["saved"] = True
        st.success("✅ Deine Daten wurden (Demo) gespeichert.")
