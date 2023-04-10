import requests
from bs4 import BeautifulSoup
import psycopg2


def insert_monster(monster: str) -> None:

  
  conn = psycopg2.connect(
      host="localhost",
      database="zezenia",
      user="ysis",
      password="123123"
  )

  
  cursor = conn.cursor()

  sql = "INSERT INTO monsters (name) VALUES (%s)"
  val = (monster,)

  cursor.execute(sql, val)


  conn.commit()

  print(cursor.rowcount, "Adicionado")

url = "https://zezeniabrasil.com/monsters/"
headers = {
  'User-Agent': 'Mozilla/5.0 (intel MAC OS x 10.12; rv:55)'
}

response = requests.get(url, headers = headers)


soup = BeautifulSoup(response.content, "html.parser")

monster_names = soup.find_all("td", {"class": "name"})

for monster in monster_names:
  insert_monster(monster.text)