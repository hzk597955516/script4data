import pandas as pd


PDBS_DIR = './structures'
SAMPLES_DIR = './casp15_eigenfold'


DF = pd.read_csv('./casp15.csv', index_col='name')
df = pd.read_csv(SAMPLES_DIR + '.csv', index_col='path')
df['name'] = [path.split('/')[-1] for path in df.index]
df = df.set_index('name')
selected_df = pd.DataFrame([subdf.iloc[subdf.elbo_Y.argmax()] for key, subdf in df.groupby('name')])
for key in 'rmsd', 'tm', 'gdt_ts', 'lddt':
    print(key, '\t', 'mean', round(selected_df[key].mean(), 2), 'std', round(selected_df[key].std(), 2), 'median', round(selected_df[key].median(), 2))