import pandas as pd
import pickle
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Returns ensembled prediction accuracy as a function of the number of models
def ensemble(predictions,weights,target):
    acc_list = []
    for i in range(len(predictions)):
        ens_preds = final_preds(predictions[:(i+1)],weights[:(i+1)])
        acc_list.append(accuracy_score(target,ens_preds))
    return acc_list

preds_inpath = '../Data/predictions.txt'
wts1_inpath = '../Data/weights1.txt'
wts2_inpath = '../Data/weights2.txt'
wts3_inpath = '../Data/weights3.txt'
wts4_inpath = '../Data/weights4.txt'
test_target_inpath = '../Data/test_target.csv'
figure_path = '../Figures/ensemble_accs.jpg'

with open(pred_inpath,'rb') as fp:
    predictions = pickle.load(fp)
with open(wts1_inpath,'rb') as fp:
    weights1 = pickle.load(fp)
with open(wts2_inpath,'rb') as fp:
    weights2 = pickle.load(fp)
with open(wts3_inpath,'rb') as fp:
    weights3 = pickle.load(fp)
with open(wts4_inpath,'rb') as fp:
    weights4 = pickle.load(fp)

test_target = pd.read_csv(test_target_inpath)

acc_list1 = ensemble(predictions,weights1,test_target)
acc_list2 = ensemble(predictions,weights2,test_target)
acc_list3 = ensemble(predictions,weights3,test_target)
acc_list4 = ensemble(predictions,weights4,test_target)

plt.figure(figsize = (16,8))

plt.plot(acc_list1,color='red',label='Equal')
plt.plot(acc_list2,'b--',label='Accuracy')
plt.plot(acc_list3,color='green',label='ReLu_Lin')
plt.plot(acc_list4,color='yellow',label='ReLu_Exp')

plt.title('Accuracy vs. # of Models')
plt.xlabel('# of Models')
plt.ylabel('Accuracy')
plt.ylim(bottom=0.4)
plt.legend()
plt.savefig(figure_path)
