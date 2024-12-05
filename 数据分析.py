import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np

# 读取xlsx文件
file_path = 'weather_data.xlsx'  # 请替换为你的xlsx文件路径
df = pd.read_excel(file_path)

# 数据清洗和预处理
# 转换日期列为datetime类型，并设置为索引
df['Date'] = pd.to_datetime(df['Date'].str.replace('年', '-').str.replace('月', '-').str.replace('日', ''), format='%Y-%m-%d')
df.set_index('Date', inplace=True)


# 提取最高气温、最低气温和风力等级
def extract_temp_and_wind(row):
    temp_range_str = str(row['Temp Range'])
    temp_range_clean = temp_range_str.replace('℃', '')  # 移除'℃'
    temp_parts = temp_range_clean.split('/')  # 分割字符串
    high_temp = int(temp_parts[0].strip())  # 使用strip()去除可能的空白字符
    low_temp = int(temp_parts[1].strip())
    try:
        day_wind_speed = int(row['Wind'].split('/')[0].split()[-1].split('-')[0])
    except ValueError:
        day_wind_speed = 0
    try:
        night_wind_speed = int(row['Wind'].split('/')[1].split()[-1].split('-')[0])
    except ValueError:
        night_wind_speed = 0

    return high_temp, low_temp, day_wind_speed, night_wind_speed


df[['High Temp', 'Low Temp', 'Day Wind Speed', 'Night Wind Speed']] = df.apply(extract_temp_and_wind, axis=1, result_type='expand')

# 描述性分析
print(df.describe())

# 气温趋势分析
# 白天最高气温趋势分析
plt.figure(figsize=(14, 5))
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为SimHei（黑体）
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题
plt.plot(df.index, df['High Temp'], marker='o', linestyle='-', color='r', label='日最高气温')
plt.title('日最高气温趋势分析')
plt.xlabel('日期')
plt.ylabel('最高气温 (℃)')
plt.legend()
plt.grid(True)
plt.show()

# 最低气温趋势分析
plt.figure(figsize=(14, 5))
plt.plot(df.index, df['Low Temp'], marker='o', linestyle='-', color='r', label='最低气温')
plt.title('最低气温趋势分析')
plt.xlabel('日期')
plt.ylabel('最低气温 (℃)')
plt.legend()
plt.grid(True)
plt.show()


# 平均气温趋势分析
df['Avg Temp'] = (df['High Temp'] + df['Low Temp']) / 2
plt.figure(figsize=(14, 5))
plt.plot(df.index, df['Avg Temp'], marker='o', linestyle='-', color='g', label='平均气温')
plt.title('平均气温趋势分析')
plt.xlabel('日期')
plt.ylabel('平均气温 (℃)')
plt.legend()
plt.grid(True)
plt.show()

# 年天气种类统计分析
weather_counts = df['Weather'].str.split('/').explode().value_counts()
plt.figure(figsize=(10, 7))
plt.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('年天气状态统计')
plt.show()

# 年白天风力等级折线图
plt.figure(figsize=(14, 5))
plt.plot(df.index, df['Day Wind Speed'], marker='o', linestyle='-', color='purple', label='白天风力等级')
plt.title('年白天风力等级趋势分析')
plt.xlabel('日期')
plt.ylabel('风力等级')
plt.legend()
plt.grid(True)
plt.show()


# 月份与发生3级以上风的关联性分析
windy_days = df[(df['Day Wind Speed'] > 3) | (df['Night Wind Speed'] > 3)]
windy_months = windy_days.resample('ME').size()
print(f"\n发生3级以上风的月份及天数:\n{windy_months}")

# 保定的旅游季节推荐
# 假设适合旅游的条件：白天晴或多云，气温10-25℃，风力小于3级
tourist_days = df[(df['Weather'].str.contains('晴')) &
                  (df['High Temp'].between(10, 25)) &
                  (df['Day Wind Speed'] < 3) &
                  (df['Night Wind Speed'] < 3)]
tourist_months = tourist_days.resample('ME').size()
print(f"\n适合旅游的月份及天数:\n{tourist_months}")
recommended_season = tourist_months.idxmax().month  # 推荐旅游季节（月份）
print(f"\n推荐旅游季节（月份）: {recommended_season}")  # 注意：这里仅根据月份判断，实际应考虑气候特点



most_common_day_wind_direction = df['Wind'].str.split('/').str[0].str.split().str[0].mode()[0]
print(f"\n白天出现次数最多的风向: {most_common_day_wind_direction}")


# 打印气温统计
print("\n气温统计:")
print("最高气温:", df['High Temp'].max())
print("最低气温:", df['Low Temp'].min())
print("平均气温（高温）:", df['High Temp'].mean())
print("平均气温（低温）:", df['Low Temp'].mean())

# 打印风力统计
print("\n风力统计:")
print("最大白天风速:", df['Day Wind Speed'].max())
print("最小夜间风速:", df['Night Wind Speed'].min())
print("平均白天风速:", df['Day Wind Speed'].mean())
print("平均夜间风速:", df['Night Wind Speed'].mean())

# 打印天气统计
print("\n天气统计:")
weather_types_str = ', '.join(weather_counts.index)
print("天气类型:", weather_types_str)
print("\n每种天气的数量:")
print(df['Weather'].str.split('/').explode().value_counts())
