import matplotlib.pyplot as plt
import seaborn as sns


def heatmaps(dataset, labels, dpi=300):
    '''
        Input:
            dataset -> (16 MEs, N LSs, 62 bins) numpy array of data to make heatmaps for
            labels -> list of string, size 16, contains title of each heat map
    '''
    fig, axes = plt.subplots(4,4)
    for i in range(0,4):
        for j in range(0,4):
            ax = axes[i, j]
            sns.heatmap(dataset[4*i + j,:,:], ax=ax, cbar=False)
            ax.tick_params(axis='both', which='both', length=0, labelbottom=False, labelleft=False)
            ax.set_title(labels[4*i + j], fontsize=4)
    fig.set_dpi(dpi)
    plt.show()
    
def heatmap(ME, title='', x_label='', y_label='', dpi=300):
    fig, axes = plt.subplots()
    sns.heatmap(ME, ax=axes, cbar=True)
    axes.set_title(title, fontsize=12)
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)
    fig.set_dpi(dpi)
    return axes

def heatmaps(ME, ax=None, title='', x_label='', y_label='', dpi=300):
    if ax is None:
        fig, ax = plt.subplots()
    sns.heatmap(ME, ax=ax, cbar=True)
    ax.set_title(title, fontsize=12)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    # Set DPI and figure size if a new figure was created
    if ax is None:
        fig.set_dpi(dpi)
        fig.set_tight_layout(True)
    return ax
