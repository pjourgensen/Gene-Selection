import pickle

preds_inpath = '../Data/predictions.txt'
accs_inpath = '../Data/accuracies.txt'
wts1_outpath = '../Data/weights1.txt'
wts2_outpath = '../Data/weights2.txt'
wts3_outpath = '../Data/weights3.txt'
wts4_outpath = '../Data/weights4.txt'

with open(preds_inpath, "rb") as fp:
    predictions = pickle.load(fp)

with open(accs_inpath, "rb") as fp:
    accuracies = pickle.load(fp)

#Convert Predictions to -1/+1
for i in range(len(predictions)):
    for j in range(len(predictions[i])):
        if predictions[i][j] == 0:
            predictions[i][j] = -1

#Models get equal weight
wts1 = [1]*len(accuracies)

#Models are weighted by their accuracy
wts2 = accuracies

#Models are weighted by Relu of accuracy; Threshold is mode accuracy
mode = max(set(accuracies), key=accuracies.count)
wts3 = []

for i in accuracies:
    if i <= mode:
        wts3.append(0)
    else:
        wts3.append(i-mode)

#Models are weighted by exponential Relu of accuracy; Threshold is mode accuracy
wts4 = []

for i in wts3:
    wts4.append(np.exp(i)-1)

#Save weights
with open(wts1_outpath,'wb') as fp:
    pickle.dump(wts1, fp)

with open(wts2_outpath,'wb') as fp:
    pickle.dump(wts2, fp)

with open(wts3_outpath,'wb') as fp:
    pickle.dump(wts3, fp)

with open(wts4_outpath,'wb') as fp:
    pickle.dump(wts4, fp)
