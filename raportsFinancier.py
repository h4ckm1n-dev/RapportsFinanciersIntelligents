from langchain_community.llms import Ollama

# Données plus détaillées sur le produit et le marché
product_data = {
    "production_cost": 500000,  # Coût de production
    "estimated_sales": 1200000,  # Ventes estimées
    "market_competition": "modérée",  # Niveau de concurrence
    "market_trend": "croissante",  # Tendance du marché
    "risk_tolerance": "faible",  # Tolérance au risque de l'entreprise
    "launch_timing": "6 mois",  # Délai potentiel avant lancement
    "investment_need": 200000,  # Besoin d'investissement supplémentaire
}

# Création d'un prompt plus détaillé pour une analyse plus profonde
prompt = f"""
Tech Innovations Inc. envisage de lancer un nouveau produit sur le marché. Voici les données disponibles :
- Coût de production : ${product_data['production_cost']}
- Ventes estimées : ${product_data['estimated_sales']}
- Concurrence sur le marché : {product_data['market_competition']}
- Tendance du marché : {product_data['market_trend']}
- Tolérance au risque : {product_data['risk_tolerance']}
- Délai avant lancement estimé : {product_data['launch_timing']}
- Besoin d'investissement supplémentaire : ${product_data['investment_need']}

En tenant compte de ces facteurs, recommandez-vous de lancer ce produit immédiatement ou de retarder son lancement ? Veuillez expliquer votre raisonnement en fonction des risques, des bénéfices attendus, de la concurrence, et des besoins d'investissement.
"""

# Initialiser le modèle Ollama avec Llama 3
llm = Ollama(model="llama3.1")

# Générer la réponse basée sur le prompt
response = llm.generate([prompt])

# Afficher la réponse générée
print("Réponse du modèle :\n", response.generations[0][0].text)
