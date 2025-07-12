from data_retrieval import get_stockPrice_and_Change, get_historical_data, get_financial_ratios
from finance_utils import dcf
import streamlit as st
import pandas as pd

def main():
    st.title("Stock Valuation Dashboard")
    ticker = st.text_input("Enter Stock Ticker Symbol (e.g. AAPL, TSLA): ")
    if ticker:
        st.header(f"Data for {ticker}")
        price, change = get_stockPrice_and_Change(ticker)
        if price is None:
            st.error("Could not fetch stock price data. Please try again.")
            return
        st.write(f"**Current Price:** ${price:.2f}")
        st.write(f"**Daily Change:** {change:.2f}%")

        hist_data = get_historical_data(ticker, period='5y')
        if hist_data is not None:
            st.line_chart(hist_data['Close'])
        else:
            st.warning('Historical Data not available.')
        
        ratios = get_financial_ratios(ticker)
        if ratios: 
            st.subheader("Key Financial Ratios")
            df_ratios = pd.DataFrame.from_dict(ratios, orient = 'index', columns=['Value'])
            st.table(df_ratios)
        else:
            st.warning("Financial ratios not available.")
        
        fcf = ratios.get("Free Cash Flow") if ratios else None
        if fcf:
            intrinsic_value = dcf(
                FreeCashFlow = fcf,
                growth_rate = 0.05,
                discount_rate = 0.10,
                years = 5,
                terminal_growth = 0.02
            )
            st.subheader("Discounted Cash Flow (DCF) Valuation")
            st.write(f"Estimated Intrinsic Value: ${intrinsic_value:,.2f}")
        else:
            st.info("Free Cash Flow not available, cannot calculate DCF valuation.")



if __name__ == "__main__":
    main()
