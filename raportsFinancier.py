from langchain_community.llms import Ollama

# Données plus détaillées sur le produit et le marché
product_data = {
    "production_cost": 500000,  # Coût de production
    "estimated_sales": 1200000,  # Ventes estimées
    "market_competition": "modérée",  # Niveau de concurrence
    "market_trend": "croissante",  # Tendance du marché
    "risk_tolerance": 0.10,  # Tolérance au risque de l'entreprise en pourcentage (10%)
    "launch_timing": "6 mois",  # Délai potentiel avant lancement
    "investment_need": 200000,  # Besoin d'investissement supplémentaire
}

# Définir le seuil pour le lancement
risk_threshold = product_data["estimated_sales"] * product_data["risk_tolerance"]

# Création d'un prompt avec des seuils
prompt = f"""
Tech Innovations Inc. envisage de lancer un nouveau produit sur le marché. Voici les données disponibles :
- Coût de production : ${product_data['production_cost']}
- Ventes estimées : ${product_data['estimated_sales']}
- Concurrence sur le marché : {product_data['market_competition']}
- Tendance du marché : {product_data['market_trend']}
- Tolérance au risque : {product_data['risk_tolerance']*100}%
- Délai avant lancement estimé : {product_data['launch_timing']}
- Besoin d'investissement supplémentaire : ${product_data['investment_need']}

Analysez ces données en tenant compte du fait que si le coût total (coût de production + investissement supplémentaire) dépasse le seuil de tolérance au risque défini à {risk_threshold} $ (10 % des ventes estimées), il est recommandé de retarder le lancement.

Rédigez un rapport financier extrêmement détaillé pour Tech Innovations Inc. Le rapport doit inclure les sections suivantes :

1. **Introduction** : Présentez le contexte du projet et l'objectif du rapport.
2. **Analyse des risques** : Analysez les risques liés à un lancement immédiat, en comparant le coût total au seuil de tolérance au risque. Prenez en compte le coût de production, le besoin d'investissement supplémentaire, et la tolérance au risque de l'entreprise.
3. **Analyse des bénéfices attendus** : Évaluez les bénéfices potentiels en fonction des ventes estimées, des tendances du marché, et de la concurrence.
4. **Recommandation** : Proposez une recommandation claire et argumentée (lancer maintenant ou attendre). Expliquez pourquoi en justifiant chaque point avec des données et en prenant en compte le dépassement ou non du seuil de tolérance au risque.
5. **Conclusion** : Résumez le rapport en fournissant un aperçu des implications stratégiques pour l'entreprise.

Fournissez une analyse détaillée dans chaque section, avec des explications étape par étape et un raisonnement structuré.
"""

# Initialiser le modèle Ollama avec Llama 3
llm = Ollama(model="llama3.1")

# Générer la réponse basée sur le prompt
response = llm.generate([prompt])

# Afficher la réponse générée
print("Réponse du modèle :\n", response.generations[0][0].text)
