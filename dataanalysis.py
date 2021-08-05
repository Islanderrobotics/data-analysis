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
            self.isnull()
            print("that is all I have for you have a good day")
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
    def isnull(self):
        choice = input("enter yes to see if your data set has any null values")
        if (choice.upper() == "YES"):
            isnull = []
            for i in self.df.columns:
                if (self.df[i].isnull().values.any()):
                    isnull.append(i)
            if (isnull !=[]):
                print(f"your data set has {len(isnull)} column with null values, would you like to see the column names\n"
                      "as well as the amount of null values in that column")
                columns = input("enter yes if you do")
                if columns.upper() == "YES":
                    for i in isnull:
                        print(f"in column {i}, there are {self.df[i].isnull().sum().sum()} cells with null values")