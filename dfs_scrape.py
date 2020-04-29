import json, time, random
from selenium import webdriver
from bs4 import BeautifulSoup

pro_users=['youdacao', 'ChipotleAddict','Awesemo', 'papagates' 'moklovin', 'kingfi', 'chess_is_ok', 'ThatStunna',
'bric75', 'rikkidee', 'wakeywakey', 'jayk123x', 'TeeJayOrTj', 'ARaven52', 'gosixersgo76', 'I_Slewfoot_U',
'shocae', 'giantsquid', 'LuckyPapa', 'nolesman' 'csuram88', 'PetrGibbons', 'NILKNARF', 'petteytheft89',
'hoop2410', '3rd_and_schlong', 'BDholla89', 'aejones', 'squirrelpatroldk', 'BrandonAdams']

core_file='C:/Users/travi/Box Sync/NFL/DFS Research/'
date='9_25_2019'
url_core='https://www.fantasylabs.com/api/contestlist/1/4/'
username_url_core='https://www.fantasylabs.com/api/contests/usernames/1/'
lineups_url_core='https://www.fantasylabs.com/api/contests/lineups/1/'
contest_url_final=url_core+date+"/"

player_url_core='https://www.fantasylabs.com/api/contestplayers/1/'
leader_url_core='https://www.fantasylabs.com/api/contestleaderboard/1/'

browser = webdriver.Chrome()
browser.get(contest_url_final)
contest_soup = browser.page_source

# file=open('C:/Users/tburger101/Box Sync/NFL/DFS Research/Contests.txt')
# contest_soup=file.read()
contest_soup=BeautifulSoup(str(contest_soup))
all_contests=contest_soup.find("body")
print(all_contests.text)
contests=json.loads(all_contests.text)

contest_file_name= core_file+date+"_"+"contest.txt"
with open(contest_file_name, 'w') as file:
    file.write(json.dumps(contests))

for contest in contests:
    contest_id=contest.get('ContestId')
    username_url_final=username_url_core+str(contest_id)+"/"
    # file = open('C:/Users/tburger101/Box Sync/NFL/DFS Research/Users.txt')
    # username_soup = file.read()

#all users in the contest
    browser.get(username_url_final)
    username_soup = browser.page_source
    username_soup = BeautifulSoup(str(username_soup))
    all_users=username_soup.find("body")
    users = json.loads(all_users.text)
    user_file_name = core_file+str(contest_id) + "_" + "users.txt"
    with open(user_file_name, 'w') as file:
        file.write(json.dumps(users))
    time.sleep(random.randint(0,29))

#all eligible NFL players
    player_url_final=player_url_core+str(contest_id)
    browser.get(player_url_final)
    player_soup = browser.page_source
    player_soup = BeautifulSoup(str(player_soup))
    all_players = player_soup.find("body")
    players = json.loads(all_players.text)
    player_file_name = core_file + str(contest_id) + "_" + "players.txt"
    with open(player_file_name, 'w') as file:
        file.write(json.dumps(players))
    time.sleep(random.randint(0, 29))

 # Leaderboard of users
    leader_url_core = leader_url_core + str(contest_id)
    browser.get(leader_url_core)
    leader_soup = browser.page_source
    leader_soup = BeautifulSoup(str(leader_soup))
    all_leaders = leader_soup.find("body")
    leaders = json.loads(all_leaders.text)
    leader_file_name = core_file + str(contest_id) + "_" + "leaders.txt"
    with open(leader_file_name, 'w') as file:
        file.write(json.dumps(leaders))
    time.sleep(random.randint(0, 29))


    for user in users:
        user_id=user.get('OwnerId')
        user_name=user.get('Username')
        if user_name in pro_users:
            lineups_url_final=lineups_url_core+str(contest_id)+"/"+str(user_id)+"/"+"1/"
            lineups_users_url_final=lineups_url_core+str(contest_id)+"/"+str(user_id)+"/"+"0/"

            browser.get(lineups_url_final)
            lineups_soup = browser.page_source

            # file = open('C:/Users/tburger101/Box Sync/NFL/DFS Research/Lineups.txt')
            # lineups_soup = file.read()
            lineups_soup=BeautifulSoup(str(lineups_soup))
            all_lineups=lineups_soup.find("body")
            lineups = json.loads(all_lineups.text)

            browser.get(lineups_users_url_final)
            lineups_user_soup = browser.page_source

            # file = open('C:/Users/tburger101/Box Sync/NFL/DFS Research/Lineups_1.txt')
            # lineups_user_soup = file.read()
            lineups_user_soup = BeautifulSoup(str(lineups_user_soup))
            all_lineups_user=lineups_user_soup.find("body")
            lineups_user = json.loads(all_lineups_user.text)

            lineups_user_file_name = core_file+str(contest_id) + "_" + str(user_id) +"_"+"lineups_user.txt"
            with open(lineups_user_file_name, 'w') as file:
                file.write(json.dumps(lineups_user))

            lineups_file_name = core_file+str(contest_id) + "_" + str(user_id)   +"_" + "lineups_player.txt"
            with open(lineups_file_name, 'w') as file:
                file.write(json.dumps(lineups))

            time.sleep((random.randint(10,30)))

browser.close()
browser.quit()