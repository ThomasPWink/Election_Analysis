# Election_Analysis
## Overivew of Election Audit
The purpose of this election audit analysis was to automate the election process and provide clear results to the election commission.  The results to be provide were total votes, total votes per county, total percentage per county, total votes per candidate, total vote percentage by candidate, winner of the election, and county with the most votes received.  This was all to be provided in a text file written by code to minimize error by doing a manual count.

## Election-Audit Results
* Total votes in this congressional election were 369,711
Code below shows how each line was counted after the header line.  each line on the data sheet was equal to one vote
``` 
 # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
```
* Votes per County:
  * Jefferson: 10.5%  38,855 votes
  * Denver: 82.8%  306,055 votes
  * Arapahoe: 6.7%   24,801 votes
* Denver county had the largest number of votes
* Votes per Candidate:
  * Charles Casper Stockham: 23.0% 85,213 votes
  * Diana Degette: 73.8% 272,892 votes
  * Raymon Anthony Doane: 3.1% 11,606 votes

Code below shows how each candidate and county were pulled from the data sheet.  After each vote was counted for either the candidate or county and added to a total for each one everytime that county or candidate was found on a line.  
```
 # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)
            

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```
* Diana Degette won the election with 272,892 votes which was 73.8% of the total votes. 

## Election-Audit Summary
This election project was a success.  This code can be used for any election with some modifications.  If this election had multiple different offices being contested, then we can very easily create new variables and use the same code to calculate the totals for those also.  Say we have a Senate race and Governor race in the same election.  We can add the code below.  This code can also be used to tabulate the results of a measure being voted on.  If the ballot were to have a measure about funding a school or a tax increase the code can be used to calculate the yes and no votes.  
```
senate_candidate_options = []
senate_candidate_votes = {}
governor_candidate_options = []
governor_candidate_votes = {} 
# Get the candidate name from each row.
       senate_candidate_name = row[2]
       governor_candidate_name = row[3]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if senate_candidate_name not in senate_candidate_options:

            # Add the candidate name to the candidate list.
            senate_candidate_options.append(senatecandidate_name)

            # And begin tracking that candidate's voter count.
            Senate_candidate_votes[senate_candidate_name] = 0

        # Add a vote to that candidate's count
        Senate_candidate_votes[senate_candidate_name] += 1

        if governor_candidate_name not in governor_candidate_options:

            # Add the candidate name to the candidate list.
            governor_candidate_options.append(governor_candidate_name)

            # And begin tracking that candidate's voter count.
            governor_candidate_votes[governor_candidate_name] = 0

        # Add a vote to that candidate's count
        governor_candidate_votes[governor_candidate_name] += 1
```
