import os,json
"""
From one_filter_test, this test will check compat for each cpu json files and print the count of
compatible cpu by  printing ther count of compats by socket
"""

#First the choosen motherboard
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
#print(new_Asus_X870_PRIME["socket"])

#then store the value for check compat later
socket_new_Asus_X870_PRIME = new_Asus_X870_PRIME["socket"]

print(new_Asus_X870_PRIME["metadata"]["name"] + " is compatible with following CPUs:")
print("\n")
"""
NOW, Read all cpu json files and count their compat for choosen cpu
"""

compatBySocket = 0

#list for sort names
compat_cpu = []

path_to_CPU_json = r'.\open-db\CPU'

#loop for each cpu json file to print each name and count if compatible
for file_name in [file for file in os.listdir(path_to_CPU_json) if file.endswith('.json')]:
    new_path = os.path.join(path_to_CPU_json,file_name)
    #new_file_path = path_to_CPU_json + file_name
    with open(new_path,'r') as json_file:
        data = json.load(json_file)
        if data["socket"] == socket_new_Asus_X870_PRIME:
            #print(data["metadata"]["name"])
            compat_cpu.append(data["metadata"]["name"])
            compatBySocket += 1
print("\n")
print("Total compatible CPUs " + str(compatBySocket))

compat_cpu.sort()

for e in compat_cpu:
    print(e)