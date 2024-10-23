from langchain_community.llms import Ollama

# Données plus détaillées sur le produit et le marché
product_data = {
    "production_cost": 500000,  # Coût de production
    "estimated_sales": 1200000,  # Ventes estimées
    "market_competition": "modérée",  # Niveau de concurrence
    "market_trend": "croissante",  # Tendance du marché
    "risk_tolerance": "10%",  # Tolérance au risque de l'entreprise
    "launch_timing": "6 mois",  # Délai potentiel avant lancement
    "investment_need": 200000,  # Besoin d'investissement supplémentaire
}

# Création d'un prompt plus détaillé avec des critères spécifiques
prompt = f"""
Tech Innovations Inc. envisage de lancer un nouveau produit sur le marché. Voici les données disponibles :
- Coût de production : ${product_data['production_cost']}
- Ventes estimées : ${product_data['estimated_sales']}
- Concurrence sur le marché : {product_data['market_competition']}
- Tendance du marché : {product_data['market_trend']}
- Tolérance au risque : {product_data['risk_tolerance']}
- Délai avant lancement estimé : {product_data['launch_timing']}
- Besoin d'investissement supplémentaire : ${product_data['investment_need']}

Analysez les risques liés à un lancement immédiat et comparez-les aux bénéfices attendus. Si les coûts de production dépassent 50 % des ventes estimées ou si l'investissement supplémentaire dépasse le niveau de tolérance au risque, recommandez de retarder le lancement. Sinon, évaluez les bénéfices attendus et donnez une recommandation finale en fonction de la concurrence et de la tendance du marché.
"""

# Initialiser le modèle Ollama avec Llama 3
llm = Ollama(model="llama3.1")

# Générer la réponse basée sur le prompt
response = llm.generate([prompt])

# Afficher la réponse générée
print("Réponse du modèle :\n", response.generations[0][0].text)
