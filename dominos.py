import random
dominos = [
  {
    "top": 0,
    "bottom": 0,
      "picked": False

  },
  {
    "top": 0,
    "bottom": 1,
    "picked": False
  },
  {
    "top": 1,
    "bottom": 1,
    "picked": False
  },
  {
    "top": 0,
    "bottom": 2,
    "picked": False
  },
  {
    "top": 1,
    "bottom": 2,
    "picked": False
  },
  {
    "top": 2,
    "bottom": 2,
    "picked": False
  },
  {
    "top": 0,
    "bottom": 3,
    "picked": False
  },
  {
    "top": 1,
    "bottom": 3,
    "picked": False
  },
  {
    "top": 2,
    "bottom": 3,
    "picked": False
  },
  {
    "top": 3,
    "bottom": 3,
    "picked": False
  },
  {
    "top": 0,
    "bottom": 4,
    "picked": False
  },
  {
    "top": 1,
    "bottom": 4,
    "picked": False
  },
  {
    "top": 2,
    "bottom": 4,
    "picked": False
  },
  {
    "top": 3,
    "bottom": 4,
    "picked": False
  },
  {
    "top": 4,
    "bottom": 4,
    "picked": False
  },
  {
    "top": 0,
    "bottom": 5,
    "picked": False
  },
  {
    "top": 1,
    "bottom": 5,
    "picked": False
  },
  {
    "top": 2,
    "bottom": 5,
    "picked": False
  },
  {
    "top": 3,
    "bottom": 5,
    "picked": False
  },
  {
    "top": 4,
    "bottom": 5,
    "picked": False
  },
  {
    "top": 5,
    "bottom": 5,
    "picked": False
  },
  {
    "top": 0,
    "bottom": 6,
    "picked": False
  },
  {
    "top": 1,
    "bottom": 6,
    "picked": False
  },
  {
    "top": 2,
    "bottom": 6,
    "picked": False
  },
  {
    "top": 3,
    "bottom": 6,
    "picked": False
  },
  {
    "top": 4,
    "bottom": 6,
    "picked": False
  },
  {
    "top": 5,
    "bottom": 6,
    "picked": False
  },
  {
    "top": 6,
    "bottom": 6,
    "picked": False
  }
]



# shuffled_dominos = random.shuffle(list(range(29)), 29)

shuffled = sorted(dominos, key=lambda k: random.random())

# player1_dominos =shuffled_dominos[0:14]

print(type(shuffled))
print(type(dominos))

now_playing =random.randint(0,1)

print(now_playing)

board =[]


winner=None

first_play =True



class Player:

    def __init__(self, tiles, playing):
        self.tiles=tiles
        self.playing =playing


player1 = Player(tiles=shuffled[0:14],playing= False)
player2 = Player(tiles=shuffled[14:28], playing=False)





if now_playing == 0:
    player1.playing=True

else:
    player2.playing= True



def select_domino(tiles):

    tile_index =None

    if first_play:
        tile_index = random.randint(0,13)
    else:
        tile_index=0

    return tiles[tile_index]







def play(player, currentBoard):
    played_domino = select_domino(player.tiles)

    board.append(played_domino)

    remaining_tiles =player.tiles.filter()













