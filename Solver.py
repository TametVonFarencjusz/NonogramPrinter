import Board as brd

#marks
def GenerateLines(nums, length):
    pass

def CountLineFreedom(nums, length):
    return length - sum(nums) - len(nums) + 1

class Solver:
    board = None
    type = 0
    hlistmark = []
    vlistmark = []

    def __init__(self, hlist, vlist):
        self.board = brd.Board(pack = (hlist, vlist))
        if not self.checkpointcount():
            print("ERROR: Wrong hlist/vlist")
        for nums in self.board.verticalVector:
            self.vlistmark.append(0 if nums == [0] else CountLineFreedom(nums, self.board.rows))
        for nums in self.board.horizontalVector:
            self.hlistmark.append(0 if nums == [0] else CountLineFreedom(nums, self.board.cols))

    def checkpointcount(self):
        count = 0
        for nums in self.board.verticalVector:
            count += sum(nums)
        for nums in self.board.horizontalVector:
            count -= sum(nums)

        if count != 0:
            print(count)
        return count == 0

    def solve(self):
        if self.type == 0:
            #first round
            for i, freedom in enumerate(self.vlistmark):
                if freedom == 0:
                    print(f"nums: {self.board.verticalVector[i]}")
                if freedom < 0:
                    print("ERROR")
            #for nums in self.board.horizontalVector:
            #    if CountLineFreedom(nums, self.board.rows) == 0 or nums == [0]:
            #        print(f"nums: {nums}")

            #other rounds - loop
            while False:
                pass
