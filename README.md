# RapportsFinanciersIntelligents

Ce projet démontre comment utiliser les modèles de langage locaux, en particulier **Llama 3.1** via **LangChain** et **Ollama**, pour générer automatiquement des rapports financiers détaillés basés sur des données d'entreprise. Cela permet de générer rapidement des analyses financières et des recommandations, le tout en restant en local, sans avoir besoin de recourir à des services cloud.

## Fonctionnalités

- Génération automatique de rapports financiers à partir de données fournies (chiffre d'affaires, dépenses, bénéfices, taux de croissance).
- Recommandations stratégiques basées sur la performance de l'entreprise et les tendances du marché.
- Identification des risques potentiels pour permettre à l'entreprise d'anticiper et de réagir face aux défis économiques.

## Exemple de rapport généré

```
Réponse du modèle :
 Analyse des données disponibles :

- Coût de production : $500 000
- Ventes estimées : $1 200 000
- Concurrence sur le marché : modérée
- Tendance du marché : croissante
- Tolérance au risque : 10%
- Délai avant lancement estimé : 6 mois
- Besoin d'investissement supplémentaire : $200 000

Calcul des bénéfices attendus :
Bénéfices attendus = Ventes estimées - Coût de production
Bénéfices attendus = 1 200 000 - 500 000 = $700 000

Comparaison avec la tolérance au risque :
La tolérance au risque est de 10%. Le coût de production représente environ 41,7% des ventes estimées (soit 500 000/1 200 000). Cela laisse donc suffisamment d'espace pour les marges bénéficiaires et ne dépasse pas la tolérance au risque.

Calcul du besoin d'investissement supplémentaire en relation avec la tolérance au risque :
Le besoin d'investissement supplémentaire est de 200 000 $, soit environ 16,7% des ventes estimées (soit 200 000/1 200 000). Cela dépasse également légèrement le niveau de tolérance au risque.

Recommandation :
- Le coût de production ne dépasse pas les 50 % des ventes estimées.
- L'investissement supplémentaire est supérieur à la tolérance au risque (16,7 % contre 10 %).

En tenant compte du besoin d'investissement supplémentaire dépassant le niveau de tolérance au risque, il est recommandé de retarder le lancement afin d'évaluer et de réduire les besoins en investissements, avant de poursuivre avec le lancement.

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