"""
This is a boilerplate pipeline 'quality_control'
generated using Kedro 0.19.10
"""

from kedro.pipeline import Pipeline, pipeline, node
from kedro_tutorial.pipelines.quality_control.nodes import * 

def create_pipeline(**kwargs) -> Pipeline:
    my_pipeline = [node(func=std_scale,
                        inputs=['winequality-white'],
                        outputs='winequality_scaled',
                        tags='quality_control'),
                   node(func=plot_pca,
                        inputs=['winequality_scaled', 'params:which', 'params:dir.plot', 'params:pca'],
                        outputs=None,
                        tags='plot')]
    return pipeline(my_pipeline)
