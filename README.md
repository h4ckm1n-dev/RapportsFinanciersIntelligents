# RapportsFinanciersIntelligents

Ce projet démontre comment utiliser les modèles de langage locaux, en particulier **Llama 3.1** via **LangChain** et **Ollama**, pour générer automatiquement des rapports financiers détaillés basés sur des données d'entreprise. Cela permet de générer rapidement des analyses financières et des recommandations, le tout en restant en local, sans avoir besoin de recourir à des services cloud.

## Fonctionnalités

- Génération automatique de rapports financiers à partir de données fournies (chiffre d'affaires, dépenses, bénéfices, taux de croissance).
- Recommandations stratégiques basées sur la performance de l'entreprise et les tendances du marché.
- Identification des risques potentiels pour permettre à l'entreprise d'anticiper et de réagir face aux défis économiques.

## Exemple de rapport généré

```
Réponse du modèle :
 Analyse des données :

- Coût de production : $500000
- Ventes estimées : $1200000
- Concurrence sur le marché : modérée
- Tendance du marché : croissante
- Tolérance au risque : faible (supposons qu'elle soit autour de 10% par exemple)
- Délai avant lancement estimé : 6 mois
- Besoin d'investissement supplémentaire : $200000

Analyse des risques liés à un lancement immédiat :

- Les coûts de production ($500 000) représentent environ 41,7% des ventes estimées (40/97 = 41,2%). Cela est inférieur au seuil critique de 50%. 
- L'investissement supplémentaire de $200 000 dépasse le niveau de tolérance au risque de faible.

Comparaison des bénéfices attendus et recommandations :

- Étant donné que l'investissement supplémentaire dépasse le niveau de tolérance au risque, il est préférable de retarder le lancement jusqu'à ce que les ressources nécessaires soient réduites ou que d'autres solutions plus rentables soient identifiées.
- Une fois cela réalisé, la recommandation finale dépendra de la concurrence et de la tendance du marché. Si la demande est forte et qu'il existe une certaine tolérance à l'innovation au sein de votre clientèle, le lancement devrait être réalisé dans les 6 mois estimés pour profiter d'un avantage concurrentiel temporaire.
- Néanmoins, un éventuel retard serait probablement justifié par la nécessité d'allouer davantage de ressources à l'amélioration et au renforcement de la valeur ajoutée du produit, en s'appuyant sur les connaissances accumulées.

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