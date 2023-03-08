men = ["A", "B", "C", "D"]
women = ["W", "X", "Y", "Z"]

men_prefs = [["X", "W", "Y", "Z"],  # A's preferences
             ["X", "W", "Y", "Z"],  # B's preferences
             ["Y", "W", "Z", "X"],  # C's preferences
             ["X", "Z", "Y", "W"]]  # D's preferences

women_prefs = [["B", "A", "C", "D"],  # W's preferences
               ["C", "A", "D", "B"],  # X's preferences
               ["C", "B", "D", "A"],  # Y's preferences
               ["A", "C", "B", "D"]]  # Z's preferences


def gale_shapley():
    matches = [-1] * len(women)  # currently no matches, thus -1
    while -1 in matches:
        single_man = matches.index(-1)
        prefered_woman_name = men_prefs[single_man][0]  # current first choice
        prefered_woman = women.index(prefered_woman_name)  # the index
        men_prefs[single_man].pop(0)  # remove first choice

        if prefered_woman not in matches:  # preferred woman is single
            matches[single_man] = prefered_woman  # MAZAL TOV !!

        else:  # preferred woman is married
            current_match = matches.index(prefered_woman)
            # check if current match is worse than (=located after) single man
            if women_prefs[prefered_woman].index(men[current_match]) > \
                    women_prefs[prefered_woman].index(men[single_man]):
                matches[current_match] = -1  # first divorce
                matches[single_man] = prefered_woman  # then MAZAL TOV!!

    return matches


# The matching
matches = gale_shapley()
for i in range(len(matches)):
    print(men[i], "married", women[matches[i]])
