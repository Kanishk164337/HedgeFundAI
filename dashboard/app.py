import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st

from core.pipeline import HedgeFundPipeline
from charts.candlestick_chart import CandlestickChart
from portfolio.portfolio_engine import PortfolioEngine

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="HedgeFundAI",
    page_icon="📈",
    layout="wide"
)

# ==========================================================
# Header
# ==========================================================

st.title("📈 HedgeFundAI")
st.caption("AI-Powered Investment Research Platform")

# ==========================================================
# Mode Selection
# ==========================================================

mode = st.radio(
    "Choose Analysis Mode",
    [
        "Single Stock",
        "Portfolio"
    ],
    horizontal=True
)

# ==========================================================
# User Input
# ==========================================================

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

# ==========================================================
# Analyze Button
# ==========================================================

if st.button("Analyze"):

    # ======================================================
    # SINGLE STOCK MODE
    # ======================================================

    if mode == "Single Stock":

        with st.spinner("Analyzing Stock..."):

            pipeline = HedgeFundPipeline()

            result = pipeline.analyze(symbol)

        analysis = result["analysis"]

    # ======================================================
    # PORTFOLIO MODE
    # ======================================================

    else:

        with st.spinner("Analyzing Portfolio..."):

            engine = PortfolioEngine()

            symbols = [
                s.strip().upper()
                for s in portfolio_input.split(",")
                if s.strip()
            ]

            portfolio_results = engine.analyze(symbols)

        # ==================================================
        # Portfolio Statistics
        # ==================================================

        total_stocks = len(portfolio_results)

        avg_score = sum(
            stock["score"]
            for stock in portfolio_results
        ) / total_stocks

        avg_confidence = sum(
            stock["confidence"]
            for stock in portfolio_results
        ) / total_stocks

        best_stock = portfolio_results[0]
        worst_stock = portfolio_results[-1]

        # ==================================================
        # Portfolio Health
        # ==================================================

        if avg_score >= 85:
            health = "🟢 Excellent"

        elif avg_score >= 70:
            health = "🟢 Strong"

        elif avg_score >= 55:
            health = "🟡 Moderate"

        elif avg_score >= 40:
            health = "🟠 Weak"

        else:
            health = "🔴 Poor"

        # ==================================================
        # Signal Counts
        # ==================================================

        buy_count = sum(
            1 for stock in portfolio_results
            if stock["signal"] in ["BUY", "STRONG BUY"]
        )

        hold_count = sum(
            1 for stock in portfolio_results
            if stock["signal"] == "HOLD"
        )

        sell_count = sum(
            1 for stock in portfolio_results
            if stock["signal"] in ["SELL", "STRONG SELL"]
        )

        # ==================================================
        # Portfolio Summary
        # ==================================================

        st.success("✅ Portfolio Analysis Complete")

        st.subheader("📊 Portfolio Summary")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric(
                "Average Score",
                round(avg_score, 2)
            )

        with col2:
            st.metric(
                "Average Confidence",
                f"{round(avg_confidence,1)}%"
            )

        with col3:
            st.metric(
                "Best Stock",
                best_stock["symbol"]
            )

        with col4:
            st.metric(
                "Worst Stock",
                worst_stock["symbol"]
            )

        with col5:
            st.metric(
                "Portfolio Health",
                health
            )

        st.divider()

        # ==================================================
        # Signal Distribution
        # ==================================================

        st.subheader("📌 Signal Distribution")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("🟢 BUY", buy_count)

        with c2:
            st.metric("🟡 HOLD", hold_count)

        with c3:
            st.metric("🔴 SELL", sell_count)

        st.divider()

        # ==================================================
        # Portfolio Ranking
        # ==================================================

        st.subheader("🏆 Portfolio Ranking")

        st.dataframe(
            portfolio_results,
            use_container_width=True
        )

        st.stop()
            # ======================================================
    # SINGLE STOCK DASHBOARD
    # ======================================================

    # ==========================
    # Signal
    # ==========================

    signal = analysis["signal"]

    if signal == "STRONG BUY":
        st.success("🟢 STRONG BUY")

    elif signal == "BUY":
        st.success("🟢 BUY")

    elif signal == "HOLD":
        st.warning("🟡 HOLD")

    elif signal == "SELL":
        st.error("🔴 SELL")

    else:
        st.error("🔴 STRONG SELL")

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
    # AI Investment Report
    # ==========================

    st.subheader("🧠 AI Investment Report")

    st.markdown(result["report"])