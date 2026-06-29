
# 🧠 NEURO-AI

> **Benchmark of Variational Autoencoders for Spike Train Analysis**
> 
> *Classement de profils d'activités de neurones biologiques par apprentissage profond de type auto-encodeur (VAE)*

<p align="center">
  <a href="https://huggingface.co/spaces/KineDS/Benchmark_vae">
    <img src="https://img.shields.io/badge/HuggingFace-Live%20Demo-yellow?logo=huggingface" alt="Hugging Face">
  </a>
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Deep%20Learning-VAE-red">
  <img src="https://img.shields.io/badge/Framework-Gradio-orange">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen">
</p>

---

---

## 🎯 Contexte & Problématique
Les chercheurs cherchent à mieux comprendre le fonctionnement des réseaux neuronaux à partir de l'analyse des *spike trains*. Cependant, la comparaison de plusieurs architectures de *Variational Autoencoders* nécessitait jusqu'alors l'exécution de scripts Python et des manipulations techniques complexes, rendant l'analyse longue et peu accessible aux utilisateurs non spécialistes.

## 📖 Description du Projet
**NEURO-AI** est une application interactive développée dans le cadre d'un **projet de Recherche et Développement (R&D)** au **CNRS – Institut des Neurosciences Cellulaires et Intégratives (INCI)**, en collaboration avec l'**Université de Strasbourg**.

Afin de répondre à ce besoin, j'ai développé une application web interactive permettant de comparer plusieurs architectures VAE, de visualiser les espaces latents et de détecter automatiquement les neurones présentant des comportements atypiques, sans avoir à manipuler le code.

Une démonstration est disponible en ligne afin de faciliter l'exploration des différents modèles et rendre ces analyses accessibles à l'ensemble des chercheurs.

👉 **Application en ligne :** [https://huggingface.co/spaces/KineDS/Benchmark_vae](https://huggingface.co/spaces/KineDS/Benchmark_vae)
---

## 🚀 Fonctionnalités

* Comparaison interactive de plusieurs architectures VAE
* Visualisation de l'espace latent en 2D
* Détection automatique d'anomalies
* Comparaison des performances des modèles
* Interface intuitive développée avec Gradio
* Déploiement sur Hugging Face Spaces

---

## ⚙️ Comment utiliser l'application 

1. Charger les données.

2. Lancer l'analyse.
 
3. Sélectionner un modèle VAE.
   
4. Visualiser les résultats.

5. Comparer les performances des modèles.

## 🧠 Architectures comparées

* VAE + Self-Attention
* VAE + Multi-Attention
* Spiking Neural Network VAE (SNN-VAE)

---

## 🛠️ Technologies

* Python
* TensorFlow / Keras
* Gradio
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Bokeh
* Penel
* Hugging Face Spaces

---

## 🎯 Objectifs

* Explorer l'utilisation des Variational Autoencoders pour la détection d'anomalies.
* Comparer différentes architectures de Deep Learning.
* Fournir une interface interactive permettant d'analyser facilement les résultats.
* Mettre à disposition une démonstration accessible en ligne.

---
## 🌱 Contributions principales

Au-delà de la comparaison de plusieurs architectures de Variational Autoencoders, ce projet met en évidence une approche d'optimisation du coût computationnel.

Les expérimentations montrent qu'il est possible de réduire le nombre d'époques d'entraînement afin de diminuer le temps de calcul et la consommation de ressources, tout en conservant des performances comparables pour la détection d'anomalies.

Cette approche contribue au développement d'une intelligence artificielle plus sobre, en améliorant l'efficacité de l'entraînement sans compromettre la qualité des résultats.

## ▶️ Démonstration

**Hugging Face Space**

https://huggingface.co/spaces/KineDS/Benchmark_vae

---

## 🚀 Déploiement
L'application est déployée sur Hugging Face Spaces.

Le code est versionné avec Git et GitHub.

Le déploiement permet une utilisation directe depuis un navigateur web sans installation locale.

---

## 💻 Réutiliser le code
Le projet peut être réutilisé pour :

• comparer de nouvelles architectures VAE ;

• intégrer d'autres jeux de données neuronales ;

• servir de base au développement d'outils d'analyse interactifs.

---

## 🙏 Remerciements
Je tiens à exprimer ma profonde gratitude au CNRS – Institut des Neurosciences Cellulaires et Intégratives (INCI) ainsi qu'à l'Université de Strasbourg pour m'avoir accueillie dans le cadre de mon stage de Master en Data Science.
J'adresse mes sincères remerciements à M. Hugues Le Petitjean, mon encadrant de stage, pour sa disponibilité, ses conseils, son accompagnement scientifique et la confiance qu'il m'a accordée tout au long de ce projet.
Je remercie également l'ensemble des membres de l'équipe de recherche pour leur accueil, leur bienveillance et les échanges enrichissants qui ont contribué à cette expérience.


---

## 📄 Licence

Ce projet est publié à des fins de démonstration, de recherche et de portfolio.
