import datetime
import wandb
import argparse
from triangle_detection_task import do_run, default_config

current_date_time: str = datetime.datetime.now().strftime("%Y-%m-%d (T%H%M)")
entity = "sta-graph-transfer-learning"
project = "Triangle Detection"


sweep_config = {
    "metric": {"goal": "maximize", "name": "avg_target_accuracy"},
    "method": "bayes",
    "parameters": {
        "batch_size": {"values": [16, 32, 64]},
        "hidden_layers": {"min": 16, "max": 128},
        "lr": {"min": 0.0001, "max": 0.1},
        "k": {"min": 1, "max": 5},
        "sweep_n_runs": {"value": 4},
        "source_core_size": {"value": 75},
        "target_core_size": {"value": 75},
        "source_periphery_size": {"value": 500},
        "target_periphery_size": {"value": 500},
        "patience": {"value": 10},
        "min_delta": {"value": 0.01},
        "epochs": {"value": 100},
    },
}


def main() -> None:
    # read model type from arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("model", choices=["egi", "triangle", "graphsage"])
    parser.add_argument("--sweep-id", default=None, required=False)

    args = parser.parse_args()
    model = args.model
    sweep_id = args.sweep_id

    # create new sweep if sweep id is not given
    if sweep_id is None:
        # add model and name to sweep
        sweep_config.update({"name": f"{model} ({current_date_time})"}),
        sweep_config["parameters"].update({"model": {"value": model}})

        sweep_id = wandb.sweep(sweep=sweep_config, project=project, entity=entity)

    wandb.agent(sweep_id=sweep_id, function=sweep_runner)


def sweep_runner() -> None:
    wandb.init(config=default_config)
    acc = 0
    for i in range(wandb.config.sweep_n_runs):
        do_run()
        acc += wandb.summary["target-accuracy"]

    wandb.log({"avg_target_accuracy": acc / wandb.config.sweep_n_runs})
    wandb.finish()


if __name__ == "__main__":
    main()