import pandas as pd
import numpy as np


def create_dataset_by_skill(skill_id):
    df = pd.read_csv('skill_builder_data_corrected.csv', low_memory=False)
    df = df[df['skill_id']==skill_id]
    df.to_csv('by_skill_assistments_NEW/skill_builder_data_corrected_' + str(skill_id) + '.csv')


df = pd.read_csv('skill_builder_data_corrected.csv', low_memory=False)

dict_mapping = dict()
for skill_id, skill_name in df.sort(['skill_id', 'skill_name']).drop_duplicates(['skill_id', 'skill_name'])[
    ['skill_id', 'skill_name']
].values:
    if skill_id not in dict_mapping.keys():
        if type(skill_name) == str:
            dict_mapping[skill_id] = skill_name
        else:
            dict_mapping[skill_id] = str(skill_id)+'_missing_skill_name' if np.isnan(skill_name) else skill_name
pd.DataFrame({
    'skill_id': list(dict_mapping.keys()),
    'skill_name': list(dict_mapping.values())
}).to_csv('by_skill_assistments_mapping_idx2name.csv', sep='\t')
print('[INFO] Saved file containing index-name mapping')

skill_list = df.skill_id.unique()
for skill in skill_list:
    if np.isnan(skill):
        print('[WARNING] Encountered skill with nan as index')
        print('[INFO] Working on skill %f' % skill)
        create_dataset_by_skill(skill)
        print('[INFO] Stored DF for the skill')
    else:
        print('[INFO] Working on skill %d' % skill)
        create_dataset_by_skill(skill)
        print('[INFO] Stored DF for the skill')
