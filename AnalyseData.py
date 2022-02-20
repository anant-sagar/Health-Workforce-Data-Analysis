from matplotlib.collections import BrokenBarHCollection
import pandas as pd


class Analyse:
    def __init__(self, path):
        self.df = pd.read_csv(path)

    def getDataframe(self):
        return self.df

    def getMapData(self, year):
        return self.df[self.df['Period'] == year].set_index('Location')['First Tooltip']

    def getLocations(self):
        return self.df.Location.unique()

    def getYears(self):
        return self.df.Period.unique()

    def getTopTooltop(self, n):
        return self.df.groupby('Location').mean()['First Tooltip'].sort_values(ascending=False).head(n)

    def getBottomTooltop(self, n):
        return self.df.groupby('Location').mean()['First Tooltip'].sort_values().head(n)

    def getTopLocationData(self, year, n):
        return self.df[self.df['Period'] == year].set_index('Location').sort_values('First Tooltip', ascending = False)['First Tooltip'].head(n)

    def getBottomLocationData(self, year, n):
        return self.df[self.df['Period'] == year].set_index('Location').sort_values('First Tooltip')['First Tooltip'].head(n)

    def getTopYearData(self, location, n):
        return self.df[self.df['Location'] == location].set_index('Period')['First Tooltip'].head(n)

