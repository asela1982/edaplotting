# edaplotting

In the words of John Turkey :
> Exploratory data analysis can never be the whole story, but nothing else can serve as the foundation stone.


### Dependencies

pandas (required) : https://pandas.pydata.org  
numpy (required): http://numpy.scipy.org  
matplotlib (required): http://matplotlib.sourceforge.net  
seaborn (required): https://seaborn.pydata.org  

### Key features

* Plot command that supports 4-in-1 with no requirment to import any plotting libraries :sunglasses:
* Supports univariate exploratory analysis 
* Takes only a 100 random data points for plotting
* Includes the ECDF plot : https://en.wikipedia.org/wiki/Empirical_distribution_function

## looks cool!! But how do i use this library? :confused:

### Installation

```
pip install edaplotting
```

### Usage

```python
import edaplotting as eda # import the edaplotting library and assign the alias eda
import pandas as pd # import pandas
df = pd.read_csv('Pokemon.csv') # read in a dataset of interest 
object = eda.univariate(df['Speed']) # initialize the class with an one-dimensional array
object.plot() # plot the object
```

![png](image.png)


### Todo

Expand to bivariate and multivariate exploratory analysis

### License

MIT
