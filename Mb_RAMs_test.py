import os,json
"""
From one_filter_test, this test will check compat for each RAM json files and print the count of
compatible with choosen motherboard by  printing ther count of compats by ram type
"""

#First the choosen motherboard
file_path_mb = r".\open-db\Motherboard\1e962e41-f88e-4a8d-b426-f29adcbf4747.json"
with open(file_path_mb,'r') as file:
    data = json.load(file)

#print(json.dumps(data, indent=1))

#Once selected  dump in json
MSI_Z690_MEG_JSON = json.dumps(data)
#print(Asus_X870_PRIME_JSON)
#print(type(Asus_X870_PRIME_JSON))

#then covert in dict for python
new_MSI_Z690_MEG = json.loads(MSI_Z690_MEG_JSON)
#print(new_Asus_X870_PRIME)
#print(type(new_Asus_X870_PRIME))

#Them test to print the socket of motherboard by accesing their props
#print(new_Asus_X870_PRIME["socket"])

#then store the value for check compat later
ramType_new_MSI_Z690_MEG = new_MSI_Z690_MEG["memory"]["ram_type"]

print(new_MSI_Z690_MEG["metadata"]["name"] + " is compatible with following RAMs:")
print("\n")

"""
NOW, Read all motherbaord json files and count their compat for choosen RAMs
"""

compatByMType = 0

#list for sort names
compat_RAM = []

path_to_RAM_json = r'.\open-db\RAM'

#loop for each cpu json file to print each name and count if compatible
for file_name in [file for file in os.listdir(path_to_RAM_json) if file.endswith('.json')]:
    new_path = os.path.join(path_to_RAM_json,file_name)
    #new_file_path = path_to_RAM_json + file_name
    with open(new_path,'r') as json_file:
        data = json.load(json_file)
        if data["ram_type"] == ramType_new_MSI_Z690_MEG:
            #print(data["metadata"]["name"])
            compat_RAM.append(data["metadata"]["name"])
            compatByMType += 1
print("\n")
#print("Total compatible RAMs " + str(compatByMType))

compat_RAM.sort()

#for e in compat_RAM:
    #print(e)
print("Total compatible RAMs " + str(compatByMType))