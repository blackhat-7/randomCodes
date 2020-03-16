class PQueue :
    pq = []
    size = 0

    def enque(self, v, p):
        i=0
        while(i<self.size and self.pq[i][1]>=p):
            i+=1
        self.pq.insert(i, [v, p])
        self.size+=1

    def print(self):
        for i in range(self.size):
            print(self.pq[i][0], end=" ")
        print()



def main():
    p = PQueue()
    p.enque(0, 5)
    p.enque(1,4)
    p.enque(2, 6)
    p.enque(3, 5)

    p.print()




if __name__ == "__main__":
    main()