import pickle

genes_outpath = '../Data/genes.txt'
preds_outpath = '../Data/predictions.txt'
accs_outpath = '../Data/accuracies.txt'

genes = []
predictions = []
accuracies = []

with open(genes_outpath, 'wb') as fp:
    pickle.dump(genes,fp)

with open(preds_outpath, 'wb') as fp:
    pickle.dump(predictions,fp)

with open(accs_outpath, 'wb') as fp:
    pickle.dump(accuracies,fp)
