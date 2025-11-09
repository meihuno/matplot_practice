import pandas as pd
import matplotlib.pyplot as plt

def plot_timeseries(filename, aggregate='daily'):
    """
    aggregate: 'daily', 'monthly', or 'yearly'
    """

    # --- 1. データ読み込み（スペース区切り） ---
    df = pd.read_csv(filename, delim_whitespace=True)

    # --- 2. 日付変換 ---
    df['date'] = pd.to_datetime(df['date'], format='%Y.%m.%d')

    # --- 3. 同日データを集約（sum） ---
    df = df.groupby('date', as_index=False).sum()

    # --- 4. 集約単位変更 ---
    if aggregate == 'monthly':
        df = df.resample('M', on='date').sum().reset_index()
    elif aggregate == 'yearly':
        df = df.resample('Y', on='date').sum().reset_index()

    # --- 5. グラフ描画 ---
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['func'], marker='o', label='func')
    plt.plot(df['date'], df['specc'], marker='s', label='spec')
    plt.plot(df['date'], df['mod'], marker='^', label='mod')

    plt.title(f'Time Series of func / spec / mod ({aggregate})')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # --- 使用例 ---
    # ファイル名を適宜変更してください
    filename = "tmp.txt"

    # デイリー集計
    # plot_timeseries(filename, 'daily')

    # 月次集計
    plot_timeseries(filename, 'monthly')

    # 年次集計
    # plot_timeseries(filename, 'yearly')

