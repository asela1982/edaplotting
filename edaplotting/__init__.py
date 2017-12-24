# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import rcParams



# Set default Seaborn style
sns.set()

class univariate():

    percentiles = np.array([2.5,25,50,75,97.5]) # Specify array of percentiles

    def __init__(self,data):
        self.data = data

    def plot(self):
        """plotting for a one-dimensional array of measurements."""

        if len(self.data)>=100:
            self.data = self.data.sample(n=100)

            
        titlefont = {'fontname':"cursive",'weight':'bold', 'fontsize':25}
        axfont = {'fontname':"cursive",'weight':'bold','fontsize':20}
        rcParams['axes.titlepad'] = 20 
        
        ptiles_data = np.percentile(self.data,self.percentiles) # Compute percentiles: ptiles_vers
        n = len(self.data) # Number of data points: n
        x = np.sort(self.data) # x-data for the ECDF: x
        y = np.arange(1,n+1) / n # y-data for the ECDF: y

        fig, axes = plt.subplots(nrows=2, ncols=2,figsize=(15,12))
        

        fig.suptitle("EDA on a one-dimensional array",**titlefont)

        # Plot the Emperical CDF
        axes[0, 0].plot(x, y, marker = '.', linestyle = 'none')
        # Overlay percentiles as red diamonds.
        axes[0, 0].plot(ptiles_data, self.percentiles/100, marker='D', color='red', linestyle='none')
        axes[0, 0].set_title('Emperical CDF', **axfont)
        vals0 = axes[0, 0].get_yticks()
        axes[0, 0].set_yticklabels(['{:3.2f}%'.format(x*100) for x in vals0])

        # Plot the Hist
        axes[0, 1].hist(self.data, normed=1, histtype='bar')
        axes[0, 1].set_title('Histogram', **axfont)
        vals1 = axes[0, 1].get_yticks()
        axes[0, 1].set_yticklabels(['{:3.2f}%'.format(x*100) for x in vals1])

        # Create bee swarm plot with Seaborn's default setting
        sns.swarmplot(self.data,ax=axes[1, 0],color='green')
        axes[1, 0].set_title('Swarmplot', **axfont)

        # Create box plot with Seaborn's default setting
        sns.boxplot(self.data,ax =axes[1, 1],color='purple',saturation=1)
        axes[1, 1].set_title('Boxplot', **axfont)

        # Display the plot
        plt.show()
