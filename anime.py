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



