"""
This is a boilerplate pipeline 'quality_control'
generated using Kedro 0.19.10
"""

from matplotlib import pyplot as plt 
import pandas as pd 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import logging

logger = logging.getLogger(__name__)

def std_scale(data):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    scaled_data = pd.DataFrame(data=scaled_data,
                               index=data.index,
                               columns=data.columns)
    
    logger.info(f'Data scaled ! : {scaled_data.head(2)} ')
    return scaled_data


def plot_pca(data, which='red', save_dir=None, pca_args={}):
    pca = PCA(**pca_args)
    embeddings = pca.fit_transform(data)
    plt.scatter(embeddings[:,0], embeddings[:,1], s=2)
    plt.title('PCA')
    plt.savefig(save_dir + f'PCA_{which}.png')