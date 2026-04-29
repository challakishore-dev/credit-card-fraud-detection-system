import os, subprocess, sys
for f in ['data','models','outputs','templates','src']:
    os.makedirs(f, exist_ok=True)

def run(cmd):
    subprocess.check_call(cmd, shell=True)

if not os.path.exists('data/creditcard.csv'):
    run('python src/generate_data.py')
if not os.path.exists('models/model.pkl'):
    run('python src/train.py')

print('Opening server on http://127.0.0.1:8000')
run('uvicorn app:app --reload')
