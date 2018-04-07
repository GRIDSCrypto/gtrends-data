# ***** Input and output filepaths are hard-coded!!! *****
# All the plotting stuff is commented out, can put it back in if you need a visual 
# sanity check

import pandas as pd
import time
from matplotlib import pyplot

def parser(x): #Parses input timestamp to datetime
	return pd.datetime.strptime(x, '%Y-%m-%d')


def dateformat(x): # Convert datetime back to datestr
    return pd.datetime.strftime(x, '%Y-%m-%d')

def main():
	#Load in csv and parse dates
	btc_gtrends = pd.read_csv('/Users/ADV/GRIDSCrypto/Data/BTC_GoogleTrends.csv',\
	 header=1, parse_dates=[0], index_col=0, date_parser=parser)

	#Plot raw time series
	print("************ Original Weekly Data ************")
	print(btc_gtrends.head(6))
	#btc_gtrends.plot()
	#pyplot.show()

    #Upsample to daily resolution
	upsampled = btc_gtrends.resample('D')
	interpolated = upsampled.interpolate(method='linear')
	print("************ Interpolated Daily Data ************")
	print(interpolated.head(36))
	#interpolated.plot()
	#pyplot.show()

    #Write upsampled data to csv
	fout = open('Data/BTC_GoogleTrends_Daily_test.csv', 'w')
	header = 'Date,BTC Trend\n'
	fout.write(header)
	#for key in headers:
	#	fout.write(key + ',')
	#	fout.write('\n')
	for row in interpolated.iterrows():
		fout.write(dateformat(row[0]) + ',' + "%.2f" % row[1][0] + '\n')


if __name__ == "__main__":
	main()


