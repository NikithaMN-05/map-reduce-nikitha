import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 6) :
    location,date,variant,num_sequences,perc_sequences,num_sequences_total = datalist

    # print intermediate key-value pairs to standard output
    print(variant,"\t", 1)