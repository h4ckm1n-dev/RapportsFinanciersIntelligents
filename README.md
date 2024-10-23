# RapportsFinanciersIntelligents

Ce projet démontre comment utiliser les modèles de langage locaux, en particulier **Llama 3.1** via **LangChain** et **Ollama**, pour générer automatiquement des rapports financiers détaillés basés sur des données d'entreprise en demandant au model des raisonement simple. Cela permet de générer rapidement des analyses financières et des recommandations, le tout en restant en local, sans avoir besoin de recourir à des services cloud.

## Fonctionnalités

- Génération automatique de rapports financiers à partir de données fournies (chiffre d'affaires, dépenses, bénéfices, taux de croissance).
- Recommandations stratégiques basées sur la performance de l'entreprise et les tendances du marché.
- Identification des risques potentiels pour permettre à l'entreprise d'anticiper et de réagir face aux défis économiques.

## Exemple de rapport généré

```
Réponse du modèle :
 **Rapport Financier de Tech Innovations Inc.**

**Introduction**

Le présent rapport a pour objectif d'analyser les données disponibles relatives à la mise en marché d'un nouveau produit par Tech Innovations Inc. Le lancement prévu est estimé dans 6 mois, et nous devons prendre en compte divers facteurs tels que le coût de production, les ventes estimées, la concurrence, la tendance du marché, la tolérance au risque, ainsi que le besoin d'investissement supplémentaire. L'objectif est de déterminer s'il est recommandé de lancer le produit maintenant ou d'attendre.

**Analyse des Risques**

Pour évaluer les risques liés à un lancement immédiat, nous devons calculer le coût total en considérant à la fois le coût de production et le besoin d'investissement supplémentaire. Le coût de production est estimé à 500000 $, tandis que le besoin d'investissement supplémentaire s'élève à 200000 $. Cela nous donne un coût total de 700000 $. 

La tolérance au risque est définie à 10%, ce qui correspond à 1200000 * 10% = 120000 $.

**Analyse des Bénéfices Attendus**

Les ventes estimées sont de 1 200 000 $, et le marché est en croissance. Malgré la concurrence modérée, il est probable que le produit puisse réussir sur le marché donné les tendances actuelles.

En comparant le coût total à la tolérance au risque, nous pouvons observer qu'avec un coût de production et d'investissement supplémentaire s'élevant à 700000 $, ce qui dépasse nettement notre seuil de tolérance au risque. 

**Recommandation**

Étant donné que le coût total dépasse la tolérance au risque, nous recommandons **d'attendre avant de lancer le produit**.

Le rapport financier fournit une analyse détaillée du contexte du projet et des facteurs clés qui influencent la décision d'un lancement immédiat ou reporté. Le coût total (coût de production + investissement supplémentaire) dépasse nettement le seuil de tolérance au risque, ce qui nous conduit à recommander un retardement du lancement pour éviter les pertes potentielles et donner plus d'autonomie à l'entreprise.

**Conclusion**

En résumé, notre analyse montre que le coût total associé à la mise en marché du nouveau produit dépasse significativement le seuil de tolérance au risque défini. Par conséquent, nous recommandons **d'attendre avant de lancer le produit** pour éviter les pertes potentielles et donner plus d'autonomie à l'entreprise. Ce rapport fournit une vue complète des implications stratégiques du lancement immédiat ou reporté, mettant en évidence l’importance de tenir compte de divers facteurs tels que le coût total, la tolérance au risque et les projections de ventes lors de la prise de décision concernant un tel projet.


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