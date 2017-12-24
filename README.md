# edaplotting

In the words of John Turkey :
> Exploratory data analysis can never be the whole story, but nothing else can serve as the foundation stone.


### Dependencies

pandas (required) : https://pandas.pydata.org  
numpy (required): http://numpy.scipy.org  
matplotlib (required): http://matplotlib.sourceforge.net  
seaborn (required): https://seaborn.pydata.org  

## Example

### Installation

```
pip install edaplotting
```

### Usage

```python
# import the edaplotting library
import edaplotting as eda

# import pandas
import pandas as pd

# read in the dataset of interest 
df = pd.read_csv('Pokemon.csv')

# initialize the class with an one-dimensional array
object = eda.univariate(df['Speed'])

# plot the object
object.plot()
```

![png](output_0_0.png)


### License

MIT
