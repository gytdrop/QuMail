import checking
import time
from quantum_engine import QuEngine
from sync_timing import get_navic_timestamp
import sync_timing as navic
from encryption import QuVault



def run_qumail():

    print("------------ Initialising QuMail ------------")
    print("checking",end='')
    time.sleep(0.5)
    print(".",end='')
    time.sleep(0.5)
    print(".",end='')
    time.sleep(0.5)
    print(".",end='')
    time.sleep(0.5)
#starting the Quantum Handshake
#-------------------------------
   

    engine = QuEngine()
    shared_key , s_bits, r_results = engine.generate_quantum_key(120)
   
# Now let us check the Eavesdrppers such that if error rate > 11% then ---> someone listening
#--------------------------------
    sample = 10
    errors = sum(1 for i in range(sample) if s_bits[i] != r_results[i])
    if (errors/sample)>0.11:
        print("[i] Alert: Eavesdropper detected on the Link, Aborting...")
        return
#--------------------------------
#encrypting the message

    message = input("Enter your secret message:\n\n")
    
    encrypted_mail = QuVault.xor_cipher(message, shared_key)
#---------------------------------
    print(f'\n[+] sync ID: {navic.get_navic_timestamp()}')
    print(f'[+] Encrypted Qumail Payload: {encrypted_mail}')
    print('------  Transmission Secure -----')

if __name__ == "__main__":
    run_qumail()




