from pick import pick

if __name__ == "__main__":
    title = "THE HERO GAME - v0.1.0"
    options = ['Start new game', 'Load', 'About', 'Exit']

    option, index = pick(options, title, indicator='>', default_index=0)
