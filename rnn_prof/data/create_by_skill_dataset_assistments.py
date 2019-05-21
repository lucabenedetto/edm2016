import pandas as pd


def create_dataset_by_skill(skill_id):
    df = pd.read_csv('skill_builder_data_corrected.csv', low_memory=False)
    df = df[df['skill_id']==skill_id]
    df.to_csv('by_skill/skill_builder_data_corrected_' + str(skill_id) + '.csv')


df = pd.read_csv('skill_builder_data_corrected.csv', low_memory=False)

dict_mapping = dict()
for skill_id, skill_name in df[['skill_id', 'skill_name']].values:
    if skill_id not in dict_mapping.keys():
        dict_mapping[skill_id] = skill_name
pd.DataFrame(dict_mapping).to_csv('by_skill_assistment_mapping_idx2name.csv', sep='\t')
print('[INFO] Saved file containing index-name mapping')

skill_list = df.skill_id.unique()
for skill in skill_list:
    create_dataset_by_skill(skill)
