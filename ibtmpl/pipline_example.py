import pyrootutils
from ibflow.utils.initialize import initialize_mlflow_vault_and_job_flow
pyrootutils.setup_root(__file__, indicator="setup.py", pythonpath=True)
import hydra
from omegaconf import DictConfig
from ibutil.hydra.config import extras
from ibutil.logger.pylogger import PyLogger
import mlflow
pylogger = PyLogger(name=__name__, seconds_divisor=1)


def example(cfg, job_flow, mlflow, vault_conn):
    pass


@hydra.main(version_base='1.3', config_path=f"../configs",
            config_name="default.yaml")
def run_example(cfg: DictConfig):
    vault_conn, job_flow = initialize_mlflow_vault_and_job_flow(cfg=cfg)
    with mlflow.start_run(run_id=cfg.mlflow.run.run_id):
        mlflow.set_tag(cfg.mlflow.run.tag_key, cfg.mlflow.run.tag_value)
        extras(cfg)
        example(vault_conn=vault_conn, cfg=cfg, job_flow=job_flow, mlflow=mlflow, )


if __name__ == '__main__':
    run_example()

