import pandas as pd

def create_dataset_by_skill(skill_id):
    df = pd.read_csv('bridge_to_algebra_2006_2007_train.txt', sep='\t', low_memory=False)
    df[['KC(SubSkills)']] = df[['KC(SubSkills)']].fillna(value='.')
    df = df[df['KC(SubSkills)']==skill_id]
    df.to_csv('by_skill_kdd/bridge_to_algebra_2006_2007_train_' + str(skill_id) + '.csv')

df = pd.read_csv('bridge_to_algebra_2006_2007_train.txt', sep='\t', low_memory=False)
skill_list = df['KC(SubSkills)'].unique()
for skill in skill_list:
    create_dataset_by_skill(skill)
