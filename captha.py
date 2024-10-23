from langchain_community.llms import Ollama
from datetime import datetime

# Simulated financial data for a company
financial_data = {
    "revenue": 1200000,
    "expenses": 800000,
    "profit": 400000,
    "growth": 0.15,
    "market_trend": "positive",
}

# Additional details
company_name = "Tech Innovations Inc."
current_date = datetime.now().strftime("%Y-%m-%d")

# Ollama prompt to generate a business report in French
prompt = f"""
Rédige un rapport financier en français pour {company_name} en date du {current_date} basé sur les données financières suivantes :
- Chiffre d'affaires : ${financial_data['revenue']}
- Dépenses : ${financial_data['expenses']}
- Bénéfice : ${financial_data['profit']}
- Taux de croissance : {financial_data['growth'] * 100}%
- Tendance du marché : {financial_data['market_trend']}

Le rapport doit inclure :
1. Un aperçu de la performance financière de l'entreprise.
2. Des recommandations basées sur le taux de croissance actuel et les tendances du marché.
3. Les risques potentiels à prendre en compte.
"""


# Function to interact with the Ollama model via LangChain
def generate_report(prompt):
    # Initialize the Ollama model (e.g., using llama3.1)
    llm = Ollama(model="llama3.1")

    # Generate a response from the model (passing the prompt as a list)
    response = llm.generate([prompt])

    # Extract the actual text from the response
    generated_text = response.generations[0][0].text
    return generated_text


# Generate and print the business report
business_report = generate_report(prompt)
print("Rapport Financier Généré :\n", business_report)
