import subprocess, importlib , sys, time, os

requirements = ['qiskit', 'qiskit_aer', 'numpy']

for i in requirements:
    print(f"checking for {i}...")
    try:
        importlib.import_module(i.replace('-','_'))
    except ImportError:
        print(f"MODULE MISSING!\nInstalling {i} please wait...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', i])
    print('Installed Successfully!')
        
print('perfect!')
print('let us start...')
time.sleep(2)

os.system('cls||clear')