In this notebook I use MTA data from 2010-2014. The goal is to detect extreme events, trends and seasonal patterns in the data.

First, I aggregate the data in one time series of cummulative rides over time and observe an extremely low ridership in the last week 
of October 2012. The finding is explained by an extreme event occurred in NYC during this time (Hurricane Sandy).

Second, I aggregate rides based on the type of ridership and identify the types that show a constantly increasing or decreasing trend.

Third, I use Fourier transformation to to detect periodicity in the data for each station. I identify the stations with the strongest
annual seasonal pattern. 

Finally, I use KMeans algorithm to cluster the types of ridership based on their popularity over time. The algorithm performs 
well in identifying the ones with increasing, decreasing, or steady popularity. 
