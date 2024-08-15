survey_result =  [
    [ "Python", "JavaScript", "C++"], #Participant 1
    ["Python", "JavaScript", "C#"],  #Participant 2
    ["Python", "Java"],  #Participant 3
    ["Python", "C++", "JavaScript"], #Participant 4
    ["Python", "JavaScript", "C++", "Java"]  #Participant 5
]
choices_sets = [set(Participant) for Participant in survey_result ]
print(choices_sets)
# 1. identify the languaged that were chosen by all participants
common_languages = set.intersection(*choices_sets)
print("Languages chosen by all Participant", common_languages)

# 2. Find the languages that were only were only chosen by a single participants
All_languages = choices_sets[1]
chosen_by_a_single_participants = choices_sets[-1]
Languages_chosen_by_only_one_participant= list(All_languages  - chosen_by_a_single_participants)
print("Languages chosen by only one participant:", Languages_chosen_by_only_one_participant)


