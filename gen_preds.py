import pickle

#Takes in a matrix of predictions, multiples them by their corresponding weight and averages the sum across all
#models to form the ensembled prediction.
def final_preds(pred_list,weights):
    final_preds = []
    for i in range(len(pred_list[0])):
        pred_sum = 0
        for j in range(len(pred_list)):
            pred_sum += pred_list[j][i]*weights[j]
        if pred_sum == 0:
            final_preds.append(pred_sum)
        else:
            final_preds.append(pred_sum/abs(pred_sum))
    return final_preds

preds_inpath = '../Data/predictions.txt'
wts1_inpath = '../Data/weights1.txt'
wts2_inpath = '../Data/weights2.txt'
wts3_inpath = '../Data/weights3.txt'
wts4_inpath = '../Data/weights4.txt'
preds1_outpath = '../Data/preds1.txt'
preds2_outpath = '../Data/preds2.txt'
preds3_outpath = '../Data/preds3.txt'
preds4_outpath = '../Data/preds4.txt'

with open(preds_inpath,'rb') as fp:
    predictions = pickle.load(fp)
with open(wts1_inpath,'rb') as fp:
    weights1 = pickle.load(fp)
with open(wts2_inpath,'rb') as fp:
    weights2 = pickle.load(fp)
with open(wts3_inpath,'rb') as fp:
    weights3 = pickle.load(fp)
with open(wts4_inpath,'rb') as fp:
    weights4 = pickle.load(fp)

preds1 = final_preds(predictions,weights1)
preds2 = final_preds(predictions,weights2)
preds3 = final_preds(predictions,weights3)
preds4 = final_preds(predictions,weights4)

with open(preds1_outpath,'wb') as fp:
    pickle.dump(preds1,fp)
with open(preds2_outpath,'wb') as fp:
    pickle.dump(preds2,fp)
with open(preds3_outpath,'wb') as fp:
    pickle.dump(preds3,fp)
with open(preds4_outpath,'wb') as fp:
    pickle.dump(preds4,fp)
