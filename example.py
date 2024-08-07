# !python 3
# example.py - Example of py script to repo

class Example:
    x: int = 1

    def __init__(self, y: int) -> None:
        self.y = y

    def add(self) -> int:
        return self.x + self.y
    
    def prod(self) -> int:
        return self.x * self.y

    def step(self) -> int:
        self.x += 1
        return self.x
    
def main():
    z = Example(y=10)
    print(z.x)
    print(z.add())
    print(z.prod())

    print(z.step())
    print(z.add())
    print(z.prod())

if __name__=='__main__':
    main()