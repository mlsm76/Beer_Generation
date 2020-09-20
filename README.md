# Beer_Generation
This repository is for a project attempting to use machine learning to generate craft beer recipes.

## Authors
Mitch Schiller and Kevin McPherson

## Data Acquisition
Beer data was compiled from two webscrapes done on a beer recipe database called Brewer's Friend. The first contained macro information such as category, ABV, IBU, etc.
The second joined this data with the recipe specifics: grains, hops, yeast, water additions and adjuncts.

## Data Cleaning
Using domain knowledge, I narrowed the dataset down to provide a higher quality of data for future learning, ridding the dataset of outliers, input errors, and extraneous information. This process was somewhat manual, using sorting and looking at cases in their entirety. Some general trimming of the lowest value counts was used to get rid of information that might serve better to confuse the algorithm(s) than help them.
In this process, I noticed that their was a disparity hidden amongest the data that would need to be dealt with: users of the original database could enter their recipes as Imperial or Metric, and no variables from the scrape were present to distinguish between them. After plotting the low and high temperatures of yeast strains from the dataset, an obvious divide in the data presented itself. The temperature histograms contained two distinct distributions, with little overalap. Drawing a line in the sand between these was therefore trivial, but the harder task will be to convert the metric records to imperial and build a pipeline that processes new data on this same divide.

## Clustering Beer Styles
As a form of exploration, and to get an idea of how the dataframe behaves, we used Mini Batch Kmeans to cluster the data around the 167 unique styles in the dataframe. This will give us an idea of how cleanly each item fits into a particular category, and if some level of PCA will be appropropriate. Ultimately, this is a way to create visualizations that can give a viewer an idea of how the data is grouped together. Next, we will see how well a machine learning model can predict category, if we were to remove that column and use it as the target variable in a classification model, with the rest of the dataframe serving as features.

## Classification on Style/Category
We will be looking at different classification models and how they perform when asked to predict beer category, based on the inputs to the recipe and recipe specifics pulled from the Brewer's Friend website.
