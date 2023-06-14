class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    # O(1) Time | O(1) Space
    def push(self, value):
        newMinMax = {"min": value, "max": value}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], value)
            newMinMax["max"] = max(lastMinMax["max"], value)
        self.minMaxStack.append(newMinMax)
        self.stack.append(value)

    # O(1) Time | O(1) Space
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    # O(1) Time | O(1) Space
    def top(self):
        return self.stack[len(self.stack) - 1]

    # O(1) Time | O(1) Space
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    # O(1) Time | O(1) Space
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]