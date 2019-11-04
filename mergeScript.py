import pandas as pd
import numpy as np

df = pd.read_csv('data/nytimes_presidential_elections_2016_results_county.csv')

clintonVotes = df['Clinton'].groupby(df['State'])
trumpVotes = df['Trump'].groupby(df['State'])

namesDf = pd.DataFrame(data=trumpVotes.sum().index, columns=['State'])
trumpDf = pd.DataFrame(data=trumpVotes.sum().values, columns=['Trump'])
clintonDf = pd.DataFrame(data=clintonVotes.sum().values, columns=['Clinton'])

tm = pds.merge(namesDf, trumpDf, left_index=True, right_index=True)
stateVotes = pd.merge(tm, clintonDf, left_index=True, right_index=True)

stateVotes.to_csv(r'data/state-votes.csv')