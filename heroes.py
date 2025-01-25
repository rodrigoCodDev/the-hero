import json

class Hero:
    def __init__(self, name, defense, attack, health, speed, response_time, power_time, experience):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.health = health
        self.speed = speed
        self.response_time = response_time
        self.power_time = power_time
        self.experience = experience

    def __repr__(self):
        return f"Hero(name={self.name}, defense={self.defense}, attack={self.attack}, health={self.health}, speed={self.speed}, response_time={self.response_time}, power_time={self.power_time}, experience={self.experience})"


class HeroData:
    def __init__(self, json_data):
        self.data = json.loads(json_data)
        self.heroes = [
            Hero(
                hero['name'],
                hero['attributes']['defense'],
                hero['attributes']['attack'],
                hero['attributes']['health'],
                hero['attributes']['speed'],
                hero['attributes']['response_time'],
                hero['attributes']['power_time'],
                hero['attributes']['experience']
            )
            for hero in self.data['heroes']
        ]

    def get_hero_names(self):
        return [hero.name for hero in self.heroes]

    def get_hero_attributes(self, hero_name):
        for hero in self.heroes:
            if hero.name == hero_name:
                return hero
        return None

    def get_all_heroes(self):
        return self.heroes