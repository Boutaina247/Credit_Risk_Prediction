# Credit_Risk_Prediction
Streamlit App Link : https://creditriskprediction-boutaina.streamlit.app/
# Prédiction du Risque de Crédit

Cette application permet de prédire le risque de crédit d'un client en fonction de diverses informations financières. L'objectif est d'aider les institutions financières à évaluer le profil de risque des clients pour déterminer si un prêt peut être accordé.

## Fonctionnalités
L'application prend en compte plusieurs critères financiers pour prédire si un client est risqué ou non. Les critères incluent :
- L'âge du client
- Le revenu annuel
- Le statut du logement
- L'ancienneté de l'emploi
- L'objet du prêt
- La note de crédit
- Le montant emprunté
- Le taux d'intérêt du prêt
- Le pourcentage du revenu alloué au prêt
- L'historique de défauts de paiement
- La longueur de l'historique de crédit

Le modèle génère une prédiction indiquant si le client est **risqué** ou **non risqué** en fonction de ces critères.

## Cas Risqué

Un client sera considéré comme **risqué** si l'une des conditions suivantes est remplie :
1. **Historique de défauts de paiement** : Si le client a des défauts de paiement (indiqué par "Y").
2. **Taux d'intérêt élevé** : Un taux d'intérêt élevé associé à un faible revenu peut rendre le client risqué.
3. **Proportion élevée du revenu allouée au prêt** : Si une trop grande partie du revenu est allouée au remboursement du prêt, le client pourrait avoir du mal à honorer ses paiements.
4. **Note de crédit faible** : Une note de crédit faible (par exemple "E", "F", ou "G") indique une gestion financière plus risquée.
5. **Montant élevé du prêt par rapport aux revenus** : Si le montant emprunté est élevé par rapport au revenu du client, cela pourrait entraîner des difficultés de remboursement.

**Exemple de cas risqué :**
- **Âge** : 30
- **Revenu annuel** : 30 000 €
- **Statut du logement** : RENT
- **Ancienneté de l'emploi** : 2 ans
- **Objet du prêt** : PERSONAL
- **Note de crédit** : D
- **Montant emprunté** : 20 000 €
- **Taux d'intérêt** : 12 %
- **Pourcentage du revenu alloué au prêt** : 0.5
- **Historique de défauts de paiement** : Y
- **Longueur de l'historique de crédit** : 5 ans

Dans ce cas, avec un faible revenu, un historique de défauts de paiement et un montant élevé emprunté, le client sera probablement jugé risqué.

## Cas Non Risqué

Un client sera considéré comme **non risqué** si ses informations indiquent une faible probabilité de défaut de paiement, notamment :
1. **Historique de paiement solide** : Pas de défauts de paiement dans l'historique.
2. **Revenu élevé** : Un revenu suffisant pour couvrir les paiements du prêt.
3. **Note de crédit élevée** : Une bonne note de crédit (par exemple "A" ou "B").
4. **Montant raisonnable du prêt par rapport aux revenus** : Un montant emprunté faible comparé au revenu du client.
5. **Proportion faible du revenu allouée au prêt** : Le client alloue une faible part de son revenu au remboursement du prêt.

**Exemple de cas non risqué :**
- **Âge** : 30
- **Revenu annuel** : 50 000 €
- **Statut du logement** : RENT
- **Ancienneté de l'emploi** : 5 ans
- **Objet du prêt** : PERSONAL
- **Note de crédit** : A
- **Montant emprunté** : 5 000 €
- **Taux d'intérêt** : 10 %
- **Pourcentage du revenu alloué au prêt** : 0.2
- **Historique de défauts de paiement** : N
- **Longueur de l'historique de crédit** : 5 ans

Dans ce cas, avec un revenu stable, une bonne note de crédit, un faible montant emprunté, et pas d'historique de défaut, le client est jugé **non risqué**.

## Installation

1. Clonez le repository :
   ```bash
   git clone https://github.com/yourusername/credit-risk-prediction.git
