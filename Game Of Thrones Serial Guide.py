import webbrowser

link = 'http://hdrezka-ag.com/series/fantasy/45-igra-prestolov-2011-tv-series-1.html#t:65-s:season-e:episode'
print("Hey! I can help you to navigate to the 'Game of Thrones' any season and episode!")
season = (input("First type the number of the season you want to watch: "))
episode = (input("Now type the number of the episode you want to see: "))
choice = [season, episode]
if choice[0] > '8':
    print("Incorrect value. GoT has only 8 seasons! Try again.", )
    exit(0)
elif choice[0] == '7' and choice[1] > '7':
    print("Incorrect value. Season 7 has 7 episodes. Try again.")
    exit(0)
elif choice[0] == '8' and choice[1] > '4':
    print("Incorrect value. Season 8 has 6 episodes and there are only 4 of them have been released. Try again!")
    exit(0)
elif choice[0] or choice[1] == "":
    print("Please type a number")
    exit(0)
print("Enjoy:)")
readyLink = link.replace('season', season).replace('episode', episode)
webbrowser.open(readyLink)
