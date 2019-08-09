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


## Needs of this project

- frontend developers
- data exploration/descriptive statistics
- data processing/cleaning
- statistical modeling
- writeup/reporting
- etc. (be as specific as possible)

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.

    *If using offline data mention that and how they may obtain the data from the froup)*
    
3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)
4. etc...

*If your project is well underway and setup is fairly complicated (ie. requires installation of many packages) create another "setup.md" file and link to it here*  

5. Follow setup [instructions](Link to file)

## Featured Notebooks/Analysis/Deliverables
* [Notebook/Markdown/Slide Deck Title](link)
* [Notebook/Markdown/Slide DeckTitle](link)
* [Blog Post](link)


## Contributing DSWG Members

**Team Leads (Contacts) : [Full Name](https://github.com/[github handle])(@slackHandle)**

#### Other Members:

|Name     |  Slack Handle   | 
|---------|-----------------|
|[Full Name](https://github.com/[github handle])| @johnDoe        |
|[Full Name](https://github.com/[github handle]) |     @janeDoe    |

## Contact
* If you haven't joined the SF Brigade Slack, [you can do that here](http://c4sf.me/slack).  
* Our slack channel is `#datasci-projectname`
* Feel free to contact team leads with any questions or if you are interested in contributing!
