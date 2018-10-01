sPile = 100  # type: int
maxStones = 5
minStones = 1
noPlayer = 2
playerTurn = 1
qStr = "Player {} how many stones do you want? (1 - {})"

while sPile > 0:
    guess = -1
    while guess < minStones or guess > maxStones:
        guess = input(qStr.format(playerTurn, (sPile if sPile < maxStones else maxStones)))
        if guess.isdigit():
            guess = int(guess)
        else:
            guess = -1
    sPile -= guess
    if sPile <= 0:
        print("Player {} wins!".format(playerTurn))
    else:
        print("There are {} stones left".format(sPile))
    if playerTurn < noPlayer:
        playerTurn = playerTurn + 1
    else:
        playerTurn = 1

print("Game Over!")
