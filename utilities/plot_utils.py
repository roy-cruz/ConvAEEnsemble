import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


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

def heatmapsfig(ME, ax=None, title='', x_label='', y_label='', dpi=300):
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

def plotallMEs(eval_recos, evalruns_norm, Xs_train_norm, monitoring_elems, k=0, dpi=200):
    bins = np.arange(0,62)
    fig, axes = plt.subplots(4, 4, figsize=(30,30), dpi=dpi)
    axes = axes.flatten()

    for i, ax in enumerate(axes):
        reco = eval_recos[k][i]
        test = evalruns_norm[k][i]
        for j, histo in enumerate(reco):
            if j == 0: 
                ax.step(bins, histo, color='red', alpha=0.8, label='Reco')
                ax.step(bins, test[j], color='green', alpha=0.3, label='Input')
            ax.step(bins, histo, color='red', alpha=0.8)
            ax.step(bins, test[j], color='green', alpha=0.3)
        ax.step(bins, Xs_train_norm[i].mean(axis=0), color='blue', alpha=1, label='Train')
        ax.legend(loc='upper right')
        ax.tick_params(axis='x', labelsize=10)
        ax.tick_params(axis='y', labelsize=10)
        ax.set_title(monitoring_elems[i], fontsize=12)   
    plt.show()