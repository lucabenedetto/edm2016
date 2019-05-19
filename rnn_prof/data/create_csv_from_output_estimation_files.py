import pandas as pd
import os

def tail_1(f):
    stdin,stdout = os.popen2("tail -n 1 "+f)
    stdin.close()
    lines = stdout.readlines()
    stdout.close()
    return lines[0]

directory = 'output-by_skill-20190519-1725-kdd'

columns_names = ['skill_id', 'mean_acc', 'mean_auc', 'mean_log_loss']
df = pd.DataFrame(columns=columns_names)

for filename in os.listdir(directory):
    if filename.endswith('output-estimation'):
        print('[INFO] File %s' %filename)
        skill_id = int(filename.split('-')[0].split('_')[-1])
        print('[INFO] Skill id = %d' %skill_id)
        line = tail_1(directory+'/'+filename)
        if len(line.split(' '))==12:
            accuracy = float(line.split(' ')[6])
            auc = float(line.split(' ')[8])
            log_loss = float(line.split(' ')[11][:-1])
            print('[INFO] ACC %.2f, AUC %.2f, L_L %.2f' %(accuracy, auc, log_loss))
            df = df.append(pd.Series([skill_id, accuracy, auc, log_loss]).rename(lambda x: df.columns[x]), ignore_index=True)
df.to_csv(directory+'/total_output.csv')

