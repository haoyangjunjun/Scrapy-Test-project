import pandas as pd

# 读取Excel文件
file_path = 'weather_data.xlsx'
df = pd.read_excel(file_path, header=0)  # 列名
df = df.dropna(subset=['Date', 'Weather', 'Temp Range', 'Wind'], how='all')
df['Date'] = pd.to_datetime(df['Date'].str.replace('年', '-').str.replace('月', '-').str.replace('日', ''), format='%Y-%m-%d')
df = df.set_index('Date')
df = df.sort_index()  # 对DataFrame进行排序
# 数据保存回Excel文件


# 打印DataFrame的列名，以便检查
print("DataFrame列名:", df.columns.tolist())
output_file_path = 'weather_data.xlsx'
df.to_excel(output_file_path)  # 如果不重置索引，则不包括index=False
# 如果重置了索引，并且希望日期作为第一列，可以这样做：
# df.to_excel(output_file_path, index=False, columns=['Date', 'Weather', 'Temp Range', 'Wind'])

print("数据已排序并保存到", output_file_path)