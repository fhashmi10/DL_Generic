from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataConfig:
    source_URL: str
    data_download_path: Path
    data_original_path: Path
    data_transformed_path: Path


@dataclass(frozen=True)
class ModelConfig:
    base_model_path: Path
    trained_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int



@dataclass(frozen=True)
class CallbackConfig:
    root_dir: Path
    tensorboard_log_dir: Path
    model_checkpoint_path: Path



@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list



@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    params_image_size: list
    params_batch_size: int
