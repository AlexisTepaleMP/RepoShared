# !python 3
# simpleScript.py - Attending assignments

import pandas as pd

class User:
    def __init__(self, name: str, age: int, gender: str, fav_color: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.fav_color = fav_color
    
    def genDataFrame(self) -> pd.DataFrame:
        return pd.DataFrame(data=[self.name, self.age, self.gender, self.fav_color],
                            columns=['name', 'age', 'gender', 'fav_color'])

def main():
    exampleUser = User(name='John', 
                       age=23,
                       gender='M')
    df = exampleUser.genDataFrame()
    print(df)

if __name__=='__main__':
    main()