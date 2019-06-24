import pandas as pd
import pickle
import random
import tensorflow as tf

#Returns subset of data and corresponding target values
def subset(rows,columns,data,target):
    return data.iloc[rows,columns], target.iloc[rows]

train_inpath = '../Data/train_data.csv'
test_inpath = '../Data/test_data.csv'
target_train_inpath = '../Data/train_target.csv'
target_test_inpath = '../Data/test_target.csv'

genes_inpath = '../Data/genes.txt'
preds_inpath = '../Data/predictions.txt'
accs_inpath = '../Data/accuracies.txt'

train = pd.read_csv(train_inpath)
test = pd.read_csv(test_inpath)
target_train = pd.read_csv(target_train_inpath)
target_test = pd.read_csv(target_test_inpath)

with open(genes_inpath, "rb") as fp:
    genes = pickle.load(fp)

with open(preds_inpath, "rb") as fp:
    predictions = pickle.load(fp)

with open(accs_inpath, "rb") as fp:
    accuracies = pickle.load(fp)

#Set size of subset (num_rows x num_cols)
num_rows = 30
num_cols = 50
reps = 1

train_rows = len(train)
train_cols = len(train.columns)
test_rows = len(test)

for iters in range(reps):
    #Suppress output except for error messages
    tf.logging.set_verbosity(tf.logging.ERROR)

    #Select Rows and Cols
    rows = random.sample(range(train_rows),num_rows)
    cols = random.sample(range(train_cols),num_cols)

    #Save Genes used for model
    genes.append(train.columns[cols])

    #feature columns
    feature_columns = []
    for i in train.columns[cols]:
        feature_columns.append(tf.feature_column.numeric_column(i))

    #Model Initialization
    classifier = tf.estimator.DNNClassifier(
        feature_columns=feature_columns,
        hidden_units=[25, 10, 5],
        optimizer=tf.train.AdamOptimizer(1e-2),
        n_classes=2,
        dropout=0.2,
    )

    #Input Function
    train_input_fn = tf.estimator.inputs.pandas_input_fn(
        x=subset(rows,cols,train,target_train)[0],
        y=subset(rows,cols,train,target_train)[1],
        num_epochs=10,
        batch_size=num_rows,
        shuffle=True
    )

    #model training
    classifier.train(input_fn=train_input_fn, steps=1000)

    #eval function
    test_input_fn = tf.estimator.inputs.pandas_input_fn(
        x=test.iloc[:,cols],
        y=target_test.iloc[:],
        num_epochs=1,
        shuffle=False
    )

    #predictions
    preds = list(classifier.predict(test_input_fn))

    pred_class = [p["classes"] for p in preds]

    preds = []

    for i in range(len(pred_class)):
        preds.append(int(pred_class[i][0]))

    predictions.append(preds)

    accuracies.append(accuracy_score(target_test,preds))

#Store updated lists

with open(genes_inpath, 'wb') as fp:
    pickle.dump(genes, fp)

with open(preds_inpath, 'wb') as fp:
    pickle.dump(predictions, fp)

with open(accs_inpath, 'wb') as fp:
    pickle.dump(accuracies, fp)
