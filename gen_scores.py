import pandas as pd
import pickle

data_inpath = '../Data/train_data.csv'
wts4_inpath = '../Data/weights4.txt'
genes_inpath = '../Data/genes.txt'
scores_outpath = '../Data/scores.txt'

df = pd.read_csv(data_inpath)

with open(wts4_inpath,'rb') as fp:
    weights4 = pickle.load(fp)
with open(genes_inpath,'rb') as fp:
    genes = pickle.load(fp)

num_genes = len(df.columns)

gene_ave = pd.Series(data=np.zeros(num_genes),index=df.columns)

#If a gene is used in a model, add that model's weight to the gene's score and average over number of occurrences
for i in gene_ave.index:
    count = 0
    for j in range(len(genes)):
        if i in genes[j]:
            gene_ave[i] = ((gene_ave[i]*count) + weights4[j]) / (count + 1)
            count += 1

with open(scores_outpath,'wb') as fp:
    pickle.dump(gene_ave,fp)
