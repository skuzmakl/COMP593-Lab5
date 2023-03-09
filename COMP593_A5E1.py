from poke_api import search_pokemon_entries
from pastebin_api import post_new_paste
import sys

def main():
    poke_name = get_pokemon_name()
    poke_info = search_pokemon_entries(poke_name)
    if poke_info:
        title, body_text = construct_poke_paste(poke_info)
        paste_url = post_new_paste(title, body_text, '1M', False)
        print(paste_url)

def get_pokemon_name():
    num_params = len(sys.argv) - 1
    if num_params > 0:
        return sys.argv[1]
    else:
        print('Error: Missing search term')
        sys.exit(1)

def construct_poke_paste(poke_info):
    title = f"{poke_info['name'].capitalize()}'s Abilities"
    #print(title)

    ability_info = poke_info['abilities']
    pokemon_abilities = ["- " + ability['ability']['name'] for ability in ability_info]
    body_text = '\n'.join(pokemon_abilities)
    #print(body_text)

    return title, body_text

if __name__ == "__main__":
    main()