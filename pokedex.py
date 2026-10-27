import json
## Open the JSON file of pokemon data
try:
    with open("./moves.json", encoding="utf8") as f:
        moves_data = json.load(f)
except FileNotFoundError:
    moves_data = []
    print("Warning: 'moves.json' not found. Move features will be limited.")
## create variable "data" that represents the enitre pokedex list
with open('pokedex.json', 'r', encoding='utf-8') as pokedex_file:
    data = json.load(pokedex_file)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
# Add a language choice feature and print the pokemons name based on the user input
def print_pokemon_names(data, language="english"):
    for pokemon in data:
        name_info = pokemon.get("name")
        if isinstance(name_info, dict):
            print(name_info.get(language.lower(), name_info.get("english")))
        else:
            print(name_info)
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
def get_pokemon_by_type(data, search_type):
    matching_pokemon = []
    for pokemon in data:
        # Check if the search type matches any type in the Pokémon's type list
        types = [t.lower() for t in pokemon.get("type", [])]
        if search_type.lower() in types:
            matching_pokemon.append(pokemon)

    if not matching_pokemon:
        print(f"No Pokémon found with the type '{search_type}'.")
    
    return matching_pokemon
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
def search_pokemon_by_name(data, query):
    matching_pokemon = []
    for pokemon in data:
        # Get the English name (or string name depending on your JSON structure)
        name_info = pokemon.get("name")
        english_name = name_info.get("english", "") if isinstance(name_info, dict) else name_info
        
        if query.lower() in english_name.lower():
            matching_pokemon.append(english_name)

    if not matching_pokemon:
        print(f"No Pokémon found matching '{query}'.")
    
    return matching_pokemon

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
def show_moves_for_pokemon(pokemon_name, data, moves):
    # Find the specific Pokémon
    target_pokemon = None
    for pokemon in data:
        name_info = pokemon.get("name")
        english_name = name_info.get("english", "") if isinstance(name_info, dict) else name_info
        if english_name.lower() == pokemon_name.lower():
            target_pokemon = pokemon
            break

    if not target_pokemon:
        print(f"Pokémon '{pokemon_name}' not found.")
        return

    poke_types = [t.lower() for t in target_pokemon.get("type", [])]
    print(f"\n--- Moves for {target_pokemon['name']['english']} (Type: {', '.join(poke_types)}) ---")

    found_moves = False
    for move in moves:
        move_type = str(move.get("type", "")).lower()
        if move_type in poke_types:
            # 1. Look for common naming keys safely
            move_name_data = move.get("name") or move.get("ename") or move.get("move")
            
            # 2. Check if the name data exists and is a dictionary
            if isinstance(move_name_data, dict):
                move_name = move_name_data.get(lang.lower(), move_name_data.get("english", "Unknown"))
            elif move_name_data is not None:
                move_name = move_name_data
            else:
                move_name = "Unknown Move Name" # Fallback if no keys matched
                
            print(f"- {move_name} ({move.get('type')})")
            found_moves = True

    if not found_moves:
        print("No matching moves found in moves.json for these types.")

print("welcome to pokedex! type 1 to print pokemon names,type 2 to print all pokemon a single type, type 3 to search by a fragment of a pokemons name, type 4 to show the moves a pokemon can leane based on it's name")
lang = input("Enter language (english, japanese, chinese, french): ").strip()
if not lang:
    lang = "english"
choice = int(input("Enter your choice: "))

if choice == 1:
    print_pokemon_names(data, lang)

elif choice == 2:
    search_type = input("Enter the Pokémon type (e.g., Fire, Water, Grass): ").strip()
    results = get_pokemon_by_type(data, search_type)
    for p in results:
        name_info = p.get("name")
        if isinstance(name_info, dict):
            print(name_info.get(lang.lower(), name_info.get("english")))
        else:
            print(name_info)

elif choice == 3:
    query = input("Enter name fragment to search (e.g., Char): ").strip()
    matches = search_pokemon_by_name(data, query)
    for name in matches:
        print(name)

elif choice == 4:
    poke_name = input("Enter the full English name of a Pokémon: ").strip()
    show_moves_for_pokemon(poke_name, data, moves_data)
