class PromptBuilder:

    def build(self, symbol, analysis):

        prompt = f"""
You are an experienced quantitative investment analyst.

Analyze the following technical analysis.

Stock: {symbol}

Trend Analysis:
{analysis["trend"]}

Momentum Analysis:
{analysis["momentum"]}

Volatility Analysis:
{analysis["volatility"]}

Volume Analysis:
{analysis["volume"]}

Overall Score:
{analysis["overall_score"]}

Signal:
{analysis["signal"]}

Confidence:
{analysis["confidence"]}

Write a professional investment report.

Include:

1. Overall Market View
2. Trend Analysis
3. Momentum Analysis
4. Risk Analysis
5. Final Recommendation

Keep the tone professional.
"""

        return prompt