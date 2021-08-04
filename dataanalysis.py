import pandas as pd
class NotPandasDataFrame(Exception):
    pass

class DataAnalysis:
    def __init__(self, df):
        if (isinstance(df, pd.DataFrame)):
            self.df = df
            self.Head()
            self.Info()
            self.Describe()
        else:
            raise NotPandasDataFrame(df)
    def Head(self):
        choice = input("enter yes to view the output provided from pandas head method")
        if (choice.upper() == "YES"):
            print("the defualt amount of rows you will see is 5")
            try:
                values = int(input("press enter if that is fine or enter the amount of rows you would like to view"))
            except ValueError:
                values = None
            if (values is not None):
                print(self.df.head(values))
            else:
                print(self.df.head())
    def Info(self):
        choice = input("enter yes to view the output from the pandas info method")
        if (choice.upper() == "YES"):
            print(self.df.info())
            objectlist = []
            for i in self.df.columns:
                if self.df[i].dtypes == "object":
                    objectlist.append(i)
            if len(objectlist):
                print(f"the columns called\n {objectlist}\n are objects types")
                values = input("enter yes to view the values of these columns")
                count = 0
                while (values.upper() == "YES"):
                    print(self.df[objectlist[count]].value_counts())
                    count += 1
                    if (count>=len(objectlist)):
                        break
                    values = input("enter yes to view the next columns data")
    def Describe(self):
        print("the next values will be from pandas describe method")
        choice = input("enter yes to countinue")
        if (choice.upper() == "YES"):
            print(self.df.describe())