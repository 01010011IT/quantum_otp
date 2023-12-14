
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from collections import Counter

n=16
otpArray = []

def generate_otp ():
    circuit = QuantumCircuit(n,n) 
    circuit.h(range(n))
    circuit.measure_all()
    backend = Aer.get_backend("qasm_simulator")
    job = execute(circuit, backend, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    output = list(counts)[:-1]
    every_output= [str(num)[:17] for num in output]
    circuit.reset(range(n))
    print(every_output)
    circuit.draw('mpl')
    return circuit,  every_output

circuit, output = generate_otp()

every_otp= []
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
    result_string = ''.join(string_list)
    otp_Result = result_string[:4]
    every_otp.append(otp_Result)
    return otp_Result 
    
for i in output:
    conver_to_decimal(i)

print("every_otp", every_otp)


element_counts = Counter(every_otp)

for element, count in element_counts.items():
    if count > 1:
        print(f"Element {element} repeats {count} times.")
    
def save_output_to_file(every_otp):
    with open('DataBase.txt', 'a') as file:
        for value in every_otp:
            file.write(value + '\n')

new_output = every_otp
save_output_to_file(new_output)


def read_values_from_file(file_path='.\DataBase.txt'):
    with open(file_path, 'r') as file:
        values = file.readlines()
    values = [value.strip() for value in values]
    return values


# Read the values from the file
file_path = 'DataBase.txt'
saved_values = read_values_from_file(file_path)

# Use the saved values
for value in saved_values:
    otpArray.append(value)

print("otpArray", otpArray)
