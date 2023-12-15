maxRed = 12
maxGreen = 13
maxBlue = 14

def getDeals(line):
    (gameId, game) = map(str.strip, line.split(": "))
    gameNo = gameId.split(' ')[-1]
    gameDeals = game.split('; ')
    return (int(gameNo), map(lambda deal: deal.split(', '), gameDeals))

def dealPossible(deal):
    [amount, color] = deal.split(' ')
    if color == 'red': return int(amount) <= maxRed
    if color == 'green': return int(amount) <= maxGreen
    if color == 'blue': return int(amount) <= maxBlue

def gamePossible(deals):
    return all(map(lambda deal: all(map(dealPossible, deal)), deals))

with open("2/input.txt") as file:
    lines = file.readlines()
    deals = map(getDeals, lines)
    print(
        sum(
            map(
                lambda deal: deal[0] if gamePossible(deal[1]) else 0,
                deals
            )
        )
    )
