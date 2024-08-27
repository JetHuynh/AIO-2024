# -*- coding: utf-8 -*-
"""ExerciseM03W01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Nt9ynXOhxmaTdXM00O6kEFEwjW_Ygi0f

# A. Data Analysis with IMDB Movie data
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Colab Notebooks/MODULE03/data

#Download IMDB Movie dataset
# Dataset A: https://drive.google.com/file/d/1xaj40SRwgcabIxsV1SeNKv2M4UtI3h80/view?usp=share_link
!gdown 1xaj40SRwgcabIxsV1SeNKv2M4UtI3h80

"""## 1.Read data

"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Colab Notebooks/MODULE03

# Import libraries
import pandas as pd

# Load dataset
dataset_path = 'data/IMDB-Movie-Data.csv'

# Read data from .csv file
data = pd.read_csv(dataset_path)

# Read data with specified explicit index.
# We will use this later in our analysis
data_indexed = pd.read_csv(dataset_path, index_col="Title")

# test - show all
data

# test - with column index
data_indexed

"""## 2.View the data

"""

# Preview top 5 rows using head()
data.head()

# Preview last 5 rows using tail()
data.tail()

"""## 3.Understand some basic information about the data

"""

# Thông tin cơ bản về bảng dữ liệu
data.info()

# Tổng quan thống kê dữ liệu từ dataset
data.describe()

"""## 4.Data Selection – Indexing and Slicing data

"""

# Extract data as series
genre = data['Genre'] # Tách cột Gerne thành một Series
genre

# Extract data as dataframe
genre = data[['Genre']] # Tách cột Gerne thành một DataFrame
genre

# Tách cùng một lúc nhiều cột với nhau, tạo thành một DataFrame
columns = data[['Title','Genre','Actors','Director','Rating']]
columns

# Gán cột Title làm index
data.set_index('Title')

# Gán cột Title làm index sau đó query dòng data có title = 'Suicide Squad'
data.set_index('Title').loc[['Suicide Squad']]

# Tách các dòng thứ 10 đến thứ 15 dùng index sau đó lọc lấy một số cột cần thiêt
data.iloc[10:15][['Title','Rating','Revenue (Millions)']]

"""## 5.Data Selection – Based on Conditional filtering"""

# doanh thu minimum của top 5% các film có doanh thu cao nhất
minrev = data['Revenue (Millions)'].quantile(0.95)
minrev

# Phim với doanh thu cao trong giai đoạn năm 2010-2015
"""
lấy các bộ phim từ 2010 tới 2015,
với rating nhỏ hơn 6.0 nhưng lại có
doanh thu thuộc top 5% trên toàn bộ dataset
"""
data[((data['Year'] >= 2010)
      & (data['Year'] <= 2015))
      & (data['Rating'] < 6.0)
      & (data['Revenue (Millions)'] >= minrev)]

"""## 6.Groupby operations

"""

# Sử dụng groupby để tìm số rating trung bình đạt được của các đạo diễn trong bộ dữ liệu
data.groupby('Director')[['Rating']].mean()

"""## 7.Sorting operation"""

# Sử dụng sort_values để xem 5 đạo diễn có được số Rating trung bình cao nhất
data.groupby('Director')[['Rating']].mean().sort_values(by='Rating', ascending=False).head()

"""## 8.View missing values"""

# To check null values row-wise
# Kiểm tra số lượng các giá trị null có trong từng cột của bảng dữ liệu
data.isnull().sum()

# Show các dòng chứa giá trị null
data[data.isnull().any(axis=1)]

# đếm các dòng chứa giá trị null
data[data.isnull().any(axis=1)].shape[0]

"""## 9.Deal with missing values - Deleting

"""

# Use drop function to drop columns
# Drop cột Metascore (có nhiều giá trị null)
data.drop('Metascore', axis=1).head() # default inplace=False

# loại bỏ giá trị null trong data sau đó show số lượng dòng còn lại
data.dropna().shape[0]

"""##10.Deal with missing values - Filling

"""

# Kiểm tra trước khi gán giá trị - SL các dòng chứa giá trị null
data[data.isnull().any(axis=1)].shape[0]

# Gán giá trị =300 cho các ô có giá trị null
# data.fillna(300)

# Gán giá trị Rev trung bình cho các hàng có Revenue mang giá trị null
data['Revenue (Millions)'].fillna(data['Revenue (Millions)'].mean(), inplace=True)

# Kiểm tra sau khi gán giá trị - SL các dòng chứa giá trị null
data[data.isnull().any(axis=1)].shape[0]

"""## 11.Apply() functions"""

# Classify movies based on ratings
def rating_group(rating):
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'

# Apply function to the DataFrame
# creating a new column in the DataFrame to hold the rating category
data['Rating_category'] = data['Rating'].apply(rating_group)
data[['Title','Director','Rating','Rating_category']].head(10)

"""# B. Data Analysis with Time Series data"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Colab Notebooks/MODULE03/data

# Dataset B: https://drive.google.com/file/d/1AgxgBt8vArpdxheUqGlbZHqDe_Jatmxv/view?usp=share_link
# bộ dữ liệu daily time series của Open Power System Data (OPSD)
!gdown 1AgxgBt8vArpdxheUqGlbZHqDe_Jatmxv

"""##1.Import libraries and read dataset

"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Colab Notebooks/MODULE03

# Import libraries
import pandas as pd
# Display figures inline in Jupyter notebook
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
dataset_path = './data/opsd_germany_daily.csv'

# Read data from .csv file
opsd_daily = pd.read_csv(dataset_path)

print(opsd_daily.shape)
print(opsd_daily.dtypes)
opsd_daily.head(3)

# chọn cột Date làm index cho DataFrame
opsd_daily = opsd_daily.set_index('Date')
opsd_daily.head(3)

# Thực hiện Load lại data & Chỉ định cột Date làm index cho DataFrame ngay lúc load dữ liệu
# Set path
dataset_path = './data/opsd_germany_daily.csv'

# Read data from .csv file
opsd_daily = pd.read_csv(dataset_path, index_col='Date', parse_dates=True)
opsd_daily.head(3)

# Add columns with year , month , and weekday name
# DataFrame với các cột mới: Year, Month, Weekday
opsd_daily['Year'] = opsd_daily.index.year
opsd_daily['Month'] = opsd_daily.index.month
opsd_daily['Weekday Name'] = opsd_daily.index.day_name()

# Display a random sampling of 5 rows
opsd_daily.sample(5, random_state=0)

"""## 2.Time-based indexing

"""

# Lấy các mẫu dữ liệu từ ngày 20/1/2014 đến 22/1/2014
opsd_daily.loc['2014-01-20':'2014-01-22']

# Lấy được toàn bộ các mẫu dữ liệu thuộc "2012-02"
new_opsd_df = opsd_daily.loc['2012-02']
new_opsd_df.head()

"""## 3.Visualizing time series data

"""

# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(11, 4)})
col_to_plot = 'Consumption'
opsd_daily[col_to_plot].plot(linewidth=0.5)

#thêm thông tin title cho chart
plt.ylabel(col_to_plot)
plt.show()

sns.set(rc={'figure.figsize':(11, 4)})
col_to_plot = 'Solar'
opsd_daily[col_to_plot].plot(linewidth=0.5, color='green')
plt.ylabel(col_to_plot)
plt.show()

# Show Đồ thị về mức tiêu thụ điện, sản lượng điện năng từ mặt trời và sản lượng điện năng từ gió
cols_plot = ['Consumption', 'Solar', 'Wind']
axes = opsd_daily[cols_plot].plot(
    marker='.',
    alpha=0.5,
    linestyle='None',
    figsize=(11, 9),
    subplots=True
)
for ax in axes:
    ax.set_ylabel('Daily Totals (GWh)')

plt.show()

"""## 4.Seasonality

"""

# Biểu diễn phân bố của các cột Consumption, Wind, Solar theo Month
fig, axes = plt.subplots(3, 1, figsize=(11, 10), sharex=True)
for name, ax in zip(['Consumption', 'Solar', 'Wind'], axes):
    sns.boxplot(data=opsd_daily, x='Month', y=name, ax=ax)
    ax.set_ylabel('GWh')
    ax.set_title(name)
    # Remove the automatic x-axis label from all but the bottom subplot
    if ax != axes[-1]:
        ax.set_xlabel('')

"""## 5.Frequencies

"""

# lấy tần suất theo ngày từ 10/3/1998 đến 15/3/1998
pd.date_range('1998-03-10', '1998-03-15', freq='D')

# lấy tần suất theo Giờ
pd.date_range('2004-09-20', periods=8, freq='h')

# Lấy dữ liệu của 3 ngày trong bộ dữ liệu gốc làm ví dụ mẫu
# To select an arbitrary sequence of date/time values from a pandas time series,
# we need to use a DatetimeIndex, rather than simply a list of date/time strings
times_sample = pd.to_datetime(['2013-02-03', '2013-02-06', '2013-02-08'])
# Select the specified dates and just the Consumption column
consum_sample = opsd_daily.loc[times_sample, ['Consumption']].copy()
consum_sample

# Thực hiện ffill vào các ngày khác trong phạm vi từ ngày 3/2/2013 đến 8/2/2013
# Convert the data to daily frequency, without filling any missings
consum_freq = consum_sample.asfreq('D')
# Create a column with missings forward filled
consum_freq['Consumption - Forward Fill'] = consum_sample.asfreq('D', method='ffill')
consum_freq

"""## 6.Resampling

"""

# Sử dụng kỹ thuật Resampling để Downsampling - đổi tần số lấy mẫu của bộ dữ liệu từ ngày sang tuần
# Specify the data columns we want to include (i.e. exclude Year , Month , Weekday Name)
data_columns = ['Consumption', 'Wind', 'Solar', 'Wind+Solar']
# Resample to weekly frequency , aggregating with mean
opsd_weekly_mean = opsd_daily[data_columns].resample('W').mean()
opsd_weekly_mean.head(3)

# Kiểm tra số lượng mẫu dữ liệu của bảng dữ liệu mới so với bảng gốc
print('Bảng gốc: ',opsd_daily.shape[0])
print('Bảng mới: ', opsd_weekly_mean.shape[0])

# visualize daily và weekly time series của Solar trong 6 tháng theo ngày & theo tuần
# Start and end of the date range to extract
start, end = '2017-01', '2017-06'
# Plot daily and weekly resampled time series together
fig, ax = plt.subplots()
ax.plot(opsd_daily.loc[start:end, 'Solar'],
marker='.', linestyle='-', linewidth=0.5, label='Daily')
ax.plot(opsd_weekly_mean.loc[start:end, 'Solar'],
marker='o', markersize=8, linestyle='-', label='Weekly Mean Resample')
ax.set_ylabel('Solar Production (GWh)')
ax.legend()
plt.show()

# Annual resampling với bộ dữ liệu hiện tại

# Compute the annual sums, setting the value to NaN for any year which has
# fewer than 360 days of data
opsd_annual = opsd_daily[data_columns].resample('Y').sum(min_count=360)
# The default index of the resampled DataFrame is the last day of each year,
# ('2006-12-31', '2007-12-31', etc.) so to make life easier, set the index
# to the year component
opsd_annual = opsd_annual.set_index(opsd_annual.index.year)
opsd_annual.index.name = 'Year'
# Compute the ratio of Wind+Solar to Consumption
opsd_annual['Wind+Solar/Consumption'] = opsd_annual['Wind+Solar'] / opsd_annual['Consumption']
opsd_annual.tail(3)

# Show Biểu đồ cột biểu thị Solar + Wind đóng góp vào mức tiêu thụ điện năng
# Plot from 2012 onwards, because there is no solar production data in earlier years
ax = opsd_annual.loc[2012:, 'Wind+Solar/Consumption'].plot.bar(color='C0')
ax.set_ylabel('Fraction')
ax.set_ylim(0, 0.3)
ax.set_title('Wind + Solar Share of Annual Electricity Consumption')
plt.xticks(rotation=0)
plt.show()

"""## 7.Rolling windows

"""

# Review datFrame
opsd_daily[data_columns].head(8)

# Rolling windows với chu kỳ 7 ngày
# Compute the centered 7-day rolling mean
opsd_7d = opsd_daily[data_columns].rolling(7, center=True).mean()
opsd_7d.head(10)

"""## 8.Trends"""

# Xu hướng tiêu thụ điện, tuần và năm
import matplotlib.dates as mdates

# The min_periods=360 argument accounts for a few isolated missing days in the
# wind and solar production time series
opsd_365d = opsd_daily[data_columns].rolling(
    window=365,
    center=True,
    min_periods=360
).mean()

# Plot daily, 7-day rolling mean, and 365-day rolling mean time series
fig, ax = plt.subplots()
ax.plot(opsd_daily['Consumption'], marker='.', markersize=2, color='0.6',
linestyle='None', label='Daily')
ax.plot(opsd_7d['Consumption'], linewidth=2, label='7-d Rolling Mean')
ax.plot(opsd_365d['Consumption'], color='0.2', linewidth=3,
label='Trend (365-d Rolling Mean)')
# Set x-ticks to yearly interval and add legend and labels
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Consumption (GWh)')
ax.set_title('Trends in Electricity Consumption')
plt.show()

# Xu hướng sản xuất năng lượng điện gió và mặt trời qua hằng năm
# Plot 365-day rolling mean time series of wind and solar power
fig, ax = plt.subplots()
for nm in ['Wind', 'Solar', 'Wind+Solar']:
    ax.plot(opsd_365d[nm], label=nm)
    # Set x-ticks to yearly interval, adjust y-axis limits, add legend and labels
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.set_ylim(0, 400)
    ax.legend()
    ax.set_ylabel('Production (GWh)')
    ax.set_title('Trends in Electricity Production (365-d Rolling Means)')
plt.show()