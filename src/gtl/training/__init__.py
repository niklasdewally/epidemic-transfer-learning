# ruff: noqa: F401
"""
High-level training functions for models
"""


from collections.abc import Mapping as Mapping
from collections.abc import Callable as Callable
from dgl import DGLGraph as DGLGraph
from torch import Tensor
from functools import partial

from .. import Graph
from . import egi as _egi
from . import graphsage as _graphsage


_model_functions: dict[str, Callable] = {
    "graphsage": _graphsage.train_graphsage_encoder,
    "egi": partial(_egi.train_egi_encoder, sampler_type="egi"),
    "triangle": partial(_egi.train_egi_encoder, sampler_type="triangle"),
}

Model = Callable[[DGLGraph, Tensor], Tensor]


# pyre-ignore[2]:
def train(model: str, graph: Graph, **kwargs) -> Model:
    """
    Train the given model.
    """
    func = _model_functions.get(model)

    if func is None:
        raise ValueError(f"No such model: {model}")

    return func(graph, **kwargs)


# pyre-ignore[5]:
__all__ = [Model, train]
