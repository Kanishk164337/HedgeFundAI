import plotly.graph_objects as go


class CandlestickChart:

    def create(self, df, symbol):

        fig = go.Figure()

        # --------------------------
        # Candlestick
        # --------------------------

        fig.add_trace(
            go.Candlestick(
                x=df.index,
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
                name="Price"
            )
        )

        # --------------------------
        # EMA20
        # --------------------------

        if "EMA20" in df.columns:

            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df["EMA20"],
                    mode="lines",
                    name="EMA20",
                    line=dict(width=2)
                )
            )

        # --------------------------
        # EMA50
        # --------------------------

        if "EMA50" in df.columns:

            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df["EMA50"],
                    mode="lines",
                    name="EMA50",
                    line=dict(width=2)
                )
            )

        # --------------------------
        # Bollinger Bands
        # --------------------------

        if (
            "BB_Upper" in df.columns
            and "BB_Middle" in df.columns
            and "BB_Lower" in df.columns
        ):

            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df["BB_Upper"],
                    mode="lines",
                    name="BB Upper",
                    line=dict(width=1, dash="dot")
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df["BB_Middle"],
                    mode="lines",
                    name="BB Middle",
                    line=dict(width=1)
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df["BB_Lower"],
                    mode="lines",
                    name="BB Lower",
                    line=dict(width=1, dash="dot"),
                    fill="tonexty"
                )
            )

        # --------------------------
        # Layout
        # --------------------------

        fig.update_layout(
            title=f"{symbol} Price Chart",
            template="plotly_dark",
            height=700,
            xaxis_title="Date",
            yaxis_title="Price ($)",
            xaxis_rangeslider_visible=False,
            legend=dict(
                orientation="h",
                y=1.02,
                x=0
            )
        )

        return fig