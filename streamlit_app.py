import time
import streamlit as st

st.set_page_config(page_title="Apnée Trainer", page_icon="🌊", layout="centered")

st.title("🌊 Entraînement d'Apnée")
st.markdown("Améliore ton contrôle respiratoire avec cette application interactive.")

# --- Paramètres utilisateur ---
col1, col2, col3 = st.columns(3)
with col1:
    duree_apnee = st.slider("Durée d'apnée (sec)", 0, 60, 20)
with col2:
    nb_repetitions = st.slider("Nombre de répétitions", 1, 10, 3)
with col3:
    repos = st.slider("Repos entre apnées (sec)", 0, 120, 30)

# --- Bouton pour démarrer ---
if st.button("🚀 Démarrer l'exercice"):
    st.write("Prépare-toi... Respire profondément 🌬️")
    time.sleep(3)

    for i in range(nb_repetitions):
        st.markdown(f"## 🔵 Apnée {i+1}/{nb_repetitions}")
        countdown_placeholder = st.empty()
        progress_bar = st.progress(0)

        # Phase d'apnée
        for sec in range(duree_apnee, -1, -1):
            countdown_placeholder.markdown(f"### ⏳ {sec} secondes restantes")
            progress_bar.progress(int(((duree_apnee - sec) / duree_apnee) * 100) if duree_apnee > 0 else 100)
            time.sleep(1)

        countdown_placeholder.markdown("## 🟢 Respire ! 🌬️")
        st.audio("https://actions.google.com/sounds/v1/alarms/beep_short.ogg")

        # Phase de repos
        if i < nb_repetitions - 1:
            st.markdown(f"### 💤 Repos ({repos} sec)")
            progress_bar = st.progress(0)
            for r in range(repos, -1, -1):
                countdown_placeholder.markdown(f"### 🕒 {r} secondes avant la prochaine apnée")
                progress_bar.progress(int(((repos - r) / repos) * 100) if repos > 0 else 100)
                time.sleep(1)

    st.success("🏁 Exercice terminé ! Bravo 👏")
    st.balloons()