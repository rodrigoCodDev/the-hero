from pick import pick
from heroes import Hero, HeroData

if __name__ == "__main__":
    title = "THE HERO GAME -  v0.1.0"
    options = ['Start new game', 'Load', 'About', 'Exit']

    option, index = pick(options, title, indicator='>', default_index=0)

    if (index == 0) :
        title = "Select your character: "
        options = []
        hero_data = ""

        with open('heroes.json', 'r') as file:
            json_data = file.read()
            hero_data = HeroData(json_data)
            options = hero_data.get_hero_names()
            print(options)

        option, index = pick(options, title, indicator='>', default_index=0)
        
    