import pandas as pd

#One hot encode target variable
def impute_target(x):
    if x == 'ALL':
        return 1
    else:
        return 0

target_path = '../Data/actual.csv'
output_path = '../Data/clean_target.csv'

target = pd.read_csv(target_path)
target.set_index('patient',inplace=True)
target.index = target.index.astype('int64')
target.sort_index(inplace=True)
del target.index.name

target['One-hot'] = target['cancer'].apply(lambda x: impute_target(x))

target.to_csv(output_path)
