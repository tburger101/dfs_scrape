# dfs_scrape
Website Scraping

This script scrapes the fantasy labs contest dashoboard for NFL contests and outputs different types of JSON files (as described below under the Variables and Outputs section).  It takes not only the top 100 lineups in each contsest but also scrapes specific users teams.  I selected some of the top NFL DFS players per the Rotogrinders ratings to examine the team.  By changing the varaibale date in the script you get different historical data.

## Required Libraries
* JSON
* Selenium
* bs4

## Variables and Outputs 
* users- Stores a user ID to entry ID Relationship
* players - Stores player details for the contest like salary and position
* leaders- Stores the team makeup of the top 100 entries
* lineups_user- Stores all the lineup information of specific users.  
