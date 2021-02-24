import matplotlib.pyplot as plt

def bar_chart(x, x_names, y, y_title, x_title):
    """
    """
    # Box Plot 
    plt.figure()
    plt.xticks(x, x_names, rotation=90)
    plt.title(x_title + " " + y_title)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.bar(x, y)
    plt.show()

def pie_chart(x_names, y, title):
    """
    """
    plt.figure()
    plt.title(title)
    plt.pie(y, labels=x_names, autopct="%1.1f%%")
    plt.show()

def plot_bar_hist(cutoffs, bin_freqs, y_title, x_title):
    """
    """
    width = round(abs(cutoffs[1] - cutoffs[0]))

    labels = []
    label_locations = []
    for i in range(len(cutoffs)):
        if i > 0:
            labels.append(str(cutoffs[i - 1]) + "-" + str(cutoffs[i]))
            label_locations.append(cutoffs[i - 1])

    plt.title(x_title + " " + y_title)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.xticks(label_locations, labels, rotation=90)

    for j in range(len(bin_freqs)):
        plt.bar(cutoffs[j], bin_freqs[j], width, color='#581845')

def histogram(title, column_list):
    """
    """
    plt.figure()
    plt.title(title + " Histogram")
    plt.hist(column_list)
    plt.show()

def histogram_double(title, column_list1, column_list2):
    """
    """
    plt.figure()
    plt.title(title + " Histogram")
    plt.hist(column_list1, bins=10)
    plt.hist(column_list2, bins=20)
    plt.show()

def scatter_with_linear_regr(x, y, m, b, regression, covariance, y_label, x_label):
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(x_label + " vs " + y_label + ", r = " + str(regression) + ", cov = " + str(covariance))
    plt.plot([min(x), max(x)], [m * min(x) + b, m * max(x) + b], c="r", lw=5)
    plt.show()

def multi_box_wisker(code, tick_names, amt, all_genres1, all_genres2, title):
    plt.figure()
    exec(code)
    plt.title(title)
    plt.xticks(amt, tick_names, rotation=90)
    plt.show()