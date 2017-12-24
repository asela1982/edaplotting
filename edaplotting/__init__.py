# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import rcParams


# Set default Seaborn style
sns.set()

class explore():

    percentiles = np.array([2.5,25,50,75,97.5]) # Specify array of percentiles

    def __init__(self, **kwargs):
        valid_kwargs = ['x', 'y']
        for k, v in kwargs.items():
            if k not in valid_kwargs:
                raise TypeError("Invalid keyword argument %s" % k)
            setattr(self, k, v)   

    def plot_univariate(self):
        """plotting for a one-dimensional array(numeric) of measurements."""

        # extract a random sample of 100 data points
        if len(self.x)>=100:
            x = self.x.sample(n=100)

        # set plot attributes   
        titlefont = {'fontname':"cursive",'weight':'bold', 'fontsize':25}
        axfont = {'fontname':"cursive",'weight':'bold','fontsize':20}
        rcParams['axes.titlepad'] = 20 
        
        
        ptiles_data = np.percentile(self.x,self.percentiles) # Compute percentiles: ptiles_vers
        n = len(x) # Number of data points: n
        x = np.sort(x) # x-data for the ECDF: x
        y = np.arange(1,n+1) / n # y-data for the ECDF: y

        # subplots
        fig, axes = plt.subplots(nrows=2, ncols=2,figsize=(18,12))
        
        # set figure title
        fig.suptitle("EDA on a one-dimensional array",**titlefont)

        # Plot the Emperical CDF
        axes[0, 0].plot(x, y, marker = '.', linestyle = 'none')
        # Overlay percentiles as red diamonds.
        axes[0, 0].plot(ptiles_data, self.percentiles/100, marker='D', color='red', linestyle='none')
        axes[0, 0].set_title('Emperical CDF', **axfont)
        vals0 = axes[0, 0].get_yticks()
        axes[0, 0].set_yticklabels(['{:3.2f}%'.format(x*100) for x in vals0])

        # Plot the Hist
        sns.distplot(x,ax=axes[0, 1],label=self.x.name,rug=True)
        axes[0, 1].set_title('Histogram', **axfont)
        vals1 = axes[0, 1].get_yticks()
        axes[0, 1].set_yticklabels(['{:3.2f}%'.format(x*100) for x in vals1])

        # Create bee swarm plot with Seaborn's default setting
        sns.swarmplot(x,ax=axes[1, 0],color='green')
        axes[1, 0].set_title('Swarmplot', **axfont)

        # Create box plot with Seaborn's default setting
        sns.boxplot(x,ax =axes[1, 1],color='purple',saturation=1)
        axes[1, 1].set_title('Boxplot', **axfont)

        # Display the plot
        plt.show()
        
        
    def plot_bivariate(self):
        """plotting for a two-dimensional array(numeric) of measurements."""
            

        # set plot attributes   
        titlefont = {'fontname':"cursive",'weight':'bold', 'fontsize':25}
        axfont = {'fontname':"cursive",'weight':'bold','fontsize':20}
        rcParams['axes.titlepad'] = 20 
        

        # subplots
        fig, axes = plt.subplots(nrows=1, ncols=3,figsize=(18,8))
        
        # set figure title
        fig.suptitle("EDA on a two-dimensional array",**titlefont)

        # scatter
        # Create scatter plot with Seaborn's default setting
        sns.regplot(x=self.x, y=self.y,color='g',marker="+",ax=axes[0])
        axes[0].set_title('scatter plot', **axfont)
    
    
        # Create scatter plot with Seaborn's default setting
        sns.kdeplot(self.x, self.y, ax=axes[1])
        sns.rugplot(self.x, color="g", ax=axes[1])
        sns.rugplot(self.y, vertical=True, ax=axes[1])
        axes[1].set_title('KDE', **axfont)
        
 
        # Create kde plot with Seaborn's default setting
        sns.kdeplot(self.x, self.y, ax=axes[1])
        sns.rugplot(self.x, color="g", ax=axes[1])
        sns.rugplot(self.y, vertical=True, ax=axes[1])
        axes[1].set_title('KDE', **axfont)
        
        # Create kde(n=60) plot with Seaborn's default setting
        cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
        sns.kdeplot(self.x, self.y, cmap=cmap, n_levels=60, shade=True,ax=axes[2])
        axes[2].set_title('KDE (n=60)', **axfont)
    
    
        # Display the plot
        plt.show()