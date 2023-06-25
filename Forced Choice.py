numberOfCards, secretCard, steps = list(map(int, input().split()))

for _ in range(steps):
    numberOfCardsChosen, *chosen_cards = list(map(int, input().split()))

    if secretCard in chosen_cards:
        print("KEEP")
    else:
        print("REMOVE")
