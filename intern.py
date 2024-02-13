import yfinance as yf
import pandas as pd
import numpy as np

# Data Ingestion
def fetch_stock_data(ticker, start_date, end_date):
    # Fetch OHLC data from Yahoo Finance
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Data Cleaning
def clean_data(stock_data):
    # Handle missing values
    stock_data.dropna(inplace=True)
    
    # Detect and correct outliers
    # For simplicity, we'll just remove any outliers in this example
    # Address inconsistencies in timestamps or date formats (if any)
    # Not required here as Yahoo Finance data is typically clean
    
    return stock_data

# Data Transformation
def calculate_technical_indicators(stock_data):
    # Calculate moving averages
    stock_data['MA_50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['MA_200'] = stock_data['Close'].rolling(window=200).mean()
    
    # Calculate Bollinger Bands
    rolling_mean = stock_data['Close'].rolling(window=20).mean()
    rolling_std = stock_data['Close'].rolling(window=20).std()
    stock_data['Upper_Band'] = rolling_mean + (2 * rolling_std)
    stock_data['Lower_Band'] = rolling_mean - (2 * rolling_std)
    
    # Calculate Relative Strength Index (RSI)
    delta = stock_data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    RS = gain / loss
    RSI = 100 - (100 / (1 + RS))
    stock_data['RSI'] = RSI.fillna(0)  # Fill initial NaN values
    
    return stock_data

# Example usage
if __name__ == "__main__":
    # Parameters
    ticker = 'AAPL'  # Example stock ticker
    start_date = '2020-01-01'
    end_date = '2024-01-01'
    
    # Data Ingestion
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    
    # Data Cleaning
    cleaned_data = clean_data(stock_data)
    
    # Data Transformation
    transformed_data = calculate_technical_indicators(cleaned_data)
    
    print(transformed_data.head())
