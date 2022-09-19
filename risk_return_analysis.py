#!/usr/bin/env python
# coding: utf-8

# # Analyzing Portfolio Risk and Return
# 
# In this Challenge, you'll assume the role of a quantitative analyst for a FinTech investing platform. This platform aims to offer clients a one-stop online investment solution for their retirement portfolios that’s both inexpensive and high quality. (Think about [Wealthfront](https://www.wealthfront.com/) or [Betterment](https://www.betterment.com/)). To keep the costs low, the firm uses algorithms to build each client's portfolio. The algorithms choose from various investment styles and options.
# 
# You've been tasked with evaluating four new investment options for inclusion in the client portfolios. Legendary fund and hedge-fund managers run all four selections. (People sometimes refer to these managers as **whales**, because of the large amount of money that they manage). You’ll need to determine the fund with the most investment potential based on key risk-management metrics: the daily returns, standard deviations, Sharpe ratios, and betas.
# 
# ## Instructions
# 
# ### Import the Data
# 
# Use the ``risk_return_analysis.ipynb`` file to complete the following steps:
# 
# 1. Import the required libraries and dependencies.
# 
# 2. Use the `read_csv` function and the `Path` module to read the `whale_navs.csv` file into a Pandas DataFrame. Be sure to create a `DateTimeIndex`. Review the first five rows of the DataFrame by using the `head` function.
# 
# 3. Use the Pandas `pct_change` function together with `dropna` to create the daily returns DataFrame. Base this DataFrame on the NAV prices of the four portfolios and on the closing price of the S&P 500 Index. Review the first five rows of the daily returns DataFrame.
# 
# ### Analyze the Performance
# 
# Analyze the data to determine if any of the portfolios outperform the broader stock market, which the S&P 500 represents. To do so, complete the following steps:
# 
# 1. Use the default Pandas `plot` function to visualize the daily return data of the four fund portfolios and the S&P 500. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# 2. Use the Pandas `cumprod` function to calculate the cumulative returns for the four fund portfolios and the S&P 500. Review the last five rows of the cumulative returns DataFrame by using the Pandas `tail` function.
# 
# 3. Use the default Pandas `plot` to visualize the cumulative return values for the four funds and the S&P 500 over time. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# 4. Answer the following question: Based on the cumulative return data and the visualization, do any of the four fund portfolios outperform the S&P 500 Index?
# 
# ### Analyze the Volatility
# 
# Analyze the volatility of each of the four fund portfolios and of the S&P 500 Index by using box plots. To do so, complete the following steps:
# 
# 1. Use the Pandas `plot` function and the `kind="box"` parameter to visualize the daily return data for each of the four portfolios and for the S&P 500 in a box plot. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# 2. Use the Pandas `drop` function to create a new DataFrame that contains the data for just the four fund portfolios by dropping the S&P 500 column. Visualize the daily return data for just the four fund portfolios by using another box plot. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
#     > **Hint** Save this new DataFrame&mdash;the one that contains the data for just the four fund portfolios. You’ll use it throughout the analysis.
# 
# 3. Answer the following question: Based on the box plot visualization of just the four fund portfolios, which fund was the most volatile (with the greatest spread) and which was the least volatile (with the smallest spread)?
# 
# ### Analyze the Risk
# 
# Evaluate the risk profile of each portfolio by using the standard deviation and the beta. To do so, complete the following steps:
# 
# 1. Use the Pandas `std` function to calculate the standard deviation for each of the four portfolios and for the S&P 500. Review the standard deviation calculations, sorted from smallest to largest.
# 
# 2. Calculate the annualized standard deviation for each of the four portfolios and for the S&P 500. To do that, multiply the standard deviation by the square root of the number of trading days. Use 252 for that number.
# 
# 3. Use the daily returns DataFrame and a 21-day rolling window to plot the rolling standard deviations of the four fund portfolios and of the S&P 500 index. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# 4. Use the daily returns DataFrame and a 21-day rolling window to plot the rolling standard deviations of only the four fund portfolios. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# 5. Answer the following three questions:
# 
# * Based on the annualized standard deviation, which portfolios pose more risk than the S&P 500?
# 
# * Based on the rolling metrics, does the risk of each portfolio increase at the same time that the risk of the S&P 500 increases?
# 
# * Based on the rolling standard deviations of only the four fund portfolios, which portfolio poses the most risk? Does this change over time?
# 
# ### Analyze the Risk-Return Profile
# 
# To determine the overall risk of an asset or portfolio, quantitative analysts and investment managers consider not only its risk metrics but also its risk-return profile. After all, if you have two portfolios that each offer a 10% return but one has less risk, you’d probably invest in the smaller-risk portfolio. For this reason, you need to consider the Sharpe ratios for each portfolio. To do so, complete the following steps:
# 
# 1. Use the daily return DataFrame to calculate the annualized average return data for the four fund portfolios and for the S&P 500. Use 252 for the number of trading days. Review the annualized average returns, sorted from lowest to highest.
# 
# 2. Calculate the Sharpe ratios for the four fund portfolios and for the S&P 500. To do that, divide the annualized average return by the annualized standard deviation for each. Review the resulting Sharpe ratios, sorted from lowest to highest.
# 
# 3. Visualize the Sharpe ratios for the four funds and for the S&P 500 in a bar chart. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# 4. Answer the following question: Which of the four portfolios offers the best risk-return profile? Which offers the worst?
# 
# #### Diversify the Portfolio
# 
# Your analysis is nearing completion. Now, you need to evaluate how the portfolios react relative to the broader market. Based on your analysis so far, choose two portfolios that you’re most likely to recommend as investment options. To start your analysis, complete the following step:
# 
# * Use the Pandas `var` function to calculate the variance of the S&P 500 by using a 60-day rolling window. Visualize the last five rows of the variance of the S&P 500.
# 
# Next, for each of the two portfolios that you chose, complete the following steps:
# 
# 1. Using the 60-day rolling window, the daily return data, and the S&P 500 returns, calculate the covariance. Review the last five rows of the covariance of the portfolio.
# 
# 2. Calculate the beta of the portfolio. To do that, divide the covariance of the portfolio by the variance of the S&P 500.
# 
# 3. Use the Pandas `mean` function to calculate the average value of the 60-day rolling beta of the portfolio.
# 
# 4. Plot the 60-day rolling beta. Be sure to include the `title` parameter, and adjust the figure size if necessary.
# 
# Finally, answer the following two questions:
# 
# * Which of the two portfolios seem more sensitive to movements in the S&P 500?
# 
# * Which of the two portfolios do you recommend for inclusion in your firm’s suite of fund offerings?
# 

# ### Import the Data

# #### Step 1: Import the required libraries and dependencies.

# In[ ]:


# Import the required libraries and dependencies

import pandas as pd
import numpy as np
from pathlib import Path


# #### Step 2: Use the `read_csv` function and the `Path` module to read the `whale_navs.csv` file into a Pandas DataFrame. Be sure to create a `DateTimeIndex`. Review the first five rows of the DataFrame by using the `head` function.

# In[ ]:


# Import the data by reading in the CSV file and setting the DatetimeIndex 
# Review the first 5 rows of the DataFrame

whale_navs_prices = pd.read_csv(
    Path("./Resources/whale_navs.csv"), 
    index_col="date", 
    parse_dates=True, 
    infer_datetime_format=True)

display(whale_navs_prices.head())


# #### Step 3: Use the Pandas `pct_change` function together with `dropna` to create the daily returns DataFrame. Base this DataFrame on the NAV prices of the four portfolios and on the closing price of the S&P 500 Index. Review the first five rows of the daily returns DataFrame.

# In[ ]:


# Prepare for the analysis by converting the dataframe of NAVs and prices to daily returns
# Drop any rows with all missing values
# Review the first five rows of the daily returns DataFrame.

whale_navs_daily_returns = whale_navs_prices.pct_change().dropna()

display(whale_navs_daily_returns.head())


# ---

# ## Quantitative Analysis
# 
# The analysis has several components: performance, volatility, risk, risk-return profile, and portfolio diversification. You’ll analyze each component one at a time.

# ###  Analyze the Performance
# 
# Analyze the data to determine if any of the portfolios outperform the broader stock market, which the S&P 500 represents.

# #### Step 1:  Use the default Pandas `plot` function to visualize the daily return data of the four fund portfolios and the S&P 500. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[ ]:


# Plot the daily return data of the 4 funds and the S&P 500 
# Inclue a title parameter and adjust the figure size

whale_navs_daily_returns.plot(
    figsize = (10,7),
    title = "Whale NAVS Fund Portfolio & Market: Daily Returns")


# #### Step 2: Use the Pandas `cumprod` function to calculate the cumulative returns for the four fund portfolios and the S&P 500. Review the last five rows of the cumulative returns DataFrame by using the Pandas `tail` function.

# In[ ]:


# Calculate and plot the cumulative returns of the 4 fund portfolios and the S&P 500
# Review the last 5 rows of the cumulative returns DataFrame

whale_navs_cum_daily_returns = (1 + whale_navs_daily_returns).cumprod() - 1

display(whale_navs_cum_daily_returns.tail())


# #### Step 3: Use the default Pandas `plot` to visualize the cumulative return values for the four funds and the S&P 500 over time. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[ ]:


# Visualize the cumulative returns using the Pandas plot function
# Include a title parameter and adjust the figure size

whale_navs_cum_daily_returns.plot(
    figsize = (10,7),
    title = "Whale NAVS Fund Portfolio & Market: Cumulative Daily Returns")


# #### Step 4: Answer the following question: Based on the cumulative return data and the visualization, do any of the four fund portfolios outperform the S&P 500 Index?

# **Question** Based on the cumulative return data and the visualization, do any of the four fund portfolios outperform the S&P 500 Index?
# 
# **Answer** Up until early 2016, there were short periods of time where some of the funds outperformed the S&P 500.  But from that point forward, the S&P 500 outperformed all (four) funds.

# ---

# ### Analyze the Volatility
# 
# Analyze the volatility of each of the four fund portfolios and of the S&P 500 Index by using box plots.

# #### Step 1: Use the Pandas `plot` function and the `kind="box"` parameter to visualize the daily return data for each of the four portfolios and for the S&P 500 in a box plot. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[ ]:


# Use the daily return data to create box plots to visualize the volatility of the 4 funds and the S&P 500 
# Include a title parameter and adjust the figure size

whale_navs_daily_returns.plot(
    kind = "box",
    figsize = (15,20),
    title = "Whale NAVS Fund Portfolio & Market: Daily Returns Box Plot")


# #### Step 2: Use the Pandas `drop` function to create a new DataFrame that contains the data for just the four fund portfolios by dropping the S&P 500 column. Visualize the daily return data for just the four fund portfolios by using another box plot. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[ ]:


# Create a new DataFrame containing only the 4 fund portfolios by dropping the S&P 500 column from the DataFrame
# Create box plots to reflect the return data for only the 4 fund portfolios
# Include a title parameter and adjust the figure size

whale_navs_daily_returns_funds = whale_navs_daily_returns.drop(columns = "S&P 500")

whale_navs_daily_returns_funds.plot(
    kind = "box",
    figsize = (15,10),
    title = "Whale NAVS Fund Portfolio: Daily Returns Box Plot")


# #### Step 3: Answer the following question: Based on the box plot visualization of just the four fund portfolios, which fund was the most volatile (with the greatest spread) and which was the least volatile (with the smallest spread)?

# **Question** Based on the box plot visualization of just the four fund portfolios, which fund was the most volatile (with the greatest spread) and which was the least volatile (with the smallest spread)?
# 
# **Answer** Most volatile ==> BERKSHIRE HATHAWAY INC; 
#            Least volatile ==> TIGER GLOBAL MANAGEMENT LLC

# ---

# ### Analyze the Risk
# 
# Evaluate the risk profile of each portfolio by using the standard deviation and the beta.

# #### Step 1: Use the Pandas `std` function to calculate the standard deviation for each of the four portfolios and for the S&P 500. Review the standard deviation calculations, sorted from smallest to largest.

# In[ ]:


# Calculate and sort the standard deviation for all 4 portfolios and the S&P 500
# Review the standard deviations sorted smallest to largest

whale_navs_std = whale_navs_daily_returns.std()
whale_navs_std_sorted = whale_navs_std.sort_values()

display(whale_navs_std_sorted)


# #### Step 2: Calculate the annualized standard deviation for each of the four portfolios and for the S&P 500. To do that, multiply the standard deviation by the square root of the number of trading days. Use 252 for that number.

# In[ ]:


# Calculate and sort the annualized standard deviation (252 trading days) of the 4 portfolios and the S&P 500
# Review the annual standard deviations smallest to largest

num_trading_days = 252;
whale_navs_ann_std = whale_navs_std * np.sqrt(num_trading_days)
whale_navs_ann_std_sorted = whale_navs_ann_std.sort_values()

display(whale_navs_ann_std_sorted)


# #### Step 3: Use the daily returns DataFrame and a 21-day rolling window to plot the rolling standard deviations of the four fund portfolios and of the S&P 500 index. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[ ]:


# Using the daily returns DataFrame and a 21-day rolling window, 
# plot the rolling standard deviation of the 4 portfolios and the S&P 500
# Include a title parameter and adjust the figure size

whale_navs_std_rolling21 = whale_navs_daily_returns.rolling(window = 21).std()

whale_navs_std_rolling21.plot(
    figsize = (15,10),
    title = "Whale NAVS Fund Portfolio & Market: Daily Return Standard Deviation w/ Rolling Window = 21")


# #### Step 4: Use the daily returns DataFrame and a 21-day rolling window to plot the rolling standard deviations of only the four fund portfolios. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[ ]:


# Using the daily return data and a 21-day rolling window, plot the rolling standard deviation of just the 4 portfolios. 
# Include a title parameter and adjust the figure size

whale_navs_std_funds_rolling21 = whale_navs_daily_returns_funds.rolling(window = 21).std()

whale_navs_std_funds_rolling21.plot(
    figsize = (15,10),
    title = "Whale NAVS Fund Portfolio: Daily Return Standard Deviation w/ Rolling Window = 21")


# #### Step 5: Answer the following three questions:
# 
# 1. Based on the annualized standard deviation, which portfolios pose more risk than the S&P 500?
# 
# 2. Based on the rolling metrics, does the risk of each portfolio increase at the same time that the risk of the S&P 500 increases?
# 
# 3. Based on the rolling standard deviations of only the four fund portfolios, which portfolio poses the most risk? Does this change over time?

# **Question 1**  Based on the annualized standard deviation, which portfolios pose more risk than the S&P 500?
# 
# **Answer 1** None

# **Question 2** Based on the rolling metrics, does the risk of each portfolio increase at the same time that the risk of the S&P 500 increases?
# 
# **Answer 2** There seems to be some correlation in the direction of the std deviation (i.e. risk) between the funds and the market (s&p500) - although the absolute value of the std deviation (risk) is higher in the market.  The correlation is more prevalent in certain time frames (e.g. beginning of 2020).  It would also be more prevalent if we further smooth out the rolling std window (i.e. increase the # of days in rolling window)
# 

# **Question 3** Based on the rolling standard deviations of only the four fund portfolios, which portfolio poses the most risk? Does this change over time? 
# 
# **Answer 3** Overall, Berkshire Hathaway fund is the most riskiest fund based on rolling std deviation plots. Yes this does change over time.  In early 2015, Berkshire Hathaway and the Soros fund had similar std deviations.  However, in late 2015, Birskhire fund decreased in std deviation whereas the Tiger Global fund spiked in std deviation.  For most of late 2016 to late 2018, the Birkshire fund was clearly the most riskiest fund.  In 2019, the Paulson fund started to spike on par with the Birkshire fund std deviation. And finally in early 2020, all the funds std deviations spike together.

# ---

# ### Analyze the Risk-Return Profile
# 
# To determine the overall risk of an asset or portfolio, quantitative analysts and investment managers consider not only its risk metrics but also its risk-return profile. After all, if you have two portfolios that each offer a 10% return but one has less risk, you’d probably invest in the smaller-risk portfolio. For this reason, you need to consider the Sharpe ratios for each portfolio.

# #### Step 1: Use the daily return DataFrame to calculate the annualized average return data for the four fund portfolios and for the S&P 500. Use 252 for the number of trading days. Review the annualized average returns, sorted from lowest to highest.

# In[ ]:


# Calculate the annual average return data for the for fund portfolios and the S&P 500
# Use 252 as the number of trading days in the year
# Review the annual average returns sorted from lowest to highest

whale_navs_ann_avg_daily_returns = whale_navs_daily_returns.mean() * num_trading_days

display(whale_navs_ann_avg_daily_returns.sort_values())


# #### Step 2: Calculate the Sharpe ratios for the four fund portfolios and for the S&P 500. To do that, divide the annualized average return by the annualized standard deviation for each. Review the resulting Sharpe ratios, sorted from lowest to highest.

# In[ ]:


# Calculate the annualized Sharpe Ratios for each of the 4 portfolios and the S&P 500.
# Review the Sharpe ratios sorted lowest to highest

whale_navs_ann_sharpe_ratio = whale_navs_ann_avg_daily_returns / whale_navs_ann_std

display(whale_navs_ann_sharpe_ratio.sort_values())


# #### Step 3: Visualize the Sharpe ratios for the four funds and for the S&P 500 in a bar chart. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[ ]:


# Visualize the Sharpe ratios as a bar chart
# Include a title parameter and adjust the figure size

whale_navs_ann_sharpe_ratio.plot(
    kind = 'bar',
    figsize = (10,7),
    title = "Whale NAVS Fund Portfolio & Market: Annual Sharpe Ratio")


# #### Step 4: Answer the following question: Which of the four portfolios offers the best risk-return profile? Which offers the worst?

# **Question** Which of the four portfolios offers the best risk-return profile? Which offers the worst?
#     
# **Answer** Best ==> Birkshire Hathaway Fund;
#            Worst ==> Paulson & Co Fund

# ---

# ### Diversify the Portfolio
# 
# Your analysis is nearing completion. Now, you need to evaluate how the portfolios react relative to the broader market. Based on your analysis so far, choose two portfolios that you’re most likely to recommend as investment options.

# #### Use the Pandas `var` function to calculate the variance of the S&P 500 by using a 60-day rolling window. Visualize the last five rows of the variance of the S&P 500.

# In[ ]:


# Calculate the variance of the S&P 500 using a rolling 60-day window.

whale_navs_var_market_rolling60 = whale_navs_daily_returns['S&P 500'].rolling(window = 60).var()

display(whale_navs_var_market_rolling60.tail())


# #### For each of the two portfolios that you chose, complete the following steps:
# 
# 1. Using the 60-day rolling window, the daily return data, and the S&P 500 returns, calculate the covariance. Review the last five rows of the covariance of the portfolio.
# 
# 2. Calculate the beta of the portfolio. To do that, divide the covariance of the portfolio by the variance of the S&P 500.
# 
# 3. Use the Pandas `mean` function to calculate the average value of the 60-day rolling beta of the portfolio.
# 
# 4. Plot the 60-day rolling beta. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# ##### Portfolio 1 - Step 1: Using the 60-day rolling window, the daily return data, and the S&P 500 returns, calculate the covariance. Review the last five rows of the covariance of the portfolio.

# In[ ]:


# Calculate the covariance using a 60-day rolling window 
# Review the last five rows of the covariance data

fund1_selection = "BERKSHIRE HATHAWAY INC"

whale_navs_cov_fund1_mkt_rolling60 = whale_navs_daily_returns_funds[fund1_selection].rolling(window = 60).cov(whale_navs_daily_returns['S&P 500'])

display(whale_navs_cov_fund1_mkt_rolling60.tail())


# ##### Portfolio 1 - Step 2: Calculate the beta of the portfolio. To do that, divide the covariance of the portfolio by the variance of the S&P 500.

# In[ ]:


# Calculate the beta based on the 60-day rolling covariance compared to the market (S&P 500)
# Review the last five rows of the beta information

whale_navs_cov_fund1_mkt_rolling60 = whale_navs_daily_returns_funds[fund1_selection].rolling(window = 60).cov(whale_navs_daily_returns['S&P 500'])
whale_navs_beta_fund1_rolling60 = whale_navs_cov_fund1_mkt_rolling60 / whale_navs_var_market_rolling60

display(whale_navs_beta_fund1_rolling60.tail())


# ##### Portfolio 1 - Step 3: Use the Pandas `mean` function to calculate the average value of the 60-day rolling beta of the portfolio.

# In[ ]:


# Calculate the average of the 60-day rolling beta

whale_navs_beta_fund1_rolling60_mean = whale_navs_beta_fund1_rolling60.mean()

display(whale_navs_beta_fund1_rolling60_mean)


# ##### Portfolio 1 - Step 4: Plot the 60-day rolling beta. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[ ]:


# Plot the rolling beta 
# Include a title parameter and adjust the figure size

whale_navs_beta_fund1_rolling60.plot(
    figsize = (15,10),
    title = f"Whale NAVS Fund {fund1_selection}: Beta w/ Rolling Window = 60")


# ##### Portfolio 2 - Step 1: Using the 60-day rolling window, the daily return data, and the S&P 500 returns, calculate the covariance. Review the last five rows of the covariance of the portfolio.

# In[ ]:


# Calculate the covariance using a 60-day rolling window 
# Review the last five rows of the covariance data

fund2_selection = "TIGER GLOBAL MANAGEMENT LLC"

whale_navs_cov_fund2_mkt_rolling60 = whale_navs_daily_returns_funds[fund2_selection].rolling(window = 60).cov(whale_navs_daily_returns['S&P 500'])

display(whale_navs_cov_fund2_mkt_rolling60.tail())


# ##### Portfolio 2 - Step 2: Calculate the beta of the portfolio. To do that, divide the covariance of the portfolio by the variance of the S&P 500.

# In[ ]:


# Calculate the beta based on the 60-day rolling covariance compared to the market (S&P 500)
# Review the last five rows of the beta information

whale_navs_cov_fund2_mkt_rolling60 = whale_navs_daily_returns_funds[fund2_selection].rolling(window = 60).cov(whale_navs_daily_returns['S&P 500'])
whale_navs_beta_fund2_rolling60 = whale_navs_cov_fund2_mkt_rolling60 / whale_navs_var_market_rolling60

display(whale_navs_beta_fund2_rolling60.tail())


# ##### Portfolio 2 - Step 3: Use the Pandas `mean` function to calculate the average value of the 60-day rolling beta of the portfolio.

# In[ ]:


# Calculate the average of the 60-day rolling beta

whale_navs_beta_fund2_rolling60_mean = whale_navs_beta_fund2_rolling60.mean()

display(whale_navs_beta_fund2_rolling60_mean)


# ##### Portfolio 2 - Step 4: Plot the 60-day rolling beta. Be sure to include the `title` parameter, and adjust the figure size if necessary.

# In[ ]:


# Plot the rolling beta 
# Include a title parameter and adjust the figure size

whale_navs_beta_fund2_rolling60.plot(
    figsize = (15,10),
    title = f"Whale NAVS Fund {fund2_selection}: Beta w/ Rolling Window = 60")


# -
# -
# ***EXTRA: ANALYZING ALL PORTFOLIOS (4 FUNDS) AT THE SAME TIME***
# -
# -

# Portfolio ALL - Step 1: Using the 60-day rolling window, the daily return data, and the S&P 500 returns, calculate the covariance. Review the last five rows of the covariance of the portfolio.

# In[ ]:


# Calculate the covariance using a 60-day rolling window 
# Review the last five rows of the covariance data

whale_navs_cov_funds_mkt_rolling60 = whale_navs_daily_returns_funds.rolling(window = 60).cov(whale_navs_daily_returns['S&P 500'])
display(whale_navs_cov_funds_mkt_rolling60.tail())


# Portfolio ALL - Step 2: Calculate the beta of the portfolio. To do that, divide the covariance of the portfolio by the variance of the S&P 500.

# In[ ]:


# Calculate the beta based on the 60-day rolling covariance compared to the market (S&P 500)
# Review the last five rows of the beta information

# Create an empty dataframe to hold the resultant rolling betas
whale_navs_beta_funds_rolling60 = pd.DataFrame()
# Loop through the covariance dataframe, extract the fund name (column) and covariance data values
#    and compute the rolling beta, and finally concatenate it to the resultant beta dataframe
for (fund_name, fund_prices) in whale_navs_cov_funds_mkt_rolling60.iteritems():
    whale_navs_beta_fund_rolling60 = fund_prices / whale_navs_var_market_rolling60
    whale_navs_beta_funds_rolling60 = pd.concat([whale_navs_beta_funds_rolling60, 
                                                 pd.DataFrame({fund_name: whale_navs_beta_fund_rolling60})], axis="columns")
display(whale_navs_beta_funds_rolling60.tail())


# Portfolio ALL - Step 3: Use the Pandas mean function to calculate the average value of the 60-day rolling beta of the portfolio.

# In[ ]:


# Calculate the average of the 60-day rolling beta

whale_navs_beta_funds_rolling60_mean = whale_navs_beta_funds_rolling60.mean()
display(whale_navs_beta_funds_rolling60_mean)


# Portfolio ALL - Step 4: Plot the 60-day rolling beta. Be sure to include the title parameter, and adjust the figure size if necessary.

# In[ ]:


# Plot the rolling beta 
# Include a title parameter and adjust the figure size

whale_navs_beta_funds_rolling60.plot(
    figsize = (15,10),
    title = "Whale NAVS Fund Portfolio: Beta w/ Rolling Window = 60")


# Answer the following two questions:
# Which of the two portfolios seem more sensitive to movements in the S&P 500?
# 
# Which of the two portfolios do you recommend for inclusion in your firm’s suite of fund offerings?
# 
# Question 1 Which of the two portfolios seem more sensitive to movements in the S&P 500?
# 
# Answer 1 # fund1_selection = "BERKSHIRE HATHAWAY INC"
# 
# Question 2 Which of the two portfolios do you recommend for inclusion in your firm’s suite of fund offerings?
# 
# Answer 2 # fund1_selection = "BERKSHIRE HATHAWAY INC"

# ---
