<----------------Stock Valuation Dashboard---------------->

An interactive dashboard built with Python and Streamlit that allows users to retrieve financial metrics and get an estimate of the intrinsic value using Discounted Cash Flow valuation for public companies.

~ Features

- Enter a stock ticker (e.g., AAPL, TSLA)
- See current stock price and daily % change
- View 5-year historical price chart
- Display key financial ratios:
  - PE Ratio, EV/EBITDA, ROE, Debt/Equity, FCF, etc.
- Run a (simplified) DCF valuation based on real Free Cash Flow

~ Tech Stack

- **Frontend**: Streamlit
- **Data**: Yahoo Finance API (`yfinance`)
- **Charts**: Streamlit
- **Finance logic**: Custom Python DCF model

~ How to install

1. Clone the repository

   ```bash
   git clone https://github.com/Abdulrahman-Hameedi/stock-dashboard.git
   cd stock-dashboard

2. Install dependencies
    ```bash
    pip install -r requirements.txt

3. Run streamlit
    ```bash
    streamlit run dashboard.py
