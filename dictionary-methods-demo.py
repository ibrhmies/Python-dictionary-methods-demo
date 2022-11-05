players = {
    "1": {
        "name": "Cristiano Ronaldo",
        "yearOfBirth": "1985",
        "nationality": "Portugal",
        "currentTeam": "Portugal",
        "history": "juventus, real madrid, portugal"
    },
    "2": {
        "name": "Lionel Messi",
        "yearOfBirth": "1987",
        "nationalty": "Argantina",
        "currentTeam": "Argantina",
        "history": "Barcelona, Argantina"
    }
}


id = input("oyuncu id bilgisini giriniz:")

player = players.get(id)

print(player)
#-> id bilgisine göre oyuncu aratma.

id = input("silmek istediğiniz oyuncu id:")

players.pop(id)

print(players)
#-> silmek istediğin id ile oyuncu silme
