# Add our dependencies.
import csv
import os

# Assign a variable for the open path
election_file = os.path.join( "Resources/election_data.csv")

# initialize a aggregate(agg) vote counter.
agg_votes = 0

# initiate Candidate(cand) alternatives
cand_list = []

cand_votes = {}

# Winning Cand and count tracker
win_cand = ""
win_count = 0

with open(election_file) as election_data:

    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # add to total votes
        agg_votes += 1

    # collect candidate name from each row.
        cand_name = row[2]

        if cand_name not in cand_list:
            # add candidate name to candidate list.
            cand_list.append(cand_name)

            cand_votes[cand_name] = 0

        cand_votes[cand_name] += 1

# Assign a variable for the save path.
election_analysed = os.path.join("Analysis/analysis_pypoll.txt")

# save the result to a text file
with open(election_analysed, "w") as election_txt:

    result = (f"````` text"
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {agg_votes:,}\n"
        f"-------------------------\n")
    print(result)
   
    election_txt.write(result)       

    for cand_name in cand_votes:
        votes = cand_votes[cand_name]
        # calculate the percentage of votes
        percent_vote = int(votes) / int(agg_votes) * 100

        cand_result = (f"{cand_name}: {percent_vote:.1f}% ({votes:,})\n")
        print(cand_result)
       
        election_txt.write(cand_result)

        # Determine winning candidate
        if (votes > win_count):
            # if true, make win_count = votes
            win_count = votes
            # make the win_cand to the cand's name
            win_cand = cand_name

    summary = (f"-------------------------\n"
        f"Winner: {win_cand}\n"
        f"-------------------------\n"
        f"```````")
    print(summary)
    # save result summary to the text file.
    election_txt.write(summary)