from currentsapi import CurrentsAPI
from colorama import Fore

'''
-=-=--=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-MazZ's News Hub-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
This program uses the 'currents' API which keeps track of current/old News articles from a list of over 42,000 
news outlets. Including but not limited to: FOX, CNN, ABC, NBC, MSNBC, NPR, AP, CNBC, FT, BuzzFeed, Washington Post, 
NY Times, BBC, SCMP, ADN, CDN, WWLP, TheRegister, SMH, WBBJTV, TMZ, WSVN, WNBC, WSWS, EWN, and MANY, MANY MORE!

You can see all the latest articles that have been published, from these various News agencies, in realtime. Or search 
for something specific using keyword(s)/phrases. 

Rather than search through 500 different news outlets, the user can simply use this hub to search through all of them
within a minute.

For API key you can go to: 
https://currentsapi.services/en
- Register account (Free)
- You'll be given a free API key which allows for up to 600 requests per day.
    - If not self-evident >> Replace API_KEY with your own >> Run Program >> VOILA!

Note:
If you're running this in a Win32 tty session, the colors may mess with the output since the tty itself does not seem to
read the ANSI chars from the color lib 'colorama >>> Fore'. I'll have a fix for this in the future.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''

API_KEY = 'YOUR API KEY GOES HERE'

api = CurrentsAPI(api_key=API_KEY)


def current_news():
    # Searches for most recently added News articles that have been published.
    latest = api.latest_news()
    current_list = []
    results = []
    a_count = 0

    print(Fore.BLUE + "Latest News:" + Fore.RESET)

    # Grabs key values
    for i in latest.values():
        current_list.append(i)

    # Adds values of 'news:' key
    for i in current_list[1]:
        results.append(i)

    # Creates list of 'news' key values cleaned for output
    for i in results:
        cleaned = list(i.values())

        news_id = cleaned[0]
        title = cleaned[1]
        description = cleaned[2]
        url = cleaned[3]
        author = cleaned[4]
        img = cleaned[5]
        lang = cleaned[6]
        category = cleaned[7]
        published = cleaned[8]
        a_count += 1

        print(Fore.MAGENTA + f"Article #{a_count}" + Fore.RESET)
        print(Fore.LIGHTYELLOW_EX + f"ID:\n{Fore.RESET}{news_id}")
        print(Fore.LIGHTYELLOW_EX + f"Title:\n{Fore.LIGHTRED_EX}{title}")
        print(Fore.LIGHTYELLOW_EX + f"Description:\n{Fore.WHITE}{description}{Fore.RESET}".replace('. ', '.\n'))
        print(Fore.LIGHTYELLOW_EX + f"URL:\n{Fore.LIGHTBLUE_EX}{url}{Fore.RESET}")
        print(Fore.LIGHTYELLOW_EX + f"Author:\n{Fore.LIGHTMAGENTA_EX}{author}")
        print(Fore.LIGHTYELLOW_EX + f"Link to Image:\n{Fore.LIGHTBLUE_EX}{img}{Fore.RESET}")
        print(Fore.LIGHTYELLOW_EX + f"Language:\n{Fore.WHITE}{lang}{Fore.RESET}")
        print(Fore.LIGHTYELLOW_EX + f"Category:\n{Fore.WHITE}{category}{Fore.RESET}")
        print(Fore.LIGHTYELLOW_EX + "Published Date:\n" + Fore.WHITE + published + Fore.RESET + "\n")


def search_news(keyword=None):
    # Searches for News articles related to keyword/phrase.
    searches = api.search(keywords=str(keyword))

    # Stores the Data to be cleaned
    news_list = []
    results = []
    a_count = 0

    print(Fore.BLUE + f"Search Results:" + Fore.RESET)

    # Iterates through 'searches' dict, and grabs the key values.
    for i in searches.values():
        news_list.append(i)

    # Adds data from each key value to it's own list.
    for i in news_list[1]:
        results.append(i)

    # Outputs the Data
    for i in results:
        cleaned = list(i.values())

        news_id = cleaned[0]
        title = cleaned[1]
        description = cleaned[2]
        url = cleaned[3]
        author = cleaned[4]
        img = cleaned[5]
        lang = cleaned[6]
        category = cleaned[7]
        published = cleaned[8]
        a_count += 1

        print(Fore.MAGENTA + f"Article #{a_count}" + Fore.RESET)
        print(Fore.LIGHTYELLOW_EX + f"ID:\n{Fore.RESET}{news_id}")
        print(Fore.LIGHTYELLOW_EX + f"Title:\n{Fore.LIGHTRED_EX}{title}")
        print(Fore.LIGHTYELLOW_EX + f"Description:\n{Fore.WHITE}{description}{Fore.RESET}".replace('. ', '.\n'))
        print(Fore.LIGHTYELLOW_EX + f"URL:\n{Fore.LIGHTBLUE_EX}{url}{Fore.RESET}")
        print(Fore.LIGHTYELLOW_EX + f"Author:\n{Fore.LIGHTMAGENTA_EX}{author}")
        print(Fore.LIGHTYELLOW_EX + f"Link to Image:\n{Fore.LIGHTBLUE_EX}{img}{Fore.RESET}")
        print(Fore.LIGHTYELLOW_EX + f"Language:\n{Fore.WHITE}{lang}{Fore.RESET}")
        print(Fore.LIGHTYELLOW_EX + f"Category:\n{Fore.WHITE}{category}{Fore.RESET}")
        print(Fore.LIGHTYELLOW_EX + "Published Date:\n" + Fore.WHITE + published + Fore.RESET + "\n")


def main():
    run = False
    while not run:
        choice = input(Fore.GREEN + "~*~*~*~*~*~*~Welcome to MazZ\'s News Media Hub!~*~*~*~*~*~*~*~\n" +
                       Fore.MAGENTA + "Please Choose an Option:\n " +
                       Fore.BLUE + "[1] Search for Specific Topic\n "
                                   "[2] Return Most Recently Published Articles\n" +
                       Fore.MAGENTA + "Choice: " + Fore.RESET).lower()

        if choice == str(int(1)):
            search = input(Fore.BLUE + "Type Keyword or name of Article to search for: " + Fore.RESET).lower()
            print(Fore.GREEN + "Searching..." + Fore.RESET)

            search_news(keyword=search)

            cont = input(Fore.BLUE + "Would you like to search for something else? [Y/N]: " + Fore.RESET).lower()

            if cont == 'y':
                continue
            else:
                quit()

        elif choice == str(int(2)):
            print(Fore.GREEN + 'Searching...' + Fore.RESET)
            current_news()

            cont2 = input(Fore.MAGENTA + "Please Choose an Option:\n" + Fore.BLUE +
                          " [1] Search for Specific Article, Keyword(s), or Phrase.\n"
                          " [2] Refresh Current\n"
                          " [3] Quit\n" + Fore.MAGENTA +
                          "Choice: " + Fore.RESET).lower()

            if cont2 == str(int(1)):
                phrase = input(Fore.BLUE + "What News Topic would you like to search for?: " + Fore.RESET).lower()
                search_news(keyword=phrase)

            elif cont2 == str(int(2)):
                current_news()

            elif cont2 == str(int(3)):
                quit()

        else:
            print(Fore.RED + "Please choose an option..." + Fore.RESET)


if __name__ == '__main__':
    main()
