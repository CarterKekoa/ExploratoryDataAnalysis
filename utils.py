import math 
import numpy as np 
import mypytable 
import os


# PA3 Functions
def table_set(file_name):
    """
    """
    # Set file path
    #filename = "vgsales.csv"
    file_path = os.path.join("input_data", file_name)

    # populate table with data in file
    table = mypytable.MyPyTable().load_from_file(file_path)
    #mypytable.MyPyTable.pretty_print(table)

    return table

def col_barchart_data_plot_prep(column_list):
    """
    """
    x = []
    x_names = []
    y = []
    i = 0

    # separates the lists duplicate values into a dictionary, storing the value and the amount of duplicates
    dups = {i:column_list.count(i) for i in column_list}
    
    # iterates the dictionary and stores values in lists to be used by box plot
    for k,v in dups.items():
        x.append(i)
        x_names.append(str(k))
        y.append(int(v))
        i += 1

    return x, x_names, y


def pie_chart_data_prep(table, cols_to_plot):
    """
    """
    totals_list = []
    for col_name in cols_to_plot:
        column_list = mypytable.MyPyTable.get_column(table, str(col_name))

        total = 0
        for val in column_list:
            total = total + float(val)
        totals_list.append(total)
    return totals_list

def MPG_ratings_Data_Prep(column_list):
    """
    """
    freqs = [0,0,0,0,0,0,0,0,0,0]
    ratings = [1,2,3,4,5,6,7,8,9,10]
    x_names = ["<= 13", "14", "15-16", "17-19", "20-23", "24-26", "27-30", "31-36", "37-44", ">= 45"]

    for val in column_list:
        temp = round(val)
        #print(temp)
        if temp <= 13:
            freqs[0] = freqs[0] + 1
        elif temp == 14:
            freqs[1] = freqs[1] + 1
        elif temp >= 15 and temp <= 16:
            freqs[2] = freqs[2] + 1
        elif temp >= 17 and temp <= 19:
            freqs[3] = freqs[3] + 1
        elif temp >= 20 and temp <= 23:
            freqs[4] = freqs[4] + 1
        elif temp >= 24 and temp <= 26:
            freqs[5] = freqs[5] + 1
        elif temp >= 27 and temp <= 30:
            freqs[6] = freqs[6] + 1
        elif temp >= 31 and temp <= 36:
            freqs[7] = freqs[7] + 1
        elif temp >= 37 and temp <= 44:
            freqs[8] = freqs[8] + 1
        elif temp >= 45:
            freqs[10] = freqs[10] + 1
    #print(freqs)
    return ratings, x_names, freqs

def compute_equal_width_cutoffs(values, num_bins):
    # first compute the range of the values 
    values_range = max(values) - min(values)
    bin_width = values_range / num_bins
    # bin_width is likely a float
    # if your application allows for ints, use them
    # we will use floats
    # np.arrange() is like built in range for floats
    cutoffs = list(np.arange(min(values),  max(values), bin_width)) # (start, stop, step)
    cutoffs.append(max(values)) # explicitly add max since it stops N - 1 above
    # optionally: might want to round
    cutoffs = [round(cutoff, 2) for cutoff in cutoffs]  # (cutoff, 2) specifies amount of decimal points
    return cutoffs

def compute_freq(values, cutoffs):
    bin_freqs = []
    for i in range(len(cutoffs)):
        freq = 0
        for j in range(len(values)):
            if i == (len(cutoffs) - 2):
                if values[j] >= cutoffs[i] and values[j] <= cutoffs[i + 1]:
                    freq += 1
            elif i < (len(cutoffs) - 2):
                if values[j] >= cutoffs[i] and values[j] < cutoffs[i + 1]:
                    freq += 1
        if i != (len(cutoffs) - 1):
            bin_freqs.append(freq)
    return bin_freqs

def scatter_plot_data_prep(table, x, y):
    m, b = compute_slope_intercept(x,y)
    r = np.corrcoef(x,y)
    regression = (r[0][1])
    covar = np.cov(x,y)
    covariance = (covar[0][1])
    return float(m), float(b), float(regression), float(covariance)
    
def compute_slope_intercept(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y) 
    m = sum([(x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))]) \
        / sum([(x[i] - mean_x) ** 2 for i in range(len(x))])
    # y = mx + b => y - mx
    b = mean_y - m * mean_x
    return m, b 

def stripper(column_list, symbol, factor):
    new_list = []
    for col in column_list:
        new_list.append(float(col.strip(symbol))/factor)
    return new_list

def splitter(column_list, symbol):
    new_list = []
    comma_list = []
    for col in column_list:
        temp = col.split(symbol)
        comma_list.append(temp)
        for val in temp:
            new_list.append(val)
    return new_list, comma_list

def multi_boxplot_data_prep(table, list1, list2, column):
    genre_column_list = mypytable.MyPyTable.get_column(table, column)
    no_comma_list, comma_list = splitter(genre_column_list, ',')
    x, x_names, y = col_barchart_data_plot_prep(no_comma_list)

    length = list(range(len(x_names)))
    plot_len = []
    all_genres1 = []
    all_genres2 = []

    # for genre in genre_column_list
    for dup_genre in x_names:
        new_IMDb_genre_list = []
        new_rt_genre_list = []
        for i in range(len(comma_list)):
            for col in comma_list[i]:
                if col == dup_genre:
                    new_IMDb_genre_list.append(float(list1[i]))
                    new_rt_genre_list.append(float(list2[i]))
        
        all_genres1.append(new_IMDb_genre_list)
        all_genres2.append(new_rt_genre_list)
    
    code1 = "plt.boxplot(["
    code2 = "plt.boxplot(["
    for index in length:
        plot_len.append(index + 1)
        if index == (len(length) - 1):
            code1 = code1 + "all_genres1[" + str(index) + "]])"
            code2 = code2 + "all_genres2[" + str(index) + "]])"
        else:
            code1 = code1 + "all_genres1[" + str(index) + "],"
            code2 = code2 + "all_genres2[" + str(index) + "],"
        #plt.boxplot([all_genres[0], all_genres[1], all_genres[2]])

    return code1, code2, all_genres1, all_genres2, x_names