# !python 3
# simpleScript.py - Attending assignments

import pandas as pd

class User:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender
    
    def genDataFrame(self) -> pd.DataFrame:
        return pd.DataFrame(data=[self.name, self.age, self.gender],
                            columns=['name', 'age', 'gender'])

def main():
    exampleUser = User(name='John', 
                       age=23,
                       gender='M')
    df = exampleUser.genDataFrame()
    print(df)

if __name__=='__main__':
    main()