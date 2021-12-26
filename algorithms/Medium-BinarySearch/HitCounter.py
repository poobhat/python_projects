class HitCounter:

    def __init__(self):
        self.hitList = []
        self.hitMap = {}

    def counter(self, timestamp):
        if timestamp > 300:
            pop= timestamp-300
            suphitList = [(k,v) for k,v in self.hitMap.items()]
            print(f"suphitList : {suphitList}")
            print(f"pop : {pop}")
            if pop <= len(suphitList):
                superPop = suphitList[pop-1]
                popIdx = self.hitList.index(superPop)
                return len(self.hitList[popIdx+1:])
            else:
                return 0
        else:
            return len(self.hitList)

    def hit(self, timestamp: int) -> None:
        print(f"hitList : {self.hitList}")
        self.hitList.append((timestamp,self.counter(timestamp)+1))

    def getHits(self, timestamp: int) -> int:
        self.hitMap = dict(self.hitList)
        print(f"hitList : {self.hitList}")
        print(f"hitMap : {self.hitMap}")
        if timestamp in self.hitMap:
            return self.hitMap[timestamp]
        else:
            return self.counter(timestamp)