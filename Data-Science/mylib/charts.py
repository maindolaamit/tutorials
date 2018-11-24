import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def donut(df_col):
    df_count = df_col.str.lower().value_counts()
    # print(f"Number of spams : {df_count[0]} | No. of hams {df_count[1]}")

    fig, ax = plt.subplots()
    colors = ['#66b3ff', '#99ff99', '#ffcc99']
    patches, text, autotext = ax.pie(df_count, labels=df_count.index, autopct='%1.1f%%',
                                     shadow=True, startangle=90)
    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')
    title = f'Distribution of : {df_col.name.upper()}'
    plt.title(title, fontsize=17)
    plt.tight_layout()
    plt.show()


def bi_donut(df_cols, sup_title):
    fig, (ax1, ax2) = plt.subplots(
        ncols=2, figsize=(15, 6), constrained_layout=False)
    columns = df_cols.columns

    for i in range(2):
        ax = ax1 if i == 0 else ax2
        col = columns[i]
        df_col = df_cols[col]
        df_count = df_col.str.upper().value_counts()
        title = f'{df_col.name.upper()}'
        ax.set_title(label=title, ha='center', va='bottom',
                     fontdict={'fontsize': 15}, color='r')
        patches, text, autotext = ax.pie(df_count, labels=df_count.index, autopct='%1.1f%%',
                                         startangle=90)
        # draw circle
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')
        ax.add_artist(centre_circle)
        ax.legend(loc='upper left')

    plt.tight_layout()
    fig.suptitle(sup_title, ha='center', va='bottom', size=18,
                 fontweight='bold', fontdict={'color': 'g'})
    _ = plt.show()

def double_donut(grp_data):
    from matplotlib import cm
    # Create groups and subgroups
    group_names = grp_data.index.levels[0].to_list()
    group_size = [grp_data[name].sum() for name in group_names]
    subgroup_names = [f"{x[1]}" for x in grp_data.index.values]
    subgroup_size = grp_data.values

    # Create colors
    color_pallete = [cm.Blues, cm.Reds, cm.Greens,
                     cm.Oranges, cm.Purples, cm.Greys]

    grp_cmap = {group_names[i]: color_pallete[i]
                for i in range(len(group_names))}

    # Create color pallete for group and subgroups
    grp_colors = [grp_cmap[color](0.8) for color in grp_cmap.keys()]
    subgroup_colors = []
    for grp in grp_cmap.keys():
        variance = np.linspace(.1, .9, grp_data[grp].count())  # Divide based on Sub-group count for a group
        for i in variance:
            subgroup_colors.append(grp_cmap[grp](i))

    # First Ring (outside)
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.axis('equal')
    mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=grp_colors)
    plt.setp(mypie, width=0.3, edgecolor='white')
    # Second Ring (Inside)
    mypie2, _ = ax.pie(subgroup_size, radius=1.3-0.3, labels=subgroup_names, labeldistance=0.7                           , colors=subgroup_colors)
    plt.setp(mypie2, width=.9, edgecolor='white')
    plt.margins(0, 0)

       # show it
    plt.show()

def violinplot(x, y, df, hue, title="Data Distribution", xlabel=None, ylabel=None, figsize=(12,8)):
    fig, ax = plt.subplots(figsize=figsize)
    ax = sns.stripplot(x=x, y=x, data=df
                       ,hue=hue, jitter=0.2, size=2.5)
    ax = sns.violinplot(x=x, y=y, data=df)
    if xlabel is None:
        xlabel = df[x].name
    if ylabel is None:
        ylabel = df[y].name
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    _ = plt.show()