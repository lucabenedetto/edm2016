import pandas as pd

def create_dataset_by_skill(skill_id):
    df = pd.read_csv('skill_builder_data_corrected.csv', low_memory=False)
    df = df[df['skill_id']==skill_id]
    df.to_csv('by_skill/skill_builder_data_corrected_' + str(skill_id) + '.csv')

df = pd.read_csv('skill_builder_data_corrected.csv', low_memory=False)
skill_list = df.skill_id.unique()
for skill in skill_list:
    create_dataset_by_skill(skill)
