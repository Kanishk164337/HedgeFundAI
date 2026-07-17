import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st

from core.pipeline import HedgeFundPipeline
from charts.candlestick_chart import CandlestickChart
from portfolio.portfolio_engine import PortfolioEngine

st.set_page_config(
    page_title="HedgeFundAI",
    page_icon="📈",
    layout="wide"
)

st.title("📈 HedgeFundAI")
st.caption("AI-Powered Investment Research Platform")
mode = st.radio(
    "Choose Analysis Mode",
    [
        "Single Stock",
        "Portfolio"
    ],
    horizontal=True
)
if mode == "Single Stock":

    symbol = st.text_input(
        "Enter Stock Symbol",
        value="AAPL"
    )

else:

    portfolio_input = st.text_area(
        "Enter Symbols (comma separated)",
        value="AAPL,MSFT,NVDA"
    )
if st.button("Analyze"):

    if mode == "Single Stock":

        with st.spinner("Analyzing Stock..."):

            pipeline = HedgeFundPipeline()
            result = pipeline.analyze(symbol)

        analysis = result["analysis"]

    else:

        with st.spinner("Analyzing Portfolio..."):

            engine = PortfolioEngine()

            symbols = [
                s.strip().upper()
                for s in portfolio_input.split(",")
                if s.strip()
            ]

            portfolio_results = engine.analyze(symbols)

            st.success("✅ Portfolio Analysis Complete")

            st.subheader("🏆 Portfolio Ranking")

            st.dataframe(
               portfolio_results,
               use_container_width=True
             )

            st.stop()    # ==========================
    # Signal
    # ==========================

    signal = analysis["signal"]

    if signal == "BUY":
        st.success("🟢 BUY")

    elif signal == "HOLD":
        st.warning("🟡 HOLD")

    else:
        st.error("🔴 SELL")

    # ==========================
    # Metrics
    # ==========================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📊 Overall Score",
            round(analysis["overall_score"], 2)
        )

        st.metric(
            "🎯 Confidence",
            f"{analysis['confidence']}%"
        )

    with col2:

        st.metric(
            "📈 Trend",
            analysis["trend"]["score"]
        )

        st.metric(
            "⚡ Momentum",
            analysis["momentum"]["score"]
        )

    with col3:

        st.metric(
            "🌊 Volatility",
            analysis["volatility"]["score"]
        )

        st.metric(
            "📦 Volume",
            analysis["volume"]["score"]
        )

    st.divider()

    # ==========================
    # Price Chart
    # ==========================

    st.subheader("📈 Price Chart")

    chart = CandlestickChart()

    fig = chart.create(
        result["data"],
        result["symbol"]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ==========================
    # AI Report
    # ==========================

    st.subheader("🧠 AI Investment Report")

    st.markdown(result["report"])