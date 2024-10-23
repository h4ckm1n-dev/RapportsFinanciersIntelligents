# RapportsFinanciersIntelligents

Ce projet démontre comment utiliser les modèles de langage locaux, en particulier **Llama 3.1** via **LangChain** et **Ollama**, pour générer automatiquement des rapports financiers détaillés basés sur des données d'entreprise. Cela permet de générer rapidement des analyses financières et des recommandations, le tout en restant en local, sans avoir besoin de recourir à des services cloud.

## Fonctionnalités

- Génération automatique de rapports financiers à partir de données fournies (chiffre d'affaires, dépenses, bénéfices, taux de croissance).
- Recommandations stratégiques basées sur la performance de l'entreprise et les tendances du marché.
- Identification des risques potentiels pour permettre à l'entreprise d'anticiper et de réagir face aux défis économiques.

## Exemple de rapport généré

```
Réponse du modèle :
 **Analyse du scénario**

Avant de prendre une décision, il faut considérer attentivement les données fournies.

*   **Coût de production : $500 000**
    Ce montant représentent le coût fixe pour la production initiale du produit. Il est important de noter que ce chiffre ne prend en compte que le coût de production et non le coût total lié au lancement d'un nouveau produit.
*   **Ventes estimées : $1 200 000**
    La vente projetée représente la source potentielle de revenus, qui pourrait aider à couvrir les coûts et générer des bénéfices. Il est crucial d'évaluer si ces prévisions sont fiables.
*   **Concurrence sur le marché : modérée**
    Une concurrence modérée suggère qu'il existe une opportunité pour que le produit se distingue dans un marché relativement moins saturé.

Dans ce cas, il semble que le lancement du produit soit à la fois rentable et opportun. La vente projetée est supérieure au coût de production initial, ce qui peut contribuer à couvrir les dépenses associées au lancement. De plus, une concurrence modérée suggère qu'il y a une opportunité pour que le produit se distingue dans un marché relativement moins saturé.

Cependant, avant d'engager pleinement tout investissement ou de prendre la décision finale, il pourrait être judicieux d'effectuer une analyse plus approfondie des prévisions de ventes et des coûts associés à lancement. Par exemple :

*   Analyser les données sur le marché pour valider les prévisions de ventes.
*   Évaluer soigneusement le besoin d'investissement supplémentaire avant de prendre une décision finale.

En résumé, en tenant compte des facteurs mentionnés, il semble que lancer ce produit immédiatement soit la meilleure approche. La vente projetée est supérieure au coût de production initial, et une concurrence modérée offre une opportunité pour que le produit se distingue dans un marché relativement moins saturé.
```

## Comment utiliser

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/votre-utilisateur/RapportIAAutomatisé.git
   cd RapportIAAutomatisé
   ```

2. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'exemple :**

   Assurez-vous que le modèle Llama 3.1 est téléchargé localement avec Ollama.

   ```bash
   ollama pull llama3.1
   ```

   Ensuite, exécutez le script pour générer un rapport financier.

   ```bash
   python generate_report.py
   ```

## Technologies utilisées

- **LangChain** : Pour gérer les chaînes de prompts et faciliter l'interaction avec les modèles de langage.
- **Ollama** : Pour exécuter localement le modèle Llama 3.1.
- **Python** : Langage principal utilisé pour développer l'application.

## Licence

Ce projet est sous licence MIT.