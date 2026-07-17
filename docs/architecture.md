# HedgeFundAI Architecture

## High Level Architecture

```
                 User
                   │
                   ▼
           Streamlit Dashboard
                   │
                   ▼
          HedgeFundPipeline
                   │
     ┌─────────────┼─────────────┐
     ▼             ▼             ▼
 Market       Indicators     Analysis
                   │             │
                   ▼             ▼
               AI Decision Engine
                   │
                   ▼
                Dashboard
```

---

## Project Modules

### market/

Responsible for market data collection.

Current Providers

- Alpha Vantage
- Yahoo Finance
- Binance

---

### indicators/

Responsible for technical indicators.

Modules

- Trend
- Momentum
- Volatility
- Volume

---

### analysis/

Scores every indicator.

Produces

- Trend Score
- Momentum Score
- Volatility Score
- Volume Score
- Overall Score

---

### ai/

LLM integration.

Provider

Groq

Model

Llama 3.3 70B

---

### portfolio/

Portfolio analysis.

Current Features

- Ranking
- Multi-stock analysis

Upcoming

- Risk
- Correlation
- Allocation

---

### dashboard/

Streamlit UI.

Current

- Single Stock
- Portfolio

Upcoming

- News
- Risk Dashboard
- AI Chat
```