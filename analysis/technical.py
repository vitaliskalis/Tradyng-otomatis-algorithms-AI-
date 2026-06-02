"""
Technical Analysis Indicators
RSI, MACD, Bollinger Bands, Moving Averages
"""

import pandas as pd
import numpy as np
from typing import Tuple, Dict
from utils.logger import trading_logger, error_logger

class TechnicalAnalysis:
    """Technical analysis indicators"""
    
    @staticmethod
    def calculate_rsi(data: pd.DataFrame, period: int = 14, column: str = 'close') -> pd.Series:
        """
        Calculate Relative Strength Index (RSI)
        
        Args:
            data: DataFrame dengan price data
            period: RSI period (default 14)
            column: Column name untuk calculate (default 'close')
            
        Returns:
            Series dengan RSI values
        """
        try:
            delta = data[column].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
            
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            
            return rsi
            
        except Exception as e:
            error_logger.error(f"Error calculating RSI: {str(e)}")
            return pd.Series()
    
    @staticmethod
    def calculate_macd(data: pd.DataFrame, 
                      fast: int = 12, 
                      slow: int = 26, 
                      signal: int = 9,
                      column: str = 'close') -> Tuple[pd.Series, pd.Series, pd.Series]:
        """
        Calculate MACD (Moving Average Convergence Divergence)
        
        Args:
            data: DataFrame dengan price data
            fast: Fast EMA period
            slow: Slow EMA period
            signal: Signal line period
            column: Column name
            
        Returns:
            Tuple (MACD line, Signal line, Histogram)
        """
        try:
            ema_fast = data[column].ewm(span=fast).mean()
            ema_slow = data[column].ewm(span=slow).mean()
            
            macd_line = ema_fast - ema_slow
            signal_line = macd_line.ewm(span=signal).mean()
            histogram = macd_line - signal_line
            
            return macd_line, signal_line, histogram
            
        except Exception as e:
            error_logger.error(f"Error calculating MACD: {str(e)}")
            return pd.Series(), pd.Series(), pd.Series()
    
    @staticmethod
    def calculate_bollinger_bands(data: pd.DataFrame,
                                 period: int = 20,
                                 std_dev: float = 2.0,
                                 column: str = 'close') -> Tuple[pd.Series, pd.Series, pd.Series]:
        """
        Calculate Bollinger Bands
        
        Args:
            data: DataFrame dengan price data
            period: SMA period
            std_dev: Standard deviation multiplier
            column: Column name
            
        Returns:
            Tuple (Upper band, Middle band, Lower band)
        """
        try:
            sma = data[column].rolling(window=period).mean()
            std = data[column].rolling(window=period).std()
            
            upper_band = sma + (std * std_dev)
            lower_band = sma - (std * std_dev)
            
            return upper_band, sma, lower_band
            
        except Exception as e:
            error_logger.error(f"Error calculating Bollinger Bands: {str(e)}")
            return pd.Series(), pd.Series(), pd.Series()
    
    @staticmethod
    def calculate_sma(data: pd.DataFrame, period: int, column: str = 'close') -> pd.Series:
        """
        Calculate Simple Moving Average
        
        Args:
            data: DataFrame
            period: Period
            column: Column name
            
        Returns:
            Series dengan SMA values
        """
        try:
            return data[column].rolling(window=period).mean()
        except Exception as e:
            error_logger.error(f"Error calculating SMA: {str(e)}")
            return pd.Series()
    
    @staticmethod
    def calculate_ema(data: pd.DataFrame, period: int, column: str = 'close') -> pd.Series:
        """
        Calculate Exponential Moving Average
        
        Args:
            data: DataFrame
            period: Period
            column: Column name
            
        Returns:
            Series dengan EMA values
        """
        try:
            return data[column].ewm(span=period).mean()
        except Exception as e:
            error_logger.error(f"Error calculating EMA: {str(e)}")
            return pd.Series()
    
    @staticmethod
    def calculate_atr(data: pd.DataFrame, period: int = 14) -> pd.Series:
        """
        Calculate Average True Range
        
        Args:
            data: DataFrame dengan OHLC data
            period: Period
            
        Returns:
            Series dengan ATR values
        """
        try:
            high = data['high']
            low = data['low']
            close = data['close']
            
            tr1 = high - low
            tr2 = abs(high - close.shift())
            tr3 = abs(low - close.shift())
            
            tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
            atr = tr.rolling(window=period).mean()
            
            return atr
            
        except Exception as e:
            error_logger.error(f"Error calculating ATR: {str(e)}")
            return pd.Series()
    
    @staticmethod
    def calculate_roc(data: pd.DataFrame, period: int = 12, column: str = 'close') -> pd.Series:
        """
        Calculate Rate of Change
        
        Args:
            data: DataFrame
            period: Period
            column: Column name
            
        Returns:
            Series dengan ROC values
        """
        try:
            roc = ((data[column] - data[column].shift(period)) / data[column].shift(period)) * 100
            return roc
        except Exception as e:
            error_logger.error(f"Error calculating ROC: {str(e)}")
            return pd.Series()
    
    @staticmethod
    def calculate_stochastic(data: pd.DataFrame, 
                           period: int = 14,
                           smooth_k: int = 3,
                           smooth_d: int = 3) -> Tuple[pd.Series, pd.Series]:
        """
        Calculate Stochastic Oscillator
        
        Args:
            data: DataFrame dengan OHLC data
            period: Lookback period
            smooth_k: K smoothing period
            smooth_d: D smoothing period
            
        Returns:
            Tuple (K line, D line)
        """
        try:
            low_min = data['low'].rolling(window=period).min()
            high_max = data['high'].rolling(window=period).max()
            
            k = 100 * ((data['close'] - low_min) / (high_max - low_min))
            k_smooth = k.rolling(window=smooth_k).mean()
            d_smooth = k_smooth.rolling(window=smooth_d).mean()
            
            return k_smooth, d_smooth
            
        except Exception as e:
            error_logger.error(f"Error calculating Stochastic: {str(e)}")
            return pd.Series(), pd.Series()

class SignalGenerator:
    """Generate trading signals berdasarkan indicators"""
    
    @staticmethod
    def generate_rsi_signal(data: pd.DataFrame, 
                          rsi_period: int = 14,
                          oversold: float = 30,
                          overbought: float = 70) -> Dict:
        """
        Generate signal berdasarkan RSI
        
        Args:
            data: DataFrame
            rsi_period: RSI period
            oversold: Oversold threshold
            overbought: Overbought threshold
            
        Returns:
            Dict dengan signal
        """
        try:
            rsi = TechnicalAnalysis.calculate_rsi(data, rsi_period)
            current_rsi = rsi.iloc[-1]
            
            signal = "HOLD"
            confidence = 0.5
            
            if current_rsi < oversold:
                signal = "BUY"
                confidence = (oversold - current_rsi) / oversold
            elif current_rsi > overbought:
                signal = "SELL"
                confidence = (current_rsi - overbought) / (100 - overbought)
            
            return {
                "signal": signal,
                "confidence": confidence,
                "rsi": current_rsi,
                "reason": f"RSI: {current_rsi:.2f}"
            }
            
        except Exception as e:
            error_logger.error(f"Error generating RSI signal: {str(e)}")
            return {"signal": "HOLD", "confidence": 0}
    
    @staticmethod
    def generate_macd_signal(data: pd.DataFrame,
                           fast: int = 12,
                           slow: int = 26,
                           signal: int = 9) -> Dict:
        """
        Generate signal berdasarkan MACD
        
        Args:
            data: DataFrame
            fast: Fast EMA period
            slow: Slow EMA period
            signal: Signal period
            
        Returns:
            Dict dengan signal
        """
        try:
            macd_line, signal_line, histogram = TechnicalAnalysis.calculate_macd(
                data, fast, slow, signal
            )
            
            current_macd = macd_line.iloc[-1]
            current_signal = signal_line.iloc[-1]
            current_histogram = histogram.iloc[-1]
            prev_histogram = histogram.iloc[-2]
            
            signal_type = "HOLD"
            confidence = 0.5
            
            # Bullish crossover
            if prev_histogram < 0 and current_histogram > 0:
                signal_type = "BUY"
                confidence = 0.7
            # Bearish crossover
            elif prev_histogram > 0 and current_histogram < 0:
                signal_type = "SELL"
                confidence = 0.7
            elif current_histogram > 0:
                signal_type = "BUY"
                confidence = 0.6
            elif current_histogram < 0:
                signal_type = "SELL"
                confidence = 0.6
            
            return {
                "signal": signal_type,
                "confidence": confidence,
                "macd": current_macd,
                "signal_line": current_signal,
                "histogram": current_histogram,
                "reason": f"MACD crossover: {current_macd:.6f}"
            }
            
        except Exception as e:
            error_logger.error(f"Error generating MACD signal: {str(e)}")
            return {"signal": "HOLD", "confidence": 0}
    
    @staticmethod
    def generate_bb_signal(data: pd.DataFrame,
                         period: int = 20,
                         std_dev: float = 2.0) -> Dict:
        """
        Generate signal berdasarkan Bollinger Bands
        
        Args:
            data: DataFrame
            period: BB period
            std_dev: Standard deviation
            
        Returns:
            Dict dengan signal
        """
        try:
            upper, middle, lower = TechnicalAnalysis.calculate_bollinger_bands(
                data, period, std_dev
            )
            
            current_price = data['close'].iloc[-1]
            current_upper = upper.iloc[-1]
            current_lower = lower.iloc[-1]
            current_middle = middle.iloc[-1]
            
            signal_type = "HOLD"
            confidence = 0.5
            
            if current_price < current_lower:
                signal_type = "BUY"
                confidence = 0.65
            elif current_price > current_upper:
                signal_type = "SELL"
                confidence = 0.65
            
            return {
                "signal": signal_type,
                "confidence": confidence,
                "price": current_price,
                "upper": current_upper,
                "middle": current_middle,
                "lower": current_lower,
                "reason": f"Price touches BB: {current_price:.2f}"
            }
            
        except Exception as e:
            error_logger.error(f"Error generating BB signal: {str(e)}")
            return {"signal": "HOLD", "confidence": 0}

if __name__ == "__main__":
    # Test (need real data)
    print("Technical Analysis module loaded successfully")
