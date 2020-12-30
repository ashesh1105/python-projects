from dispenser50 import Dispenser50
from dispenser20 import Dispenser20
from dispenser10 import Dispenser10

class ATMDispenserChain: # pylint: disable=too-few-public-methods
    """The Chain Client"""

    def __init__(self):
        # initialize the successor chain
        self.chain1 = Dispenser50()
        self.chain2 = Dispenser20()
        self.chain3 = Dispenser10()

        # set the chain of responsibility
        # The Client may compose chains once or
        # the hadler can set them dynamically at
        # handle time
        self.chain1.set_successor(self.chain2)
        self.chain2.set_successor(self.chain3)


if __name__ == "__main__":

    ATM = ATMDispenserChain()

    AMOUNT = int(input("Enter amount to withdrawal : "))
    if AMOUNT < 10 or AMOUNT % 10 != 0:
        print("Amount should be positive and in multiple of 10s.")
        exit()
    # process the request
    ATM.chain1.handle(AMOUNT)
    print("Now go spoil yourself")