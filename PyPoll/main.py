import pandas as pd
data_file = "Resources/election_data.csv"
data_file_df = pd.read_csv(data_file)
#data_file_df.head()

totalvote = data_file_df["Voter ID"].count()
#print(data_file_df.Candidate == 'Khan')

Khan = data_file_df[data_file_df.Candidate == 'Khan']
Khancount = Khan["Voter ID"].count()
Khanpct = '{:.3%}'.format(Khancount/totalvote)
#print(Khancount)
#print(Khanpct)

Correy = data_file_df[data_file_df.Candidate == 'Correy']
Correycount = Correy["Voter ID"].count()
Correypct = '{:.3%}'.format(Correycount/totalvote)
#print(Correycount)
#print(Correypct)

Li = data_file_df[data_file_df.Candidate == 'Li']
Licount = Li["Voter ID"].count()
Lipct = '{:.3%}'.format(Licount/totalvote)
#print(Licount)
#print(Lipct)

Tooley = data_file_df[data_file_df.Candidate == "O'Tooley"]
Tooleycount = Tooley["Voter ID"].count()
Tooleypct = '{:.3%}'.format(Tooleycount/totalvote)
#print(Tooleycount)
#print(Tooleypct)

for x in Khancount, Correycount, Licount, Tooleycount:
    if x > Correycount and x > Licount and x > Tooleycount:
        y = Khan["Candidate"][0]
        #print(f'Winner: {y}')
    elif x > Khancount and x > Licount and x > Tooleycount:
        y = Correy["Candidate"][0]
        #print(f'Winner: {y}')
    elif x > Khancount and x > Correycount and x > Tooleycount:
        y = Li["Candidate"][0]
        #print(f'Winner: {y}')
    elif x > Khancount and x > Licount and x > Correycount:
        y = Tooley["Candidate"][0]
        #print(f'Winner: {y}')
        
print('Election Results')
print('-------------------------')
print(f'Total Votes: {totalvote}')
print('-------------------------')
print(f'Khan: {Khanpct} ({Khancount})',f'Correy: {Correypct} ({Correycount})', f'Li: {Lipct} ({Licount})', f"O'Tooley: {Tooleypct} ({Tooleycount})", sep="\n")
print('-------------------------')
print(f'Winner: {y}')
print('-------------------------')