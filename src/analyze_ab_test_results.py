#!/usr/bin/env python
# coding: utf-8

# # Analyze A/B Test Results
# 
# This project will ensure you have mastered the subjects covered in the Hypothesis Testing lessons.  The hope is to have this project be as comprehensive of these topics as possible.  Good luck!
# 
# Corresponding with this notebook is a slide deck where you will need to update all the portions in red.  Completing the notebook will provide all the results needed for the slides.  **Correctly completing the slides is a required part of the project.**
# 
# ## Table of Contents
# - [Introduction](#intro)
# - [Part I - Descriptive Statistics](#descriptive)
# - [Part II - Probability](#probability)
# - [Part III - Experimentation](#experimentation)
# 
# 
# <a id='intro'></a>
# ### Introduction
# 
# A/B tests are very commonly performed by data analysts and data scientists.  For this project, you will be working to understand the results of an A/B test run by an e-commerce website.  Your goal is to work through this notebook to help the company understand if they should implement the new page, keep the old page, or perhaps run the experiment longer to make their decision.
# 
# **As you work through this notebook, follow along in the classroom and answer the corresponding quiz questions associated with each question.** The labels for each classroom concept are provided for each question.  This will assure you are on the right track as you work through the project, and you can feel more confident in your final submission meeting the criteria.  As a final check, assure you meet all the criteria on the rubric.
# 
# <a id='descriptive'></a>
# #### Part I - Descriptive Statistics
# 
# To get started, let's import our libraries.

# In[ ]:


import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

random.seed(0)


# For all questions in `Part I` notice links to [pandas documentation](https://pandas.pydata.org/) are provided to assist with answering the questions.  Though there are other ways you could solve the questions, the documentation is provided to assist you with one fast way to find the answer to each question.
# 
# 
# `a)` Now, read in the `ab_data.csv` data. Store it in `df`. Read in the dataset and take a look at the top few rows here. **This question is completed for you**.

# In[ ]:


df = pd.read_csv('ab_data.csv')
df.head()


# `b)` Use the below cell to find the number of rows in the dataset. [Helpful pandas link - `Dataframe.shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html#pandas.DataFrame.shape)

# In[ ]:





# `c)` The proportion of users converted.  [Helpful  Pandas Link - `Dataframe.mean`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html)

# In[ ]:





# `d)` Do any of the rows have missing values? [Helpful Pandas Link - `Dataframe.isnull`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html) and [Helpful Pandas Link- `Dataframe.sum`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html)

# In[ ]:





# `e)` How many customers are from each country? Build a bar chart to show the count of visits from each country.

# In[ ]:


# number of visitors from each country - pull the necessary code from the next cell to provide just the counts


# In[ ]:


# bar chart of results - this part is done for you
df['country'].value_counts().plot(kind='bar');
plt.title('Number of Visits From Each Country');
plt.ylabel('Count of Visits');
plt.show();


# `f)` Recognize that all of your columns are of a **categorical data type** with the exception of one.  Which column is not **categorical**? [Helpful Pandas Link](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html)

# In[ ]:





# `g)` What are the possible values of the `converted` column?  Does it make sense that these values are the only possible values? Why or why not? 
# 
# **Here you can use one of the functions you used in an earlier question**.

# In[ ]:





# <a id='probability'></a>
# #### Part II - Probability
# 
# Now that you have had a chance to learn more about the dataset, let's look more at how different factors are related to `converting`.
# 
# `a)` What is the probability of an individual converting regardless of the page they receive or the country they are from? Simply, what is the chance of conversion in the dataset?

# In[ ]:





# `b)` Given that an individual was in the `control` group, what is the probability they converted? **This question is completed for you**

# In[ ]:


df.query('group == "control"')['converted'].mean()


# `c)` Given that an individual was in the `treatment` group, what is the probability they converted?

# In[ ]:





# `d)` Do you see evidence that the treatment is related to higher `converted` rates?

# In[ ]:





# `e)` What is the probability that an individual was in the `treatment`?

# In[ ]:





# `f)` What is the probability that an individual was from Canada `CA`?

# In[ ]:





# `g)` Given that an individual was in the `US`, what was the probability that they `converted`? **This question is completed for you**
# 
# $P(\text{converted} == 1|\text{country} ==\text{"US"})$
# 
# 

# In[ ]:


df.query('country == "US"')['converted'].mean()


# `h)` Given that an individual was in the `UK`, what was the probability that they `converted`? 
# 
# $P(\text{converted} == 1|\text{country} ==\text{"UK"})$

# In[ ]:





# `i)` Do you see evidence that the `converted` rate might differ from one country to the next?

# In[ ]:





# `j)` Consider the table below, fill in the conversion rates below to look at how conversion by country and treatment group vary.  The `US` column is done for you, and two methods for calculating the probabilities are shown - **COMPLETE THE REST OF THE TABLE**.  Does it appear that there could be an interaction between how country and treatment impact conversion?
# 
# These two values that are filled in can be written as:
# 
# $P(\text{converted} == 1|(\text{country} ==\text{"US" AND }\text{group} ==\text{"control"})) = 10.7\%$
# 
# $P(\text{converted} == 1|(\text{country} ==\text{"US" AND }\text{group} ==\text{"treatment"})) = 15.8\%$
# 
# |             | US          | UK          | CA          |
# | ----------- | ----------- | ----------- | ----------- |
# | Control     | 10.7%       |  %          |  %          |
# | Treatment   | 15.8%       |  %          |  %          |

# In[ ]:


# Method 1  - explicitly calculate each probability
print(df.query('country == "US" and group == "control" and converted == 1').shape[0]/df.query('country == "US" and group == "control"').shape[0]) 
print(df.query('country == "US" and group == "treatment" and converted == 1').shape[0]/df.query('country == "US" and group == "treatment"').shape[0])


# In[ ]:


# Method 2 - quickly calculate using `groupby`
df.query('country == "US"').groupby('group')['converted'].mean()


# ##### Solution -- Complete the Table Here
# 
# |             | US          | UK          | CA          |
# | ----------- | ----------- | ----------- | ----------- |
# | Control     | 10.7%       |  %          |  %          |
# | Treatment   | 15.8%       |  %          |  %          |

# In[ ]:





# <a id='experimentation'></a>
# ### Part III - Experimentation
# 
# Consider you need to make the decision just based on all the data provided.  If you want to assume that the control page is better unless the treatment page proves to be definitely better at a Type I error rate of 5%, you state your null and alternative hypotheses in terms of **$p_{control}$** and **$p_{treatment}$** as:  
# 
# $H_{0}: p_{control} >= p_{treatment}$
# 
# $H_{1}: p_{control} < p_{treatment}$
# 
# Which is equivalent to:
# 
# $H_{0}: p_{treatment} - p_{control} <= 0$
# 
# $H_{1}: p_{treatment} - p_{control} > 0$
# 
# 
# Where  
# * **$p_{control}$** is the `converted` rate for the control page
# * **$p_{treatment}$** `converted` rate for the treatment page
# 
# **Note for this experiment we are not looking at differences associated with country.**

# Assume under the null hypothesis, $p_{treatment}$ and $p_{control}$ both have "true" success rates equal to the **converted** success rate regardless of page - that is $p_{treatment}$ and $p_{control}$ are equal. Furthermore, assume they are equal to the **converted** rate in `df` regardless of the page. **These are set in the first cell below.**<br><br>
# 
# * Use a sample size for each page equal to the ones in `df`. **These are also set below.**  <br><br>
# 
# * Perform the sampling distribution for the difference in `converted` between the two pages over 500 iterations of calculating an estimate from the null.  <br><br>
# 
# * Use the cells below to provide the necessary parts of this simulation.  
# 
# If this doesn't make complete sense right now, don't worry - you are going to work through the problems below to complete this problem.  You can use **Quiz 4** in the classroom to make sure you are on the right track.<br><br>

# `a)` The **convert rate** for $p_{treatment}$ under the null.  The **convert rate** for $p_{control}$ under the null. The sample size for the `control` and the sample size for the `treatment` are from the original dataset. **All of these values are set below, and set the stage for the simulations you will run for the rest of this section.**

# In[ ]:


p_control_treatment_null  = df['converted'].mean()
n_treatment = df.query('group == "treatment"').shape[0]
n_control = df.query('group == "control"').shape[0]


# `b)` Use the results from part `a)` to simulate `n_treatment` transactions with a convert rate of `p_treatment_null`.  Store these $n_{treatment}$ 1's and 0's in a `list` of **treatment_converted**.  It should look something like the following (the 0's and and 1's **don't** need to be the same): 
# 
# `[0, 0, 1, 1, 0, ....]` 

# In[ ]:


# treatment_converted = 


# `c)` Use the results from part `a)` to simulate `n_control` transactions with a convert rate of `p_control_null`.  Store these $n_{treatment}$ 1's and 0's in a `list` of **control_converted**.  It should look something like the following (the 0's and and 1's **don't** need to be exactly the same): 
# 
# `[0, 0, 1, 1, 0, ....]` 

# In[ ]:


# control_converted = 


# `d)` Find the estimate for $p_{treatment}$ - $p_{control}$ under the null using the simulated values from part `(b)` and `(c)`.

# In[ ]:





# `e)` Simulate 500 $p_{treatment}$ - $p_{control}$ values using this same process as `b)`- `d)` similarly to the one you calculated in parts **a. through g.** above.  Store all 500 values in an numpy array called **p_diffs**.  This array should look similar to the below **(the values will not match AND this will likely take a bit of time to run)**:
# 
# `[0.001, -0.003, 0.002, ...]`

# In[ ]:


p_diffs = []
# for _ in range(500):
    # simulate the treatment and control converted arrays

    # calculate p_treatment and p_control under the null

    # calculate the difference between p_treatment_null and p_control_null

    # add p_diff to the p_diffs array


# `f)` Plot a histogram of the **p_diffs**.  Does this plot look like what you expected?  Use the matching problem in the classroom to assure you fully understand what was computed here.

# In[ ]:


# p_diffs = pd.Series(p_diffs)
# p_diffs.hist(bins=20)


# `g)` What proportion of the **p_diffs** are greater than the difference observed between `treatment` and `control` in `df`?

# In[ ]:





# `h)` In words, explain what you just computed in part `g)`  What is this value called in scientific studies?  What does this value mean in terms of whether or not there is a difference between the new and old pages using our Type I error rate of 0.05?

# **Your Answer Here**

# <a id='finalcheck'></a>
# ## Final Check!
# 
# Congratulations!  You have reached the end of the A/B Test Results project!  You should be very proud of all you have accomplished!
# 
# > **Tip**: Once you are satisfied with your work here, check over your notebook to make sure that it satisfies all the specifications mentioned in the rubric. You should also probably remove all of the "Hints" and "Tips" like this one so that the presentation is as polished as possible.
# 
# 
# <a id='submission'></a>
# ## Submission
# 
# Please follow the directions in the classroom to submit this notebook, as well as your completed slides.
