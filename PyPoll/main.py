#import libraries and create necessary file paths
import os
import csv

poll_path = os.path.join("..", "python-challenge", "PyPoll", "Resources", "election_data.csv")


with open(poll_path, "r") as poll_file:
    csvreader = csv.reader(poll_file, delimiter = ",")
    header = next(csvreader)

    ## 1. Total votes cast
    def total_votes_cast(csvreader):
        count = 0
        for row in csvreader:
            count += 1
        return int(count)
    

    ## 2. Find complete list of candidates
    def find_list_candidates(csvreader):
        candidates = [row[2] for row in csvreader]
        unique_candidates = list(set(candidates))
        return unique_candidates
    
    ## 3. Percentage of votes each candidate won
    ## 4. Total number of votes each candidate won
    def candidate_polls(csvreader, unique_candidates):
        cand1_count = 0.0
        cand2_count = 0.0
        cand3_count = 0.0
        for row in csvreader:
            if row[2] == unique_candidates[0]:
                cand1_count += 1
            elif row[2] == unique_candidates[1]:
                cand2_count += 1
            elif row[2] == unique_candidates[2]:
                cand3_count += 1
        return [cand1_count, cand2_count, cand3_count]
    
    def candidate_percentage(cand_count_list):
        cand1_pct = (cand_count_list[0] / total_votes) * 100
        cand2_pct = (cand_count_list[1] / total_votes) * 100
        cand3_pct = (cand_count_list[2] / total_votes) * 100
        return [cand1_pct, cand2_pct, cand3_pct]

    ## 5. Winner of the Election based on popular vote
    def candidate_dictionary(unique_candidates, cand_count_list, cand_pct_list):
        candidate_info = {unique_candidates[i]:[int(cand_count_list[i]), round(cand_pct_list[i], 3)] for i in range(3)}
        return candidate_info
    
    def winner_info(input_dictionary, cand_count_list):
        for i in range(1, len(cand_count_list)):
            if cand_count_list[i] > cand_count_list[i-1]:
                winner_index = i
        winner, values = list(input_dictionary.items())[winner_index]
        return winner
 
    #Results
    total_votes = total_votes_cast(csvreader)
    print(total_votes)
    poll_file.seek(0)
    next(csvreader)
    unique_candidates = find_list_candidates(csvreader)
    print(unique_candidates)
    poll_file.seek(0)
    next(csvreader)
    cand_count_list = candidate_polls(csvreader, unique_candidates)
    cand_pct_list = candidate_percentage(cand_count_list)
    poll_file.seek(0)
    next(csvreader)    
    candidate_info = candidate_dictionary(unique_candidates, cand_count_list, cand_pct_list)
    print(candidate_info[unique_candidates[0]], candidate_info[unique_candidates[1]], candidate_info[unique_candidates[2]])
    poll_file.seek(0)
    next(csvreader)
    winner = winner_info(candidate_info, cand_count_list)
    print(winner)
    poll_file.seek(0)
    next(csvreader)

    ## path to write txt file
    store_path = os.path.join("..", "python-challenge", "PyPoll", "analysis", "analysis.txt")

    with open(store_path, "w") as txtfile:
        outputs = ["Election Results", "---------------------------------------------------------------------",
                   f"Total Votes: {str(total_votes)}", "---------------------------------------------------------------------",
                   f"{unique_candidates[0]}: {str(cand_pct_list[0])}% ({str(cand_count_list[0])})", f"{unique_candidates[1]}: {str(cand_pct_list[1])}% ({str(cand_count_list[1])})",
                   f"{unique_candidates[2]}: {str(cand_pct_list[2])}% ({str(cand_count_list[2])})",
                   "---------------------------------------------------------------------", f"Winner: {winner}"]
        
        for text in outputs:
            txtfile.write(f"{text} \n")
