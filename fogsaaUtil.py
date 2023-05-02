import heapq
import enum

testarr1 = [0,3,2,5,7,6,1]
testarrs = [[0,3,5,7,1],
            [0,3,1,5,7,6,2],
            [0,3,2,5,7,6,1],
            [0,3,2],
            [1,2,3,4,5,6,7]]

class Types(enum.Enum):
    oneToOne = 0
    match = -2
    mismatch = 2
    gap = 1
    root = 0

class Node:
    
    def __init__(self, arr1, arr2, idx1, idx2, parent_present_score, type=Types.oneToOne):
        self.arr1 = arr1
        self.arr2 = arr2
        self.idx1 = idx1
        self.idx2 = idx2
        self.type = type
        self.children = []
        if self.type == Types.oneToOne:
            self.type = self.determineMatch()
        else:
            self.type = type
        self.presentScore = parent_present_score + self.type.value
        self.futureScores = self.calculateFutureScores()
        self.fitnessScores = self.calculateFitnessScores()

    def determineMatch(self):
        if self.arr1[self.idx1] == self.arr2[self.idx2] or (self.arr1[self.idx1] is None) or (self.arr2[self.idx2] is None):
            return Types.match
        else:
            return Types.mismatch
        
    def calculateFutureScores(self):

        len1 = len(self.arr1) - self.idx1
        len2 = len(self.arr2) - self.idx2

        if len2 < len1:
            fut_min = (len2 * Types.mismatch.value) + ((Types.gap.value) * (len1-len2))
            fut_max = (len2 * Types.match.value) + ((Types.gap.value) * (len1-len2))
        else:
            fut_min = (len1 * Types.mismatch.value) + ((Types.gap.value) * (len2-len1))
            fut_max = (len1 * Types.match.value) + ((Types.gap.value) * (len2-len1))

        return (fut_min, fut_max)
    
    def generateChildren(self):
        if not self.children:
            if len(self.arr1) - (self.idx1 + 1):
                self.children.append(Node(arr1=self.arr1, arr2=self.arr2, idx1=self.idx1 + 1, idx2=self.idx2, parent_present_score=self.presentScore, type=Types.gap))
            if len(self.arr2) - (self.idx2 + 1):
                self.children.append(Node(arr1=self.arr1, arr2=self.arr2, idx1=self.idx1, idx2=self.idx2 + 1, parent_present_score=self.presentScore, type=Types.gap))
            if (len(self.arr1) > (self.idx1+1)) and (len(self.arr2) > (self.idx2+1)):
                self.children.append(Node(arr1=self.arr1, arr2=self.arr2, idx1=self.idx1 + 1, idx2=self.idx2 + 1, parent_present_score=self.presentScore, type=Types.oneToOne))

    def getChildren(self):
        if not self.children:
            self.generateChildren()
        return self.children
    
    # Custom comparison values for use in the priority queue. Nodes are to be compared by max fitness scores.
    def __eq__(self, other):
        return self.fitnessScores[1] == other.fitnessScores[1]
    def __ne__(self, other):
        return not (self == other)
    def __lt__(self, other):
        return self.fitnessScores[1] < other.fitnessScores[1]
    def __gt__(self, other):
        return self.fitnessScores[1] > other.fitnessScores[1]
    def __le__(self, other):
        return self.fitnessScores[1] <= other.fitnessScores[1]
    def __ge__(self, other):
        return self.fitnessScores[1] >= other.fitnessScores[1]

    def calculateFitnessScores(self):
        return (self.presentScore + self.futureScores[0], self.presentScore + self.futureScores[1])
    
@staticmethod
def compareSequences(arr1, arr2):
    """Used to perform the FOGSAA comparison on any two sequences.
        NOTE: It returns the negative of the best fitness score achieved, as the fitness scores were only made
                negative to aid in node-node comparisons. The higher the output number, the better."""
    expand = Node(arr1=arr1, arr2=arr2, parent_present_score=0, idx1=-1, idx2=-1, type=Types.root)
    current_best = 10000
    alternatives = []
    heapq.heapify(alternatives)
    for child in expand.getChildren():
        heapq.heappush(alternatives, child)
    while alternatives[0].fitnessScores[1] <= current_best:
        expand = heapq.heappop(alternatives)
        while expand.getChildren():
            for child in expand.getChildren():
                heapq.heappush(alternatives, child)
            expand = heapq.heappop(alternatives)
        if (not expand.getChildren()) and expand.presentScore < current_best:
            current_best = expand.presentScore
    return -1 * current_best