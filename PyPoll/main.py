import csv
import os

csv_path = os.path.join("Resources", "election_data.csv")
txt_export = os.path.join("Analysis","election_analysis.txt")

total_votes = 0
candidates = {}
candidate_percent = {}
winner = ""
winner_count = 0

#Read CSV and calculate total votes and votes per candidate
with open(csv_path) as info:
    reader = csv.reader(info)

    header = next(reader)

    for row in reader:
        total_votes += 1
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
    #Find the winner
    winner = max(candidates, key=candidates.get)
    winner_count = candidates[winner] 

    


#Generate Output Summary
output = (
    f"Election Results\n"
    f"-----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------------------\n"
)
for candidate, votes in candidates.items():
    candidate_percent = round((votes/total_votes)*100,3)
    output += f"{candidate}: {candidate_percent}% ({votes})\n"
output += (
    f"-----------------------------\n"
    f"Winner: {winner}\n"
    f"-----------------------------\n"
)
 
print(output)
with open(txt_export, "w") as txt_file:
    txt_file.write(output)