"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.10
"""

from kedro.pipeline import Pipeline, pipeline, node
from kedro_tutorial.pipelines.data_science.nodes import * 


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=split_train_test,
             inputs=['white.winequality_scaled', 'params:test_size'],
            outputs=['X_train', 'X_test', 'y_train', 'y_test'],
            name='split_train_test'),
        node(func=load_model,
             inputs=['params:model.name', 'params:model.params.mlp'],
             outputs='model',
             name='load_model'),
        node(func=train_model,
             inputs=['model', 'X_train', 'y_train'],
             outputs='trained_model',
             name='train_model'),
        node(func=predict,
             inputs=['trained_model', 'X_test'],
             outputs='y_pred',
             name='predict'),
        node(func=plot_metrics,
             inputs=['y_test', 'y_pred', 'params:white', 'trained_model', 'params:dir.plot'],
             outputs=None,
             name='plot_metrics')])