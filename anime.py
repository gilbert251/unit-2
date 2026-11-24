import json

with open("anime.json", "r", encoding="utf-8") as f:
    data = json.load(f)

anime_list = data["data"]   # a list of 25 anime (each one is a dictionary)



# ------------------------------------------------------------
# Q1. Filtering and counting
# Print the title and score of every anime with a score
# greater than 9.0. Then print how many there were.
# ------------------------------------------------------------
def scores(anime_list):
    print("all anime with a scores of 9+")
    high_score_amount=0
    for i in anime_list:
        try:
            if i["score"]>=9:
                print(i["title"])
                high_score_amount+=1

        except KeyError:
            continue

    print(f"total:{high_score_amount}")

# ------------------------------------------------------------
# Q2. Accumulator
# Calculate and print the average score of all the anime
# in the list. Round the answer to 2 decimal places.
# ------------------------------------------------------------




# ------------------------------------------------------------
# Q3. Finding the maximum
# Print the title and episode count of the anime that has the
# most episodes.
# Hint: look closely at the "episodes" values. Does every
# anime have a number?
# ------------------------------------------------------------




# ------------------------------------------------------------
# Q4. Nested lists
# Each anime has a "genres" list. Each item in that list is a
# dictionary with a "name" key (for example, "Comedy").
# Print the title of every anime that has the genre "Comedy".
# ------------------------------------------------------------






