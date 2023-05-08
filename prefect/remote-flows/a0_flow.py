import platform

from prefect import flow, get_run_logger, task


@task
def platform_info():
    print("Printing Platform Information -")
    logger = get_run_logger()
    info = [
        f"Architecture - {platform.architecture()}",
        f"Machine - {platform.machine()}",
        f"Node - {platform.node()}",
        f"Processor - {platform.processor()}",
        f"Py build - {platform.python_build()}",
        f"Py compiler - {platform.python_compiler()}",
        f"Py branch - {platform.python_branch()}",
        f"Py revision - {platform.python_revision()}",
        f"Py version - {platform.python_version()}",
        f"Py version_tuple - {platform.python_version_tuple()}",
        f"Py implementation - {platform.python_implementation()}",
        f"Release - {platform.release()}",
        f"System - {platform.system()}",
        f"Version - {platform.version()}",
    ]
    for ele in info:
        print(ele)
        logger.info(ele)
    return info



@task
def package_info():
    import cv2
    import mlflow as mlf
    import pytorch_lightning as pl
    import torch
    import torchvision

    logger = get_run_logger()
    print("Printing Packages Information -")
    info = [
        f"pytorch_lightning - {pl.__version__}",
        f"mlflow - {mlf.__version__}",
        f"cv2 - {cv2.__version__}",
        f"torch - {torch.__version__}",
        f"torchvision - {torchvision.__version__}",
        f"GPU Available - {torch.cuda.is_available()}",
        f"GPU Counts - {torch.cuda.device_count()}",
        f"GPU Name - {torch.cuda.get_device_name(0)}",
    ]
    for ele in info:
        print(ele)
        logger.info(ele)
    return info



@flow
def print_executor_info():
    platform_info()
    package_info()

if __name__ == "__main__":
    print_executor_info()