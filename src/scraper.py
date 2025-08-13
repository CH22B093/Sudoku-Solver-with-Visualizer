"""
Web scraper to fetch Sudoku from New York Times website.
"""
import requests
from bs4 import BeautifulSoup
import json

def fetch_nyt_sudoku():
    url = 'https://www.nytimes.com/puzzles/sudoku'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    script = soup.find('script', {'id': '__NEXT_DATA__', 'type': 'application/json'})
    data = json.loads(script.string)
    grid = data['props']['pageProps']['initialState']['puzzle']['puzzle']
    board = [grid[i*9:(i+1)*9] for i in range(9)]
    return board
