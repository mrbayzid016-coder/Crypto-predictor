import pandas as pd

def get_latest_data():
    # Demo data (পরবর্তীতে আসল API connect করা যাবে)
    data = {"close": [100, 102, 101, 105, 107, 110, 108, 111, 115, 117]}
    return pd.DataFrame(data)
