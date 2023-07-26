"""Module to define data classes for config mapping"""
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataConfig:
    """Class to map data config"""
    source_URL: str
    data_download_path: Path
    data_original_path: Path
    data_transformed_path: Path


@dataclass(frozen=True)
class ModelConfig:
    """Class to map model config"""
    base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int



@dataclass(frozen=True)
class CallbackConfig:
    """Class to map callback config"""
    callback_path: Path
    tensorboard_log_path: Path
    model_checkpoint_path: Path


@dataclass(frozen=True)
class TrainConfig:
    """Class to map training config"""
    base_model_path: Path
    trained_model_path: Path
    training_data_path: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list

