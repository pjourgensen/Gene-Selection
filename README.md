# Gene Selection for Acute Leukemias

#### -- Project Status: [Completed]

## Intro/Objective
The purposes of this project are ultimately to help guide genetic research and to construct a classifier that may quickly distinguish Acute Lymphoblastic Leukemia from Acute Myeloid Leukemia to ensure the patient receives the proper treatment. This is achieved by identifying combinations of genes that play a significant role in distinguishing the two cancer classes.  The struggle in this process is that the data contains very few samples (72) with respect to the number of features (9000+). In this project, I approach this challenge by leveraging bootstrapping with artificial neural networks to form a collection of models that can then be used to score and rank each gene. Finally, the number of highest scoring genes is optimized with a K-Nearest Neighbors model to identify the sub-selection most suited to distinguising the two cancer classes.

### Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling

### Technologies
* Python, jupyter
* Pandas, Numpy
* SKLearn
* Tensorflow
* Seaborn, Matplotlib

## Project Description
(Provide more detailed overview of the project.  Talk a bit about your data sources and what questions and hypothesis you are exploring. What specific data analysis/visualization and modelling work are you using to solve the problem? What blockers and challenges are you facing?  Feel free to number or bullet point things here)
* Data  
   * Data consists of 72 patients with over 9000 gene expression levels
   * 47 classified as patients with ALL, 25 with AML
   * Data already cleaned and suitable for use in ML models
* Baseline Model for Bootstrapping
   * Wanted a model that allowed for nonlinear combinations of gene expressions
   * Needed a model that remained weak and trained quickly
   * Chose to use a small densely connected neural network with high dropout rate to satisfy the preconditions
* Gene Scoring
   * Initial plan was to use individual model accuracies to score the individual genes
   * Majority of models only predicted majority class, however, so new methodology needed to be developed
   * Decided to only consider models that scored above that threshold to identify genes (or combinations) that may have predictive power
* KNN Optimization
   * Performed a grid search over the number of highest scoring genes to find the optimal number suited for classification

## Getting Started

1. Clone this repo.
2. Raw Data can be downloaded from [here](https://www.kaggle.com/crawford/gene-expression).    
3. Download the requirements.
4. If your preference is for notebooks, simply open and run "final_notebook.ipynb"
5. Else, run "main.py"

## For more detail and discussion:
* [Blog Post](https://pjourgensen.github.io/genes.html)

