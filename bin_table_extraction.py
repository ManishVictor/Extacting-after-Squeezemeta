import pandas as pd
with open('All_bin_filtered','a') as file2:
    file2.write(('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n').format('Sample','Bin_ID','Method','Tax','Tax_16S','Length','GC_perc','Num_contigs','Disparity','Completeness','Contamination','Strain_het','Coverage_Sample1','TPM_Sample1'))
for i in range(1,3,1):
    for j in range(1,10,1):
        file_name = (('18.S{}R{}.bintable').format(j,i))
        with open(file_name,'r') as file1:
            bin_file = file1.readlines()
        for k in range(2,len(bin_file),1):
            split_each = (bin_file[k].split('\t'))
            #print(split_each)
            completeness = split_each[8]
            contamination = split_each[9]
            if((pd.to_numeric(completeness) > 50) and (pd.to_numeric(contamination) < 10)):
                with open('All_bin_filtered','a') as file2:
                    file2.write(('S{}R{}\t{}').format(j,i,bin_file[k]))