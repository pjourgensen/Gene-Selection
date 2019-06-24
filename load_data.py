import pandas as pd

train_data_path = '../Data/data_set_ALL_AML_train.csv'
test_data_path = '../Data/data_set_ALL_AML_independent.csv'
output_path = '../Data/clean_data.csv'

#load data
df = pd.concat([pd.read_csv(train_data_path),pd.read_csv(test_data_path)],axis=1)

#clean & transpose
patients = [i for i in df.columns if i[:4] != 'call']
df = df.loc[:,patients]
gene_description = df['Gene Description']
df.drop('Gene Description',axis=1,inplace=True)
df.set_index(df.iloc[:,0],inplace=True)
df.drop('Gene Accession Number',axis=1,inplace=True)
df = df.transpose()
df.index = df.index.astype('int64')
df.sort_index(inplace=True)

df.to_csv(output_path)
