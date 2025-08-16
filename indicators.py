def generate_signals(df):
    df['MA5'] = df['close'].rolling(5).mean()
    df['MA10'] = df['close'].rolling(10).mean()

    if df['MA5'].iloc[-1] > df['MA10'].iloc[-1]:
        return "BUY"
    else:
        return "SELL"
