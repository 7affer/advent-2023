maxRed = 12
maxGreen = 13
maxBlue = 14


def getDeals(line):
    (gameId, game) = map(str.strip, line.split(": "))
    gameNo = gameId.split(" ")[-1]
    gameDeals = game.split("; ")
    return (int(gameNo), map(lambda deal: deal.split(", "), gameDeals))


def dealPossible(deal):
    [amount, color] = deal.split(" ")
    amount = int(amount)
    if color == "red":
        return amount <= maxRed
    if color == "green":
        return amount <= maxGreen
    if color == "blue":
        return amount <= maxBlue


def gamePossible(deals):
    return all(map(lambda deal: all(map(dealPossible, deal)), deals))

with open("2/input.txt") as file:
    lines = file.readlines()
    deals = map(getDeals, lines)
    possibleDeals = map(lambda deal: deal[0] if gamePossible(deal[1]) else 0, deals)
    print(sum(possibleDeals))
