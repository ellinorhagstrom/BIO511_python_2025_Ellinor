#3.0
mylist = ["a", "list", "can", "contain", "strings", "and", "numbers", 2]
print(type(mylist)) 

print(mylist)
print("\n",mylist[0])

#3.1
mylist7 = ["one","two","three","four","five","six","seven"]

loop_number=1
for item in mylist7:
    if loop_number > 5:
        break #Istället för exit, pga exit stoppar hela scriptet, men break går bara ur loopen
    else:
        print(item, loop_number)
        loop_number+=1

#3.2
sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
codons = ['CCA', 'TGT', 'GTA', 'TAG']


#Går igenom sekvens för sekvens, alltså kollar om något av kodonen finns i sekvens 1, sedan vidare med alla kodon i sekvens 2 etc.
for sequence in sequences: #Titta på varje sekvens (item) i listan sequences
    for codon in codons: #Titta sedan på varje kodon (item) i listan codons
        if codon in sequence: #Om kodon finns i sekvensen --> print
            print(codon + " is in:" + sequence)
         
#3.2.1
start_codon = "ATG"
stop_codon = ["TAA", "TAG","TGA"]

print("\n")

both_codons = [] # Skapar en tom lista som jag kan appenda senare

for sequence in sequences:
    has_start = False #Måste sätta till false i början, ¨annars fortsätter variablerna vara true för nästa sekvens om de någon gång varit true i tidigare sekvens.
    has_stop = False

    if start_codon in sequence:
        print(f"start codon: {start_codon} is in {sequence} ")
        has_start = True
    
    for stop in stop_codon:
        if stop in sequence:
            print(f"stop codon: {stop} is in {sequence} ")
            has_stop = True
    
    if (has_start and has_stop) == True:
        print(f"Both start and stop codon is present in {sequence}")
        both_codons.append(sequence)

print(f"\nSequences with both start and stop codons {both_codons}\n")

#3.2.2.1
for item in both_codons:
    start_index = item.find(start_codon)

    for stop in stop_codon:
        stop_index = item.find(stop)
        
        if stop_index != -1: #Om stopcodon inte är lika med -1 (alltså att codonet inte finns i sekvensen)
            if start_index < stop_index:
                print(f"Start codon {start_codon, start_index} comes before stop codon {stop, stop_index} in sequence: {item}")

            else:
                print(f"Start codon {start_codon, start_index} comes AFTER stop codon {stop, stop_index} in sequence: {item}")

#3.2.2
data = dict({'pat_001': ['bacZZt98', 'bac889Ytd'], 'pat_002': ['bac0GFrr'], 'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']})

for key_pat, value_bact in data.items():
    print(f"\n{key_pat}: {value_bact}")
    
    if "bac889Ytd" in value_bact:
        print(True)
    else:
        print(False)

#3.2.3
unique_bacteria_list = []

for key_pat, value_bact in data.items():
    for item in value_bact:
        if item not in unique_bacteria_list:
            unique_bacteria_list.append(item)
print(unique_bacteria_list, "\n")

#3.2.4
unique_bacteria_dict = {}

for key_pat, value_bact in data.items():
    for item in value_bact:
        if item not in unique_bacteria_dict:
            unique_bacteria_dict[item] = []

print(unique_bacteria_dict, "\n")

#3.2.5
unique_bacteria_dict = {}

for key_pat, value_bact in data.items():
    for item in value_bact:
        if item not in unique_bacteria_dict:
            unique_bacteria_dict[item] = []
        
        unique_bacteria_dict[item].append(key_pat)            

print(unique_bacteria_dict)

           



