import pandas as pd
import regex as re


data = pd.read_csv(r"C:\Sem_4_July_2022\IFN712_Research_In_IT_Practice\mouse-chromosome-19-sample-guides.txt")
print(data.columns)
# print(data)
data = data.drop(['sgrnascorer2score', 'seqCount', 'passedG20', 'passedTTTT', 'passedATPercent',
       'passedSecondaryStructure', 'ssL1', 'ssStructure', 'ssEnergy',
       'acceptedByMm10db', 'acceptedBySgRnaScorer','passedBowtie', 'passedOffTargetScore', 'AT', 'bowtieChr','passedAvoidLeadingT'], axis=1)
print(data.columns)

# bowtie start and end
data['bowtieStart'] = data['bowtieStart'].replace('?',None)
data['bowtieStart'] = data['bowtieStart'].astype(float)
print(type(data.bowtieStart[1]))

data['bowtieEnd'] = data['bowtieEnd'].replace('?',None)
data['bowtieEnd'] = data['bowtieEnd'].astype(float)
print(type(data.bowtieEnd[1]))

# guide start and end
data.drop(data[data['start'] == '-'].index, inplace = True)
data['start'] = data['start'].astype(int)
print(type(data.start[1]))
data['end'] = data['end'].astype(int)
print(type(data.end[1]))

# offtarget score
data['offtargetscore'] = data['offtargetscore'].replace('?',None)
data['offtargetscore'] = data['offtargetscore'].astype(float)
print(type(data.offtargetscore[1]))
print(data.seq[0:2])

header = re.split("-",data.header[0])
header=int(header[2][3:])

col_1_chr = [header]*len(data.header)
col_2_start = list(data.start)
col_3_end = list(data.end)
col_4_seq = list(data.seq)
col_5_score = list(data.consensusCount)
col_6_strand = list(data.strand)
col_7 = col_2_start
col_8 = col_3_end
col_9_colour = []
offT = list(data.offtargetscore)
bow_start = list(data.bowtieStart)
print(bow_start[1])
print(pd.isna(bow_start[1]))

for i in range(len(offT)):

       if pd.isna(bow_start[i]):
              col_9_colour.append('0,0,255')
       else:
              if pd.isna(offT[i]):
                     col_9_colour.append('119,136,153')
              elif offT[i] > 90:
                     col_9_colour.append('0,128,0')
              elif offT[i] > 80 and offT[i] <= 90:
                     col_9_colour.append('144,238,144')
              elif offT[i] > 70 and offT[i] <= 80:
                     col_9_colour.append('255,255,0')
              elif offT[i] > 60 and offT[i] <= 70:
                     col_9_colour.append('240,230,140')
              elif offT[i] > 50 and offT[i] <= 60:
                     col_9_colour.append('255,165,0')
              elif offT[i] > 40 and offT[i] <= 50:
                     col_9_colour.append('255,69,0')
              elif offT[i] > 30 and offT[i] <= 40:
                     col_9_colour.append('255,0,0')
              elif offT[i] > 20 and offT[i] <= 0:
                     col_9_colour.append('139,0,0')
              else:
                     col_9_colour.append('128,0,0')





dict = {'chr': col_1_chr, 'start': col_2_start, 'end': col_3_end, 'seq': col_4_seq, 'Score': col_5_score, 'Strand': col_6_strand, 'col_7':col_7,'col_8':col_8, 'Colour':col_9_colour }
df = pd.DataFrame(dict)
line = 'track name="CRISPR Target" description="Efficiency and specificity scores" visibility=2 itemRgb="On"'
with open("C:\Sem_4_July_2022\IFN712_Research_In_IT_Practice\Crispr_target.bed.txt", 'w') as f:
       f.write(line)
       f.write('\n')
       dataAsString = df.to_string(header=False, index=False)
       f.write(dataAsString)




