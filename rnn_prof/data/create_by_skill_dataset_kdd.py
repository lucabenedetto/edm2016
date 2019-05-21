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


filepath = 'bridge_to_algebra_2006_2007_train.txt'

df = pd.read_csv(filepath, sep='\t', low_memory=False)
original_columns = df.columns
df['question'] = df.apply(lambda r: r['Problem Name'] + '_' + r['Step Name'], axis=1)
print('[INFO] Collected dataframe')

item_skill_mapping_df = get_item_skill_mapping(filepath)
print('[INFO] Generated item skill mapping')

df_mapping_list = pd.DataFrame(columns=['skill_id', 'skill_name'])
for skill_id, skill_name in item_skill_mapping_df[['skill_id', 'skill_name']].values:
    df_mapping_list.append({'skill_id': skill_id, 'skill_name': skill_name}, ignore_index=True)
df_mapping_list.to_csv('by_skill_kdd_mapping_idx2name.csv', sep='\t')
df_mapping_list = None
print('[INFO] Saved file containing index-name mapping')

for skill_id, skill_name in item_skill_mapping_df[['skill_id', 'skill_name']].values:
    print('[INFO] Working on skill %d' % skill_id)
    list_items_to_keep = list(item_skill_mapping_df[item_skill_mapping_df['skill_id'] == skill_id]['question'].values)
    local_df = df[df['question'].isin(list_items_to_keep)]
    print('[INFO] Number of rows %d' % len(local_df.index))
    local_df[original_columns].to_csv('by_skill_kdd_NEW/bridge_to_algebra_2006_2007_train_%d.txt' % skill_id, sep='\t')
    print('[INFO] Stored DF for the skill')
