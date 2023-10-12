import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Define a common color palette
colors_palette = ['#FF5733', '#33FF57', '#3366FF', '#FF33FF', '#FF5733', '#33FF57', '#3366FF', '#FF33FF', '#FF5733', '#33FF57']

def customize_bar_chart(ax):
    """
    Customize the appearance of a bar chart.

    Args:
        ax (matplotlib.axes.Axes): The axes of the bar chart to be customized.

    Returns:
        None
    """
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    plt.tick_params(left=False, bottom=False)
    ax.tick_params(axis='both')
    plt.xticks(fontsize=8.5, weight='bold', color='#7e807e')
    plt.yticks(fontsize=8.5, weight='bold', color='#7e807e')
    ax.set_xlabel("Years", labelpad=18, size=10, fontfamily="sans", weight="bold")
    ax.xaxis.set_label_coords(x=-0.004, y=-0.087, transform=ax.transAxes)
    ax.set_ylabel("Population in Millions", labelpad=18, size=10, fontfamily="sans", weight="bold")
    ax.yaxis.set_label_coords(x=-0.09, y=0.81, transform=ax.transAxes)
    vals = ax.get_yticks()
    for tick in vals:
        ax.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#c3c9c5', zorder=1)

def generate_bar_chart(labels, values, country):
    """
    Generate a bar chart showing the population of a specific country over the years.

    Args:
        labels (list): A list of years.
        values (list): A list of corresponding population values.
        Country (str): The name of the country.

    Returns:
        None
    """
    plt.rcParams['font.sans-serif'] = ['Lato']
    plt.rcParams['font.weight'] = "medium"
    fig, ax = plt.subplots()
    bars = ax.bar(labels, values, width=0.6, color=colors_palette)    
    min_population = min(values)
    max_population = max(values)    
    plt.suptitle(f"Population between {min(labels)} and {max(labels)}", size=10, fontfamily="sans", color="#5f615f", weight="bold",
                horizontalalignment='left',
                x=0.038,
                y=0.94,
                transform=fig.transFigure)
    plt.title(f"{country}", size=17, weight='bold', fontfamily="serif", color='#000',
              horizontalalignment='left',
              x=0.038,
              y=0.96,
              transform=fig.transFigure)
    ax.set_xlabel("Years", labelpad=18, size=10, fontfamily="sans", weight="bold")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f'{x/1e6:,.0f} M'))
    ax.set_ylabel("Population", labelpad=18, size=10, fontfamily="sans", weight="bold")
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height/1e6:,.0f} M', ha='center', va='bottom', fontsize=8, fontweight='bold')        
    customize_bar_chart(ax)
    plt.savefig('./app/img/bar_'+ country + '.png')
    plt.close()

def generate_pie_chart(labels, values, continent, top_n=5):
    """
    Generate a pie chart showing the top N values from a list.

    Args:
        labels (list): A list of labels for the pie chart.
        values (list): A list of values corresponding to each label.
        continent (str): The name of the continent.
        top_n (int): The number of top values to include in the chart.

    Returns:
        None
    """
    sorted_data = sorted(zip(values, labels), reverse=True)
    top_values, top_labels = zip(*sorted_data[:top_n])
    fig, ax = plt.subplots()
    ax.pie(top_values, labels=top_labels, autopct='%1.1f%%', colors=colors_palette, shadow=True, startangle=140)
    ax.axis('equal')
    plt.title(f"Top {top_n} Population Percentage for {continent}", size=14, weight='bold')
    plt.savefig(f'./app/img/pie_{continent}.png')
    plt.close()