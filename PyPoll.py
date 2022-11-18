# The data we need to retrieve
import csv

import os

# Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path

file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter

total_votes = 0

# Candiate Options
candidate_options = []

# Candidate dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

# Read the file objet with the reader function
    file_reader = csv.reader(election_data)

# Read the header row
    headers = next(file_reader)

# Print each row in the CSV file. 
    for row in file_reader:

    # add to the total vote count 
        total_votes += 1
    
    # print the candidate name from each row
        candidate_name = row[2]

    # if the candidate does not match any existing candidate...    
        if candidate_name not in candidate_options:
    # add the candidate name to the candidate list
            candidate_options.append(candidate_name)
    # begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0
    # Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1


# Save the results to our text file
with open(file_to_save, "w") as txt_file:
   
    election_results =(
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

 # Save the final vote count to the text file
    txt_file.write(election_results)

     # 3. Print the total votes. 
    #print(total_votes)


    # 2. A complete list of candidates who received votes
    #print(candidate_options)
    # 3. The percentage of votes each candidate won

    # to do: print out each candidate's name, vote count, and percentage of votes to the terminal 
    # Iterate through the candidate list. 
    for candidate_name in candidate_votes:
        #retrive cote count of a candidate
        votes = candidate_votes[candidate_name]
        # calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # print the candidate name and percentage of votes. 
    # print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n") 
           #print each candidate, their voter count, and percentage to the termial 
        candidate_results = (f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

        print(candidate_results)
# Save the candidate results to our txt file 
        txt_file.write(candidate_results)        



        # Determing winning vote count and candidate
        # determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            # if true then set winning_count = votes and winning_percent = vote percentage 
            winning_count =  votes

            winning_percentage = vote_percentage

            # set the winning_candidate equal to the candidate's name. 
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"---------------------------------\n")

    

    #print(f"Total Votes Recieved: {total_votes}")    
    print(winning_candidate_summary)
        
    # 4. The total number of votes each cadidate won

    # 5. The Winner of the Election based on popular vote
    # Save the Winning candidate's results to the txt file
    txt_file.write(winning_candidate_summary)
    

