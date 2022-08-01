class MyGraphMatrix:
    def __init__(self, n):
        self.adjbody = []
        for i in range(n):
            self.adjbody.append([0] * n)

    def adj(self, v1, v2):
        self.adjbody[v1 - 1][v2 - 1] = 1

    def qadj(self, v1, v2):
        if self.adjbody[v1 - 1][v2 - 1] == 1:
            return True
        else:
            return False

    def trypath(self, l):
        for i in range(1, len(l)):
            if not g.qadj(l[i - 1], l[i]):
                return False
                break
            elif i==len(l)-1:
               return True


g = MyGraphMatrix(5)
g.adj(1, 2)
g.adj(1, 5)
g.adj(2, 1)
g.adj(2, 5)
g.adj(2, 3)
g.adj(2, 4)
g.adj(3, 2)
g.adj(3, 4)
g.adj(4, 2)
g.adj(4, 5)
g.adj(4, 3)
g.adj(5, 4)
g.adj(5, 1)
g.adj(5, 2)
print(g.adjbody)

print(g.trypath([1,2,5,4,3]))
print(g.trypath([1,3,5,4,3]))
print(g.trypath([1,2,4,3,5]))
print(g.trypath([1,2,4,3,2,5]))

