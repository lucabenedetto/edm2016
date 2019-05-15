import pandas as pd

def get_item_skill_mapping(filepath):
    df = pd.read_csv(filepath, sep='\t', low_memory=False)
    df[['KC(SubSkills)']] = df[['KC(SubSkills)']].fillna(value='.')
    df['question'] = df.apply(lambda r: r['Problem Name'] + '_' + r['Step Name'], axis=1)
    df = df.drop_duplicates('question')
    skill_set = set()
    for skills in df['KC(SubSkills)'].values:
        for skill in skills.split(' -- '):
            skill_set.add(skill)
    skill_dict = {name: idx for (idx, name) in enumerate(skill_set)}
    result_df = pd.DataFrame(columns=['question', 'skill_id', 'skill_name'])
    for question, skills in df[['question', 'KC(SubSkills)']].values:
        for skill in skills.split(' -- '):
            result_df = result_df.append(
                {'question': question, 'skill_id': skill_dict.get(skill), 'skill_name': skill}, ignore_index=True)
    return result_df

#####

filepath = 'bridge_to_algebra_2006_2007_train.txt'

df = pd.read_csv(filepath, sep='\t', low_memory=False)
df['question'] = df.apply(lambda r: r['Problem Name'] + '_' + r['Step Name'], axis=1)
print('[INFO] Collected dataframe')

item_skill_mapping_df = get_item_skill_mapping(filepath)
print('[INFO] Genereted item skill mapping')

skill_list = item_skill_mapping_df['skill_id'].unique()
print('[INFO] Created list of skills')

for skill_id in skill_list:
    print('[INFO] Working on skill %d' %skill_id)
    list_items_to_keep = list(item_skill_mapping_df[item_skill_mapping_df['skill_id']==skill_id]['question'].values)
    df = df[df['question'].isin(list_items_to_keep)]
    df.drop('question', axis=1).to_csv('by_skill_kdd/bridge_to_algebra_2006_2007_train_%d.csv' %skill_id)
    print('[INFO] Stored DF for the skill')

