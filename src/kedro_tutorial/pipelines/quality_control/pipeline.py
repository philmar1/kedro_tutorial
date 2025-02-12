"""
This is a boilerplate pipeline 'quality_control'
generated using Kedro 0.19.10
"""

from kedro.pipeline import Pipeline, pipeline, node
from kedro_tutorial.pipelines.quality_control.nodes import * 

def create_pipeline(**kwargs) -> Pipeline:
    wine_type = kwargs['wine_type']
    
    my_pipeline = [node(func=std_scale,
                        inputs=['winequality'], # Becomes 'red.winequality' or 'white.winequality'
                        outputs='winequality_scaled', # Becomes 'red.winequality_scaled' or 'white.winequality_scaled'
                        name='std_scale', # Becomes 'red.std_scale' or 'white.std_scale'
                        tags='quality_control'),
                   node(func=plot_pca,
                        inputs={"data": 'winequality_scaled', 
                                "which": 'params:which',
                                "save_dir": 'params:dir.plot', # Becomes 'red.dir.plot' or 'white.dir.plot'
                                "pca_args": 'params:pca'}, # Becomes 'red.pca' 'white.pca'
                        outputs=None,
                        name='plot_pca', # Becomes 'red.plot_pca' or 'white.plot_pca'
                        tags='plot')]
    return pipeline(my_pipeline,
                    inputs = {'winequality': f'winequality-{wine_type}'}, # Change all calls to 'red.winequality' to 'winequality-red' (and 'white.winequality' to 'winequality-white')
                    parameters = {'params:dir.plot': 'params:dir.plot', # Change all calls to 'params:red.dir.plot' to 'dir.plot' (and 'params:white.dir.plot' to 'dir.plot')
                              f'params:which': f'{wine_type}', # Change all calls to 'params:red.which' to 'red' (and 'params:white.which' to 'white')
                              'params:pca' : 'params:pca'}, # Change all calls to 'red.pca' to 'pca' (and 'white.pca' to 'pca')
                    namespace=f'{wine_type}') # All nodes, parameters, inputs and outputs will have the prefix red or white added to them
