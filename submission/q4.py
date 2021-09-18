import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

def plot_graph(file):
    """
    Plotting two different types of graphs.
    
    :param file: To read the command line file path
    :param org_data: to read the csv file for graph 1
    :param groups1: Grouping the data by a values
    :param method_data: to read the csv file for graph 2
    
    :return type: Graph plot
    """
    #parser = argparse.ArgumentParser()
    #parser.add_argument("--data", nargs="+")
    #file = np.loadtxt(parser.parse_args().data[0])
    
    
    plt.figure(figsize = (12,6))
    ax = plt.gca()
    
    org_data = pd.read_csv(file, sep=',')
    org_data = org_data.drop(["Entity"], axis=1)
    org_data = org_data.drop(["Method"], axis=1)
    
    groups1 = org_data.groupby(["Organization type"])
    
    #plot 1st graph
    plt.yscale('log')
    y1 = groups1.get_group('academic')
    y1.groupby('Year')['Records'].mean().plot(ax=ax,label='academic')
    
    y2 = groups1.get_group('financial')
    y2.groupby('Year')['Records'].mean().plot(ax=ax,label='financial')
    
    y3 = groups1.get_group('gaming')
    y3.groupby('Year')['Records'].mean().plot(ax=ax,label='gaming')
    
    y4 = groups1.get_group('government')
    y4.groupby('Year')['Records'].mean().plot(ax=ax,label='government')
    
    y5 = groups1.get_group('healthcare')
    y5.groupby('Year')['Records'].mean().plot(ax=ax,label='healthcare')
    
    y6 = groups1.get_group('military')
    y6.groupby('Year')['Records'].mean().plot(ax=ax,label='military')
    
    y7 = groups1.get_group('retail')
    y7.groupby('Year')['Records'].mean().plot(ax=ax,label='retail')
    
    y8 = groups1.get_group('tech')
    y8.groupby('Year')['Records'].mean().plot(ax=ax,label='tech')
    
    y9 = groups1.get_group('telecoms')
    y9.groupby('Year')['Records'].mean().plot(ax=ax,label='telecoms')
    
    y10 = groups1.get_group('web')
    y10.groupby('Year')['Records'].mean().plot(ax=ax,label='web')
    
    plt.title('Type of organizations affected by Data breaches per year')
    plt.legend(loc='lower right').set_title("Organization type")
    
    plt.savefig('organization.png')
    #plt.show()
    
    
    #Plot 2nd graph
    
    plt.figure(figsize = (12,8))
    method_data = pd.read_csv(file, sep=',')
    plt.yscale("log")
    data = method_data[method_data['Method'].isin(['hacked', 'poor security', 'lost', 'accidentally published', 'inside job'])]
    seaborn.boxplot(x='Year', y='Records', data=data, hue='Method')
    plt.title('Types of Methods used for Data Breaching per year')
    plt.legend(loc='upper left').set_title("Method")
    #plt.show()
    plt.savefig('method.png')

if __name__ == '__main__':
    file = sys.argv[2]
    plot_graph(file)