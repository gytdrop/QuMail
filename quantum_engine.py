from qiskit import QuantumCircuit as qc , transpile as tp
from qiskit_aer import Aer
#we are uing ibm qiskit for the project
import numpy as np

# The Quantum Encoding function  -   The Sender
#---------------------------------------
#if basis=0 then Z basis
#if basis=1 then X basis
#the bit is as usual 0,1
#---------------------------------------
class QuEngine:
    def create_qubit(self, bit, basis):
        q = qc(1,1)
        if bit ==1:
            q.x(0)
        if basis == 1:
            q.h(0)
        return q


#Quantum Channel  The Reciever

#---------------------------------------
# what it does?
#The reciever recieves the qubit and then measures them in a random basis. If he picks the wrong basis then --> 50% chance of getting wrong bit
#---------------------------------------

    def measure_qubit(self,q,basis):
        if basis == 1:
            q.h(0)
        q.measure(0,0)
        backend = Aer.get_backend("qasm_simulator")
        job = backend.run(tp(q,backend), shots=1, memory=True)
        result = job.result().get_memory()[0]
        return int(result)


#The Qumail Handshake - The synchroniser 
#synchronises using NavIC time-stamps

#------------------------------------  
#The no. of qubits

#    n = 100 
#------------------------------------
    def generate_quantum_key(self,n=100):
        senderBits = np.random.randint(2,size=n)
        recieverBits = np.random.randint(2,size=n)
        
        senderBases = np.random.randint(2,size=n)
        recieverBases = np.random.randint(2,size=n)

        qubits = []
        for i in range(n):
            q = self.create_qubit(senderBits[i], senderBases[i])
            result = self.measure_qubit(q, recieverBases[i])
            qubits.append(result)


    #shifting only keeps bits where bases matched

        key = [senderBits[i] for i in range(n) if senderBases[i] == recieverBases[i]]
        print(f"QuMail Key Length : {len(key)} bits")
        return key, senderBits,qubits