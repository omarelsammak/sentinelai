import mlflow

class Trainer:
    def train(self):
                # Specify the tracking server URI, e.g. 
        mlflow.set_tracking_uri("http://localhost:5000")
        # If the experiment with the name "traces-quickstart" doesn't exist, MLflow will create it
        mlflow.set_experiment("traces-quickstart")
        with mlflow.start_run():
            mlflow.log_param("param_example", 123)
            mlflow.log_metric("loss", 0.25)
        print("🧠 Training logged in MLflow")
