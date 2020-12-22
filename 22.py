def parseDeck(deck):
    return [int(n.strip()) for n in deck.splitlines()[1:]]

def anyPreviousState(deck, states):
    return tuple(deck) in states

def combat(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        card1 = p1.pop(0)
        card2 = p2.pop(0)
        winner = p1 if card1 > card2 else p2
        winnerCard = max(card1, card2)
        loserCard = min(card1, card2)
        winner.append(winnerCard)
        winner.append(loserCard)
    return p1 if len(p1) > 0 else p2

def recursiveCombat(p1, p2):
    previousP1 = []
    previousP2 = []
    while len(p1) > 0 and len(p2) > 0:
        if anyPreviousState(p1, previousP1) and anyPreviousState(p2, previousP2):
            return 1, p1
        else:
            previousP1.append(tuple(p1))
            previousP2.append(tuple(p2))
            card1 = p1.pop(0)
            card2 = p2.pop(0)
            if card1 <= len(p1) and card2 <= len(p2):
                number, __ = recursiveCombat(p1[:card1], p2[:card2])
                winner = p1 if number == 1 else p2
                winnerCard = card1 if number == 1 else card2
                loserCard = card2 if number == 1 else card1
                winner.append(winnerCard)
                winner.append(loserCard)
            else:
                winner = p1 if card1 > card2 else p2
                winnerCard = max(card1, card2)
                loserCard = min(card1, card2)
                winner.append(winnerCard)
                winner.append(loserCard)
    number = 1 if len(p1) > 0 else 2
    winner = p1 if len(p1) > 0 else p2
    return number, winner

decks = open('in/22.txt').read().split('\n\n')

p1, p2 = [parseDeck(d) for d in decks]
winner = combat(p1, p2)
print('part1:', sum((i+1) * n for i,n in enumerate(winner[::-1])))

p1, p2 = [parseDeck(d) for d in decks]
number, winner = recursiveCombat(p1, p2)
print('part2:', sum((i+1) * n for i,n in enumerate(winner[::-1])))