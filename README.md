# Beer_Generation
This repository is for a project attempting to use machine learning to generate craft beer recipes, in particular hop schedules

## Authors
Mitch Schiller and Kevin McPherson

## Data Acquisition
Beer data was compiled from two webscrapes done on a beer recipe database called Brewer's Friend. The first contained macro information such as category, ABV, IBU, etc.
The second joined this data with the recipe specifics: grains, hops, yeast, water additions and adjuncts.

## Data Cleaning
Using domain knowledge, I narrowed the dataset down to provide a higher quality of data for future learning, ridding the dataset of outliers, input errors, and extraneous information. This process was somewhat manual, using sorting and looking at cases in their entirety. Some general trimming of the lowest value counts was used to get rid of information that might serve better to confuse the algorithm(s) than help them.
In this process, I noticed that their was a disparity hidden amongest the data that would need to be dealt with: users of the original database could enter their recipes as Imperial or Metric, and no variables from the scrape were present to distinguish between them. After plotting the low and high temperatures of yeast strains from the dataset, an obvious divide in the data presented itself. The temperature histograms contained two distinct distributions, with little overalap. Drawing a line in the sand between these was therefore trivial, but the harder task will be to convert the metric records to imperial and build a pipeline that processes new data on this same divide.
