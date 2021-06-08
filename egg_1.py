class ThreeNums(object):
    def __init__(self, nums):
        self.nums = nums

    def thr_nums(self):
        for i in self.nums:
            for j in self.nums:
                for k in self.nums:
                    if i != j and i != k and j != k:
                        print(i,j,k)

test1 = ThreeNums([1,2,3,4])
test1.thr_nums()
