import json
#test to find compat for cpu by already selcting a motherboard
#first check by socket

# test acces motherboard
file_path_mb = r".\open-db\Motherboard\fdb9c244-0b4a-46c4-9ac5-ac7e43af88fc.json"
with open(file_path_mb,'r') as file:
    data = json.load(file)

#print(json.dumps(data, indent=1))

#Once selected  dump in json
Asus_X870_PRIME_JSON = json.dumps(data)
#print(Asus_X870_PRIME_JSON)
#print(type(Asus_X870_PRIME_JSON))

#then covert in dict for python
new_Asus_X870_PRIME = json.loads(Asus_X870_PRIME_JSON)
#print(new_Asus_X870_PRIME)
#print(type(new_Asus_X870_PRIME))

#Them test to print the socket of motherboard by accesing their props
print(new_Asus_X870_PRIME["socket"])

#then store the value for check compat later
socket_new_Asus_X870_PRIME = new_Asus_X870_PRIME["socket"]



"""
NOW REPEAT FOR CPU
"""

# test acces CPU
file_path_cpu = r".\open-db\CPU\b7d6999e-97a3-4ca1-b9d4-f266e4d60135.json"
with open(file_path_cpu,'r') as file:
    data = json.load(file)

#print(json.dumps(data, indent=1))
AMD_Ryzen_5_8400F_JSON = json.dumps(data)

new_AMD_Ryzen_5_8400F = json.loads(AMD_Ryzen_5_8400F_JSON)

#Them test to print the socket of motherboard by accesing their props
print(new_AMD_Ryzen_5_8400F["socket"])

#then store the value for check compat later
socket_new_AMD_Ryzen_5_8400F = new_AMD_Ryzen_5_8400F["socket"]

if socket_new_Asus_X870_PRIME == socket_new_AMD_Ryzen_5_8400F:
    print("compatible")