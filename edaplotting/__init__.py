# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# Set default Seaborn style
sns.set()

class univariate(object):

    percentiles = np.array([2.5,25,50,75,97.5]) # Specify array of percentiles

    def __init__(self,data):
        self.data = data

    def plot(self):
        """plotting for a one-dimensional array of measurements."""

        if len(self.data)>=100:
            self.data = self.data.sample(n=100)

        ptiles_data = np.percentile(self.data,self.percentiles) # Compute percentiles: ptiles_vers
        n = len(self.data) # Number of data points: n
        x = np.sort(self.data) # x-data for the ECDF: x
        y = np.arange(1,n+1) / n # y-data for the ECDF: y

        fig, axes = plt.subplots(nrows=2, ncols=2,figsize=(10,10))
        fs = 13  # fontsize

        fig.suptitle("EDA on a one-dimensional array",fontsize=16)

        # Plot the Emperical CDF
        axes[0, 0].plot(x, y, marker = '.', linestyle = 'none')
        # Overlay percentiles as red diamonds.
        axes[0, 0].plot(ptiles_data, self.percentiles/100, marker='D', color='red', linestyle='none')
        axes[0, 0].set_title('Emperical CDF', fontsize=fs)
        vals0 = axes[0, 0].get_yticks()
        axes[0, 0].set_yticklabels(['{:3.2f}%'.format(x*100) for x in vals0])

        # Plot the Hist
        axes[0, 1].hist(self.data, normed=1, histtype='bar')
        axes[0, 1].set_title('Histogram', fontsize=fs)
        vals1 = axes[0, 1].get_yticks()
        axes[0, 1].set_yticklabels(['{:3.2f}%'.format(x*100) for x in vals1])

        # Create bee swarm plot with Seaborn's default setting
        sns.swarmplot(self.data,ax=axes[1, 0],color='green')
        axes[1, 0].set_title('Swarmplot', fontsize=fs)

        # Create box plot with Seaborn's default setting
        sns.boxplot(self.data,ax =axes[1, 1],color='purple')
        axes[1, 1].set_title('Boxplot', fontsize=fs)

        # Display the plot
        plt.show()
