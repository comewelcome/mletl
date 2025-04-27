# mletl

**mletl** (Machine Learning ETL) est une bibliothèque Python pour simplifier les tâches d'ETL (Extract, Transform, Load) dans les projets de Machine Learning.  
Elle fournit des outils modulaires pour l'extraction, la transformation et le chargement de données, avec une approche flexible et adaptée aux pipelines ML modernes.

## ✨ Fonctionnalités

- Extraction facile de données à partir de différentes sources.
- Transformation configurable et personnalisable.
- Chargement optimisé pour les workflows de Machine Learning.
- Support pour la création de pipelines réutilisables.
- Conçu pour être extensible et facile à intégrer dans vos projets existants.

## 📦 Installation

pip install mletl

ou pour installer directement depuis le dépôt :

git clone https://github.com/comewelcome/mletl.git
cd mletl
pip install .

📚 Documentation
La documentation complète est en cours de rédaction.
En attendant, vous pouvez consulter les modules disponibles dans le dossier mletl/ pour explorer l'architecture et l'utilisation des classes principales.

## Structure du projet
mletl/
├── extractor.py
├── transformer.py
├── loader.py
├── __init__.py
tests/
├── test_extractor.py
├── test_transformer.py
├── test_loader.py
