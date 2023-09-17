def main():
    lvl = 1

    auctions = []
    with open(f"lvl{lvl}_in", "r") as f:
        for line in f:
            line = line.strip()
            auctions.append(line.split(','))

    for auction in auctions:
        # Initialise start bid
        start_bid = int(auction[0])

        # Get list of bidder objects through make_bidder_list function
        bidders = make_bidder_list(auction)

        # Set current and max bid
        current_bid = start_bid
        max_bid = start_bid

        # Handling first bid
        bidder = bidders[0]
        bid = bidder.bid
        if bid >= start_bid:
            winner = bidder
            max_bid = bid

        # Looking through every bidder
        for bidder in bidders:
            bid = bidder.bid
            if bid > current_bid:
                if bid > max_bid:
                    winner = bidder
                    current_bid = max_bid + 1
                    max_bid = bid
                elif bid < max_bid:
                    current_bid = bid + 1
                elif bid == max_bid:
                    current_bid = max_bid

        # Print result
        print(f"{winner.name},{current_bid}")


class Bidder:
    def __init__(self, name, bid):
        self.name = name
        self.bid = bid


def make_bidder_list(auction):
    # Remove start bid
    auction.pop(0)

    # Initialise list of bidders
    bidders = []

    # Make list of bidders with bidder name and bid
    for i, element in enumerate(auction):
        # Every second element contains the bidder's name
        if i % 2 == 0:
            bidder = Bidder(element, int(auction[i+1]))
            bidders.append(bidder)

    return bidders


if __name__ == "__main__":
    main()