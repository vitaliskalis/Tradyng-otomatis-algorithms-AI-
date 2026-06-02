# Tradyng Otomatis Algorithms AI

Bot trading otomatis menggunakan algoritma machine learning dan AI untuk trading crypto/saham secara otomatis.

## 📋 Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi](#instalasi)
- [Panduan Cepat](#panduan-cepat)
- [Struktur Project](#struktur-project)
- [Cara Kerja Bot](#cara-kerja-bot)
- [Konfigurasi](#konfigurasi)
- [Troubleshooting](#troubleshooting)
- [Berkontribusi](#berkontribusi)

## 🎯 Fitur Utama

- ✅ Analisis teknis otomatis menggunakan AI/ML
- ✅ Support multiple exchange (Binance, Coinbase, dll)
- ✅ Risk management dan stop-loss otomatis
- ✅ Backtesting untuk strategi trading
- ✅ Real-time monitoring dan alerts
- ✅ Dashboard untuk tracking performa

## 📦 Persyaratan Sistem

### Software
- Python 3.8+
- pip (Python package manager)
- Git

### Dependencies
```
requests==2.28.1
python-binance==1.0.17
pandas==1.5.3
numpy==1.24.3
scikit-learn==1.2.2
tensorflow==2.12.0
```

## 🚀 Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/vitaliskalis/Tradyng-otomatis-algorithms-AI-.git
cd Tradyng-otomatis-algorithms-AI-
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Konfigurasi
Buat file `.env` di root directory:
```bash
# Binance API (ambil dari https://www.binance.com/en/user/settings/api-management)
BINANCE_API_KEY=your_api_key_here
BINANCE_SECRET_KEY=your_secret_key_here

# Bot Settings
TRADING_PAIR=BTCUSDT
INTERVAL=1h
INITIAL_INVESTMENT=100
```

## ⚡ Panduan Cepat

### Jalankan Bot
```bash
python main.py
```

### Jalankan Backtesting
```bash
python backtest.py --pair BTCUSDT --interval 1h --start 2023-01-01 --end 2023-12-31
```

### Lihat Dashboard
```bash
python app.py
# Buka browser ke http://localhost:5000
```

## 📁 Struktur Project

```
Tradyng-otomatis-algorithms-AI-/
│
├── README.md                 # File ini
├── requirements.txt          # Dependencies
├── .env.example              # Template environment variables
├── main.py                   # Entry point bot trading
│
├── config/
│   ├── __init__.py
│   ├── settings.py           # Konfigurasi utama
│   └── api_keys.py           # API credentials
│
├── bot/
│   ├── __init__.py
│   ├── trader.py             # Core bot logic
│   ├── strategies.py         # Strategi trading
│   └── ml_model.py           # Model machine learning
│
├── analysis/
│   ├── __init__.py
│   ├── technical.py          # Analisis teknis
│   ├── sentiment.py          # Sentiment analysis
│   └── predictor.py          # Price prediction
│
├── data/
│   ├── __init__.py
│   ├── fetcher.py            # Ambil data dari API
│   ├── preprocessor.py       # Pre-process data
│   └── storage.py            # Simpan data
│
├── utils/
│   ├── __init__.py
│   ├── logger.py             # Logging system
│   ├── notifications.py      # Alert & notification
│   └── helpers.py            # Helper functions
│
├── backtest/
│   ├── __init__.py
│   ├── backtester.py         # Engine backtesting
│   ├── metrics.py            # Performance metrics
│   └── visualizer.py         # Chart & grafik
│
├── web/
│   ├── __init__.py
│   ├── app.py                # Flask/Django app
│   ├── routes.py             # API routes
│   └── templates/            # HTML templates
│
├── tests/
│   ├── __init__.py
│   ├── test_bot.py
│   ├── test_strategies.py
│   └── test_ml.py
│
└── models/
    └── trained_model.pkl     # Saved ML model
```

## 🤖 Cara Kerja Bot

### Alur Kerja Utama

```
1. FETCH DATA
   ↓
2. PREPROCESS DATA
   ↓
3. TECHNICAL ANALYSIS
   ↓
4. ML PREDICTION
   ↓
5. GENERATE SIGNAL (BUY/SELL/HOLD)
   ↓
6. RISK MANAGEMENT CHECK
   ↓
7. EXECUTE ORDER (jika sinyal valid)
   ↓
8. MONITOR & LOG
```

### Signal Generation

Bot menghasilkan signal berdasarkan:

- **RSI (Relative Strength Index)**: Oversold/Overbought detection
- **MACD**: Momentum dan trend direction
- **Bollinger Bands**: Volatility dan support/resistance
- **Machine Learning**: Predictive model untuk price movement
- **Sentiment Analysis**: News & social media sentiment

### Risk Management

- Stop-loss otomatis (5-10% dari entry price)
- Take-profit target (10-20% gain)
- Position sizing berdasarkan account balance
- Max daily loss limit
- Portfolio diversification

## ⚙️ Konfigurasi

### File `config/settings.py`

```python
# Trading Settings
TRADING_PAIR = "BTCUSDT"
TRADING_INTERVAL = "1h"  # 5m, 15m, 1h, 4h, 1d
INITIAL_INVESTMENT = 100
MAX_POSITION = 1000

# Risk Management
STOP_LOSS_PERCENT = 5
TAKE_PROFIT_PERCENT = 15
MAX_DAILY_LOSS = 200

# ML Model
MODEL_PATH = "models/trained_model.pkl"
RETRAIN_INTERVAL = 7  # days

# Notifications
TELEGRAM_BOT_TOKEN = "your_token"
TELEGRAM_CHAT_ID = "your_chat_id"
```

### File `.env`

```bash
# Exchange API
BINANCE_API_KEY=xxx
BINANCE_SECRET_KEY=xxx

# Database
DATABASE_URL=sqlite:///trading.db

# Notifications
TELEGRAM_ENABLED=true
TELEGRAM_TOKEN=xxx
EMAIL_ENABLED=false
```

## 📊 Contoh Penggunaan

### Basic Trading

```python
from bot.trader import AutomatedTrader

# Initialize trader
trader = AutomatedTrader(
    pair="BTCUSDT",
    interval="1h"
)

# Start trading
trader.start()

# Monitor status
print(trader.get_status())
```

### Backtesting Strategy

```python
from backtest.backtester import Backtester

bt = Backtester(
    pair="BTCUSDT",
    start_date="2023-01-01",
    end_date="2023-12-31",
    initial_capital=10000
)

# Run backtest
results = bt.run()

# Print metrics
print(f"Total Return: {results['total_return']}%")
print(f"Sharpe Ratio: {results['sharpe_ratio']}")
print(f"Win Rate: {results['win_rate']}%")
```

## 🧠 Melatih Model ML Sendiri

```bash
python train_model.py --pair BTCUSDT --lookback 365 --test-size 0.2
```

## 📈 Monitoring & Logs

Bot akan membuat log file di `logs/` directory:

- `trading.log`: Log transaksi
- `errors.log`: Error dan exception
- `ml.log`: Model training dan prediction logs

View real-time logs:
```bash
tail -f logs/trading.log
```

## ⚠️ Disclaimer & Warning

**PENTING**: Bot ini adalah untuk educational purposes. 

- Trading cryptocurrency SANGAT BERISIKO
- Anda bisa kehilangan seluruh modal
- Selalu gunakan SMALL CAPITAL dulu untuk testing
- JANGAN deploy di production dengan modal besar tanpa testing menyeluruh
- Konsultasi dengan financial advisor sebelum trading

## 🐛 Troubleshooting

### Error: "API Key tidak valid"
- Check file `.env` Anda
- Pastikan API key dan secret sudah benar
- Regenerate API key dari Binance

### Error: "Connection timeout"
- Check internet connection
- Cek apakah API endpoint down
- Coba lagi dalam beberapa saat

### Bot tidak generate signal
- Check data - apakah RSI/MACD calculated?
- Verify trading pair exist
- Check logs di `logs/` directory

### Low Win Rate
- Backtest dengan data lebih banyak
- Adjust parameters (stop-loss, take-profit)
- Train model dengan data terbaru
- Coba strategi berbeda

## 📚 Resource & Learning

### Baca Dokumentasi
- [Binance API Docs](https://binance-docs.github.io/apidocs/)
- [Technical Analysis Guide](https://www.investopedia.com/technical-analysis-4689657)
- [Machine Learning untuk Trading](https://towardsdatascience.com/ml-for-trading)

### YouTube Channel Rekomendasi
- Crypto Trading Tutorials
- ML & AI untuk Finance
- Python untuk Data Science

## 🤝 Berkontribusi

Kami welcome contributions! Silakan:

1. Fork repository ini
2. Buat branch feature (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buka Pull Request

## 📝 License

Project ini di-release under MIT License. Lihat file `LICENSE` untuk details.

## 💬 Support & Contact

- Issues: https://github.com/vitaliskalis/Tradyng-otomatis-algorithms-AI-/issues
- Email: vitaliskalis@email.com
- Telegram: @vitaliskalis

## 🗓️ Roadmap

- [ ] Support lebih banyak exchange
- [ ] Advanced ML models (LSTM, Transformer)
- [ ] Portfolio optimization
- [ ] Advanced risk management
- [ ] Mobile app
- [ ] Cloud deployment guide

---

**Last Updated**: June 2026
**Status**: Under Development 🚀

Jangan lupa star ⭐ repository ini jika membantu!
