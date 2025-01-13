# Fitness Program Generator

## Objectifs de l'application
Cette application a pour objectif de proposer des programmes de fitness personnalisés basés sur le profil et les objectifs de l'utilisateur. En répondant à quelques questions simples, l'utilisateur recevra une recommandation adaptée pour atteindre ses objectifs (ex. perte de poids, gain de masse musculaire, amélioration de l'endurance, etc.).

## Spécifications produit

### User Story 1 : Collecte des informations utilisateur
**En tant qu'utilisateur**, je veux fournir mes informations de base (âge, poids, niveau d'activité actuel, objectif de fitness), afin que l'application puisse générer un programme personnalisé.

#### Critères d'acceptation :
1. Les informations doivent être validées (par exemple, les âges et poids doivent être des nombres raisonnables).
2. Un message d'erreur clair doit s'afficher si des données sont manquantes ou incorrectes.
3. Les données fournies par l'utilisateur doivent être utilisées dans la génération du programme.

---



## Architecture générale de l'application
- **Langage principal** : Python
- **Dépendances** :
  - Pandas (pour manipuler les données utilisateurs)
  - NumPy (pour calculs et ajustements du programme)

## Instructions d'installation

1. **Cloner le projet**
   ```bash
   git clone https://github.com/MohAIzawi/Fitness_ProgrammU
   cd Fitness_Programmu
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**
   - Windows :
     ```bash
     venv\Scripts\activate
     ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## Instructions d'exécution

1. **Exécuter le script principal**
   ```bash
   python main.py
   ```

2. **Tester l'application**
   ```bash
   python -m pytest -v
