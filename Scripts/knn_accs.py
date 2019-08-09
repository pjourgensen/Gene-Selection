import pandas as pd
import pickle
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

#Returns list of cross_val_scores over fixed range for chosen number of highest scoring genes
def knn_pipeline(n):
    top = gene_ave.nlargest(n).index
    train_set = train.loc[:,top]

    knn_acc = []
    for i in range(10):
        KNN_model = KNeighborsClassifier(n_neighbors=i+1)
        cv = cross_val_score(KNN_model,train_set,target_train,cv=5)
        knn_acc.append(cv.mean())

    return knn_acc

train_inpath = '../Data/train_data.csv'
target_train_inpath = '../Data/train_target.csv'
scores_inpath = '../Data/scores.txt'
fig_outpath = '../Figures/knn_accs.jpg'

train = pd.read_csv(train_inpath)
target_train = pd.read_csv(target_train_inpath)

with open(scores_inpath,'rb') as fp:
    gene_ave = pickle.load(fp)

KNN_acc1 = knn_pipeline(1)
KNN_acc3 = knn_pipeline(3)
KNN_acc5 = knn_pipeline(5)
KNN_acc10 = knn_pipeline(10)
KNN_acc50 = knn_pipeline(50)

plt.figure(figsize=(12,6))

plt.plot(KNN_acc1, color='red',marker='o', label='1')
plt.plot(KNN_acc3, color='blue',marker='o', label='3')
plt.plot(KNN_acc5, color='yellow',marker='o', label='5')
plt.plot(KNN_acc10, color='green',marker='o', label='10')
plt.plot(KNN_acc50, color='orange',marker='o', label='50')

plt.title('Accuracy vs. # of Neighbors')
plt.xlabel('# of Neighbors')
plt.ylabel('Accuracy')
plt.ylim(bottom=0.825)
plt.legend()
plt.savefig(fig_outpath)
