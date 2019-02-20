import pandas as pd
import pickle

# Difficulties
pickle_in = open('test_responses_difficulty.pickle', 'rb')
difficulty = pickle.load(pickle_in)
pickle_in = open('item_id_mapping.pickle', 'rb')
ids = pickle.load(pickle_in)
df = pd.DataFrame({'difficulty':difficulty.flatten(), 'id':ids})
df.to_csv('id_difficulty_map')

# Skills
pickle_in = open('test_responses_skills.pickle', 'rb')
skills = pickle.load(pickle_in)
pickle_in = open('user_id_mapping.pickle', 'rb')
ids = pickle.load(pickle_in)
df = pd.DataFrame({'skill':skills.flatten(), 'id':ids})
df.to_csv('id_skill_map')
