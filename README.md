# CandlePattern

A small Flask API that serves candlestick pattern data.

## Installation

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Running

Start the API server with:

```bash
python app.py
```

This runs the application on port `5000` by default.

## API Endpoints

- `GET /candle_30m_new` – returns the entire dataset from `candle_30m_new.csv`.
- `GET /Calc` – returns the highest closing price in the dataset.
- `GET /Ratio` – computes the ratio of pattern occurrences. It expects two query parameters:
  - `pattern` – a sequence of digits (e.g. `1110`).
  - `timestamp` – the ending timestamp used for the calculation.

### Example call to `/Ratio`

```bash
curl "http://127.0.0.1:5000/Ratio?pattern=1110&timestamp=1535938200000"
```

The response contains counts of how often the pattern was seen and the ratio of green to red candles.
