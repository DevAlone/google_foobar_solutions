from pyflow.flow_network import MaximumFlowAlgorithmExecutor

class PushRelabelExecutor(MaximumFlowAlgorithmExecutor):
    def __init__(self, flowNetwork):
        super(PushRelabelExecutor, self).__init__(flowNetwork)

        self.preflow = [[0] * self.verticesCount for i in range(self.verticesCount)]

        self.heights = [0] * self.verticesCount
        self.excesses = [0] * self.verticesCount

    def _algorithm(self):
        print 'debug'
        for row in self.graph:
            print row
        print 'debug'
        self.heights[self.sourceIndex] = self.verticesCount

        # push some substance to graph
        for nextVertexIndex, bandwidth in enumerate(self.graph[self.sourceIndex]):
            self.preflow[self.sourceIndex][nextVertexIndex] += bandwidth
            self.preflow[nextVertexIndex][self.sourceIndex] -= bandwidth
            self.excesses[nextVertexIndex] += bandwidth

        # Relabel-to-front selection rule
        verticesList = [i for i in range(self.verticesCount)
                        if i != self.sourceIndex and i != self.sinkIndex]

        # move through list
        i = 0
        while i < len(verticesList):
            vertexIndex = verticesList[i]
            previousHeight = self.heights[vertexIndex]
            self.processVertex(vertexIndex)
            if self.heights[vertexIndex] > previousHeight:
                # if it was relabeled, swap elements
                # and start from 0 index
                verticesList.insert(0, verticesList.pop(i))
                i = 0
            else:
                i += 1

        self.maximumFlow = sum(self.preflow[self.sourceIndex])

    def processVertex(self, vertexIndex):
        while self.excesses[vertexIndex] > 0:
            for neighbourIndex in range(self.verticesCount):
                # if it's neighbour and current vertex is higher
                if self.graph[vertexIndex][neighbourIndex] - self.preflow[vertexIndex][neighbourIndex] > 0\
                        and self.heights[vertexIndex] > self.heights[neighbourIndex]:
                    self.push(vertexIndex, neighbourIndex)

            self.relabel(vertexIndex)

    def push(self, fromIndex, toIndex):
        preflowDelta = min(self.excesses[fromIndex],
                           self.graph[fromIndex][toIndex] - self.preflow[fromIndex][toIndex])
        self.preflow[fromIndex][toIndex] += preflowDelta
        self.preflow[toIndex][fromIndex] -= preflowDelta
        self.excesses[fromIndex] -= preflowDelta
        self.excesses[toIndex] += preflowDelta

    def relabel(self, vertexIndex):
        minHeight = None
        for toIndex in range(self.verticesCount):
            if self.graph[vertexIndex][toIndex] - self.preflow[vertexIndex][toIndex] > 0:
                if minHeight is None or self.heights[toIndex] < minHeight:
                    minHeight = self.heights[toIndex]

        if minHeight is not None:
            self.heights[vertexIndex] = minHeight + 1
