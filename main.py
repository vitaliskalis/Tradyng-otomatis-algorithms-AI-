"""
Main entry point untuk Tradyng Bot
Jalankan dengan: python main.py
"""

import os
import sys
import time
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from config import settings
from utils.logger import trading_logger, error_logger

def main():
    """Main function"""
    
    try:
        print("\n" + "="*60)
        print("🤖 TRADYNG OTOMATIS ALGORITHMS AI - STARTING")
        print("="*60 + "\n")
        
        # Print configuration
        settings.print_config()
        
        # Check API credentials
        if not settings.BINANCE_API_KEY or not settings.BINANCE_SECRET_KEY:
            raise ValueError("❌ Binance API credentials tidak ditemukan di .env file!")
        
        trading_logger.info("✅ Bot starting...")
        trading_logger.info(f"📊 Trading pair: {settings.TRADING_PAIR}")
        trading_logger.info(f"⏱️  Interval: {settings.TRADING_INTERVAL}")
        trading_logger.info(f"💰 Initial investment: {settings.INITIAL_INVESTMENT} USDT")
        
        # ========================================
        # IMPORT MODULES (akan dibuat di tahap berikutnya)
        # ========================================
        
        # from bot.trader import AutomatedTrader
        # from data.fetcher import DataFetcher
        # from analysis.technical import TechnicalAnalysis
        
        print("\n✅ Configuration loaded successfully!")
        print("\n📝 Next steps:")
        print("   1. Update your .env file with Binance API credentials")
        print("   2. Run: python main.py")
        print("   3. Bot will start trading automatically\n")
        
        print("="*60)
        print("⏳ Waiting for implementation...")
        print("="*60 + "\n")
        
        # TODO: Implement bot logic
        # Uncomment lines below setelah module selesai dibuat
        
        # # Initialize components
        # trader = AutomatedTrader(
        #     api_key=settings.BINANCE_API_KEY,
        #     api_secret=settings.BINANCE_SECRET_KEY,
        #     pair=settings.TRADING_PAIR,
        #     interval=settings.TRADING_INTERVAL
        # )
        
        # # Start trading
        # trader.start()
        
        # # Keep bot running
        # try:
        #     while True:
        #         time.sleep(1)
        # except KeyboardInterrupt:
        #     print("\n\n⛔ Bot stopped by user")
        #     trader.stop()
        #     trading_logger.info("Bot stopped by user")
        
    except KeyboardInterrupt:
        print("\n\n⛔ Bot interrupted by user")
        trading_logger.info("Bot interrupted by user")
        sys.exit(0)
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        error_logger.error(f"Fatal error in main: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
