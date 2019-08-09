import pandas

data_inpath = '../Data/clean_data.csv'
target_inpath = '../Data/clean_target.csv'

train_data_outpath = '../Data/train_data.csv'
test_data_outpath = '../Data/test_data.csv'
train_target_outpath = '../Data/train_target.csv'
test_target_outpath = '../Data/test_target.csv'

df = pd.read_csv(data_inpath)
target = pd.read_csv(target_inpath)

train = df.iloc[:38,:]
train.to_csv(train_data_outpath)

test = df.iloc[38:,:]
test.to_csv(test_data_outpath)

target_train = target.iloc[:38,1]
target_train.to_csv(train_target_outpath)

target_test = target.iloc[38:,1]
target_test.to_csv(test_target_outpath)
