---
Title: How we calculdate XLM 30 Volality and how it can be used in Option pricing
Date: 2024-06-21T14:02:16Z
Tags: oracle
Category: oracle
Slug: xlm-volatility-pricing
Authors: anthony
Summary: XLM Volatility pricing - how we canculate it and why it is important.
Thumbnail: vol-image.jpg
---


In Aristotle's "Politics", Thales of Miletus, a philosopher and mathematician from the 6th century BCE, used options to secure a low price for the use of olive presses before the harvest. Thales predicted a good harvest for olives, so he paid a deposit to secure the rights to use olive presses at a later date. When the harvest was indeed bountiful, the demand for olive presses surged, and Thales was able to rent out his rights at a much higher price than he paid, thus making a profit.

This example illustrates the core principles of options trading: the right, but not the obligation, to buy or sell an asset at a predetermined price within a specified period.

Options and futures are core to international trade in modern economies. All major companies in OECD countries use them to manage risk. One of the keys in making XLM more useful is to provide tools to reduce risk surrounding the use of crypto currencies. Major crypto such as BTC and ETH already have this calculation available from a couple of sources.

Below are the details of how and we calculate the volatility and why it may be useful for calculating option pricing.

# README for vol-function.py

## Overview

The script is designed to calculate the volatility of a cryptocurrency coin over a specified number of days, defaulting to 30 days. This calculation is particularly tailored for the Stellar Lumens (XLM) coin but can be adapted for any cryptocurrency (available on CoinMarketCap through CmcScraper) by changing the coin_code parameter. The script utilizes the CoinMarketCap (CMC) scraper to fetch historical price data, from which it computes the daily returns and their standard deviation as a measure of volatility. This volatility is then annualized, a common practice in financial analysis, especially when preparing inputs for models like the Black-Scholes formula. In the future we will probably switch the daily rates to use the one internal to LightEcho daily rate.

## Why Calculate Volatility This Way?

### Log Returns

The script calculates daily returns using logarithmic returns and are preferred in financial calculations for a number of reasons:

- **Normalization**: Log returns are more normalized (i.e., they are more likely to follow a normal distribution), which is an assumption in many financial models.
- **Small Price Changes**: For small price changes, log returns are approximately equal to the percentage change, making them intuitive to use and interpret.

### Annualizing Volatility

Annualizing the volatility involves scaling the standard deviation of the log returns by the square root of the number of trading days in a year divided by the time horizon of the input data. This is done because Black-Scholes requires annualized volatility.

The formula used is:

- **Volatility * sqrt(365/days)**

It's a standard practice in the market for annualizing volatility.

## How It Works

1. **Date Handling**: The script calculates the start date by subtracting the specified number of days (plus one to include the start day in the count) from the current date. Both dates are formatted as strings for the CMC scraper.

2. **Data Retrieval**: Using the CmcScraper, historical price data for the specified coin between the start and current dates is fetched.

3. **Volatility Calculation**:
    - The closing prices are converted to floats.
    - Daily log returns are calculated.
    - The standard deviation (std) of these log returns is computed over the specified window (default 30 days), representing the volatility.
    - This volatility is then annualized by multiplying it by the square root of (365/days used in calculation), making it suitable for use in annualized financial models. 365 is used since crypto exchanges are live 24/7.

4. **Output**: The script returns a dictionary containing the annualized volatility along with other metadata related to the calculation.

