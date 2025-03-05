import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

# Charger le modèle pré-entrainé
model = joblib.load('model.joblib')

# Charger le dataset
credit_risk_dataset = pd.read_csv('credit_risk_dataset.csv', sep=";")

# Fonction pour afficher l'interface utilisateur
def user_input_features():
    age = st.slider('Âge', 18, 100, 30)
    income = st.number_input('Revenu annuel', 0, 1000000, 50000)
    home_ownership = st.selectbox('Statut du logement', ['RENT', 'OWN', 'MORTGAGE'])
    emp_length = st.slider('Ancienneté de l\'emploi (en années)', 0, 50, 5)
    loan_intent = st.selectbox('Objet du prêt', ['PERSONAL', 'EDUCATION', 'MEDICAL'])
    loan_grade = st.selectbox('Note de crédit', ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    loan_amnt = st.number_input('Montant emprunté', 100, 1000000, 5000)
    loan_int_rate = st.number_input('Taux d\'intérêt du prêt', 0.0, 50.0, 10.0)
    loan_percent_income = st.number_input('Pourcentage du revenu alloué au prêt', 0.0, 1.0, 0.2)
    default_on_file = st.selectbox('Historique de défauts de paiement', ['Y', 'N'])
    cred_hist_length = st.slider('Longueur de l\'historique de crédit (en années)', 1, 20, 5)

    data = {
        'person_age': age,
        'person_income': income,
        'person_home_ownership': home_ownership,
        'person_emp_length': emp_length,
        'loan_intent': loan_intent,
        'loan_grade': loan_grade,
        'loan_amnt': loan_amnt,
        'loan_int_rate': loan_int_rate,
        'loan_percent_income': loan_percent_income,
        'cb_person_default_on_file': default_on_file,
        'cb_person_cred_hist_length': cred_hist_length
    }
    
    features = pd.DataFrame(data, index=[0])
    return features


# Entrée des données de l'utilisateur
st.title("Prédiction du Risque de Crédit")
st.markdown("<h3 style='text-align: center;'>by Boutaina BELGHITI</h3>", unsafe_allow_html=True)
# Ajouter une image de couverture
image = Image.open('images/risk.jpeg')
st.image(image, caption='Bienvenue dans l\'analyse du risque de crédit', use_container_width=True)

st.write("Veuillez entrer les informations ci-dessous pour prédire le risque d'un prêt.")

input_data = user_input_features()


# Ajouter le bouton 'Prédire'
if st.button('Prédire'):
    # Prédiction avec le modèle
    prediction = model.predict(input_data)

    # Résultat de la prédiction
    st.subheader("Résultat de la prédiction")
    if prediction == 1:
        st.markdown("<h3 style='color: red;'>Ce client est risqué.</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: green;'>Ce client n'est pas risqué.</h3>", unsafe_allow_html=True)


# Ajouter un aperçu des premières lignes du dataset
st.subheader('Aperçu des données')
st.dataframe(credit_risk_dataset.head())

# Visualisation - Histogramme du Montant du Prêt
st.subheader('Histogramme du Montant du Prêt')
fig, ax = plt.subplots(figsize=(10, 6))  # Crée explicitement un objet figure
sns.histplot(credit_risk_dataset['loan_amnt'], kde=True, ax=ax)  # Passe ax à sns.histplot
st.pyplot(fig)  # Passe la figure à st.pyplot


# Ajouter une image supplémentaire
st.image('images/data.jpeg', caption='Analyse des données', width=700)
