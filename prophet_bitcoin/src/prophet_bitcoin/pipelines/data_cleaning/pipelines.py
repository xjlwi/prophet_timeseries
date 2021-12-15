from kedro.pipeline import Pipeline, node
from .nodes import clean_data

def create_pipeline(**kwargs):
    return Pipeline(
        [node(func = clean_data,
            inputs = "bitcoin_feather", 
            outputs = "bitcoin_csv", 
            name = 'clean_bitcoin_feather')
        ]
    )