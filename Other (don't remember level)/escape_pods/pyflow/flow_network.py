class FlowNetwork:
    def __init__(self, graph, sources, sinks):
        self.sourceIndex = None
        self.sinkIndex = None
        self.graph = graph

        self._normalizeGraph(sources, sinks)
        self.verticesCount = len(graph)
        self.maximumFlowAlgorithm = None

    # make only one source and one sink
    # also remove useless transitions
    # such as going to source or from sink
    def _normalizeGraph(self, sources, sinks):
        if sources is int:
            sources = [sources]
        if sinks is int:
            sinks = [sinks]

        if len(sources) == 0 or len(sinks) == 0:
            return

        # remove useless transitions
        for fromIndex, row in enumerate(self.graph):
            for toIndex, bandwidth in enumerate(row):
                if fromIndex == toIndex or fromIndex in sinks or toIndex in sources:
                    self.graph[fromIndex][toIndex] = 0

        self.sourceIndex = sources[0]
        self.sinkIndex = sinks[0]

        # make fake vertex if there are more
        # than one source or sink
        if len(sources) > 1 or len(sinks) > 1:
            maxInputFlow = 0
            for i in sources:
                maxInputFlow += sum(self.graph[i])


            size = len(self.graph) + 1
            for room in self.graph:
                room.insert(0, 0)
            self.graph.insert(0, [0] * size)
            for i in sources:
                self.graph[0][i + 1] = maxInputFlow
            self.sourceIndex  = 0

            size = len(self.graph) + 1
            for room in self.graph:
                room.append(0)
            self.graph.append([0] * size)
            for i in sinks:
                self.graph[i + 1][size - 1] = maxInputFlow
            self.sinkIndex = size - 1


    def findMaximumFlow(self):
        if self.maximumFlowAlgorithm is None:
            raise Exception("You need to set maximum flow algorithm before.")
        if self.sourceIndex is None or self.sinkIndex is None:
            return 0

        self.maximumFlowAlgorithm.execute()
        # return relabel_to_front(self.graph, self.sourceIndex, self.sinkIndex)
        return self.maximumFlowAlgorithm.getMaximumFlow()

    def setMaximumFlowAlgorithm(self, Algorithm):
        self.maximumFlowAlgorithm = Algorithm(self)


class FlowNetworkAlgorithmExecutor(object):
    def __init__(self, flowNetwork):
        self.flowNetwork = flowNetwork
        self.verticesCount = flowNetwork.verticesCount
        self.sourceIndex = flowNetwork.sourceIndex
        self.sinkIndex = flowNetwork.sinkIndex
        # it's just a reference, so you shouldn't change
        # it in your algorithms, use deep copy before doing that
        self.graph = flowNetwork.graph
        self.executed = False

    def execute(self):
        if not self.executed:
            self._algorithm()
            self.executed = True

    # You should override it
    def _algorithm(self):
        pass



class MaximumFlowAlgorithmExecutor(FlowNetworkAlgorithmExecutor):
    def __init__(self, flowNetwork):
        super(MaximumFlowAlgorithmExecutor, self).__init__(flowNetwork)
        # use this to save your result
        self.maximumFlow = -1

    def getMaximumFlow(self):
        if not self.executed:
            raise Exception("You should execute algorithm before using its result!")

        return self.maximumFlow
