"""
    GROUP: Gym Buddy
    MEMBERS: ​Brenden Carroll, Stefani Page, Elina Tsykhmistrenko, Justin White, Hamza Zgidou​ 
    COURSE: CMSC 495:7383
    FILE: fogsaaUtil.py
"""

import heapq
import enum

"""
    FOGSAA algorithm which this file uses is believed to be more efficient than the standard Needleman-Wunsch algorithm.
    Chakraborty, A., Bandyopadhyay, S. FOGSAA: Fast Optimal Global Sequence Alignment Algorithm. Sci Rep 3, 1746 (2013). https://doi.org/10.1038/srep01746
"""

class Types(enum.Enum):
    """
        Simple enumerator to make comparison values neater. Can directly edit weights by changing these values. Currently the order of priority
        (excluding oneToOne and root which are placeholders) is match > gap > root
    """
    oneToOne = 0
    match = -2
    mismatch = 2
    gap = 1
    root = 0

class Node:
    """
        Node class which acts as the current stage of the comparison. Holds one value from each array, as well as possible extreme scores and its current score.
    """
    
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
        """
            Determines if the two nodes in the element are a match or mismatch, breaks and shortened routines contain None values
            which act as wildcards as one buddy resting doesnt interfere with their ability to be with the other during an exercise.
        """
        if self.arr1[self.idx1] == self.arr2[self.idx2] or (self.arr1[self.idx1] is None) or (self.arr2[self.idx2] is None):
            return Types.match
        else:
            return Types.mismatch
        
    def calculateFutureScores(self):
        """
            Calculates the best and worst possible scores if continuing the sequence matching from the current node.
        """
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
        """
            Generates up to 3 children. The options for the children result from: a gap in one sequence, a gap in the other sequence, a direct comparison.
            NOTE: Terminal nodes aka ones with no children are used as the only potential best scores
        """
        if not self.children:
            if len(self.arr1) - (self.idx1 + 1):
                self.children.append(Node(arr1=self.arr1, arr2=self.arr2, idx1=self.idx1 + 1, idx2=self.idx2, parent_present_score=self.presentScore, type=Types.gap))
            if len(self.arr2) - (self.idx2 + 1):
                self.children.append(Node(arr1=self.arr1, arr2=self.arr2, idx1=self.idx1, idx2=self.idx2 + 1, parent_present_score=self.presentScore, type=Types.gap))
            if (len(self.arr1) > (self.idx1+1)) and (len(self.arr2) > (self.idx2+1)):
                self.children.append(Node(arr1=self.arr1, arr2=self.arr2, idx1=self.idx1 + 1, idx2=self.idx2 + 1, parent_present_score=self.presentScore, type=Types.oneToOne))

    def getChildren(self):
        """
            Generate the children for a node if needed and return the array of child nodes
        """
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
        """
            Fitness scores are the sum of the known current score and the potential best and worst scores for the sequences originating from any node.
        """
        return (self.presentScore + self.futureScores[0], self.presentScore + self.futureScores[1])
    
# @staticmethod
def compareSequences(arr1, arr2):
    """Used to perform the FOGSAA comparison on any two sequences.
        NOTE: It returns the negative of the best fitness score achieved, as the fitness scores were only made
            negative to aid in node-node comparisons. The higher the output number, the better.
    """
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