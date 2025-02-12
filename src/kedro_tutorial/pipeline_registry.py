"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from kedro_tutorial.pipelines import quality_control


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = {} #find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    
    pipelines['quality_control-red'] = quality_control.create_pipeline(wine_type='red')
    pipelines['quality_control-white'] = quality_control.create_pipeline(wine_type='white')
    
    return pipelines
