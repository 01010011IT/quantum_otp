# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:22:46 2023

@author: Sarah
"""
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

n=16
otpArray = []

def generate_otp ():
    circuit = QuantumCircuit(n,n) 
    circuit.h(range(n))
    circuit.measure_all()
    backend = Aer.get_backend("qasm_simulator")
    job = execute(circuit, backend, shots=1,  timeout=60)
    result = job.result()
    counts = result.get_counts(circuit)
    output = list(counts)[0][0:17]
    circuit.reset(range(n))
    circuit.draw('mpl')
    return circuit, output

circuit, output = generate_otp()


def conver_to_decimal(binary_string):
    binary_string = ''.join(filter(lambda x: x in '01', binary_string))
    chunks = [binary_string[i:i+4] for i in range(0, len(binary_string), 4)]
    decimal_values = []
    for chunk in chunks:
        try:
            decimal_values.append(int(chunk, 2))
        except ValueError:
            print(f"Error: '{chunk}' is not a valid 4-bit binary chunk.")
    string_list = list(map(str, decimal_values))
    # Join the string representations without a separator
    result_string = ''.join(string_list)
    otp_Result = result_string[:4]
    return otp_Result 
    
otp_Result  = conver_to_decimal(output)

if otp_Result in otpArray: 
   circuit.reset(range(n))
   circuit, output = generate_otp() 
   otp_Result  = conver_to_decimal(output)


def save_output_to_file(output):
    with open('otpDataBases.txt', 'a') as file:
        file.write(output + '\n')

new_output = otp_Result 
save_output_to_file(otp_Result )


def read_values_from_file(file_path='.\otpDataBases.txt'):
    with open(file_path, 'r') as file:
        values = file.readlines()
    values = [value.strip() for value in values]
    return values


# Read the values from the file
file_path = 'otpDataBases.txt'
saved_values = read_values_from_file(file_path)

# Use the saved values
for value in saved_values:
    otpArray.append(value)

print("otpArray", otpArray)