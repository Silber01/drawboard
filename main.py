from random import randrange


class Dot:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = str(color)[0]

    def __str__(self):
        return self.color

    def __repr__(self):
        return f"x = {self.x}, y = {self.y}, color = {self.color}"


emptyColor = "."


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        for h in range(height):
            thisRow = []
            for w in range(width):
                thisRow.append(Dot(w, h, emptyColor))
            self.grid.append(thisRow)

    def get(self, x, y):
        return self.grid[y][x]

    def set(self, x, y, color):
        self.get(x, y).color = str(color)[0]

    def __str__(self):
        strRep = ""
        for h in range(self.height):
            for w in range(self.width):
                strRep += str(self.get(w, h)) + "  "
            strRep += "\n"
        return strRep

    def drawLine(self, x1, y1, x2, y2, color):
        if x1 not in range(0, self.width) or x2 not in range(0, self.width) \
                or y1 not in range(0, self.height) or y2 not in range(0, self.height):
            print("Out of bounds!")
            return
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)):
                self.set(x1, i, color)
            return
        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)):
                self.set(i, y1, color)
            return
        slope = (y2 - y1) / (x2 - x1)
        yInt = y2 - (slope * x2)
        if abs(slope) < 1:
            for xValue in range(min(x1, x2), max(x1, x2) + 1):
                # print(f"{xValue}, {(slope * (xValue - lX)) + lY}")
                yExact = (slope * xValue) + yInt
                yValue = round(yExact)
                self.set(xValue, yValue, color)
        else:
            for yValue in range(min(y1, y2), max(y1, y2) + 1):
                xExact = (yValue - yInt) / slope
                xValue = round(xExact)
                self.set(xValue, yValue, color)

    def clear(self):
        for h in range(self.height):
            for w in range(self.width):
                self.set(w, h, emptyColor)


def main():
    width = int(input("Insert width: "))
    height = int(input("Insert height: "))
    lines = int(input("Insert amount of lines: "))
    thisGrid = Grid(width, height)
    for i in range(lines):
        x1 = randrange(width)
        x2 = randrange(width)
        y1 = randrange(height)
        y2 = randrange(height)
        thisGrid.drawLine(x1, y1, x2, y2, chr(ord("A") + i))
        thisGrid.set(x1, y1, "s")
        thisGrid.set(x2, y2, "e")
    print(thisGrid)
        # thisGrid.clear()


main()
