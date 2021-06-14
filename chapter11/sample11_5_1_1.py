import pickle
data = {'menbers':{'alice', 'bob', 'charlie'}}
with open('sample11_5_1.pickle', 'wb') as f:
    pickle.dump(data, f)
