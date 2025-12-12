from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
import joblib
from pathlib import Path
import pandas as pd
from CancerML import logger
from CancerML.Entity.Config_Entity import DataModelingConfig


class DataModeling:
    def __init__(self, config: DataModelingConfig):
        self.config = config

    def Train_Model(self):

        file = Path(self.config.data_load_path)

        # Validate file exists
        if file.name not in self.config.all_required_files:
            logger.info("There is no CSV file in the source path.")
            return

        with open(self.config.status_file, 'w') as f:
            f.write("Validation Status : True")

        logger.info("Reading dataset...")
        df = pd.read_csv(file)

        # Ensure train column is numeric
        df["train"] = df["train"].astype(int)

        # Split features & target
        X = df.drop(columns="lpsa")
        y = df["lpsa"]

        # Preprocessing
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        x_train, x_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=11
        )

        # Save preprocessor
        save_dir = Path(self.config.local_data_path).parent
        preprocessor_path = save_dir / "preprocessor.pkl"
        joblib.dump(scaler, preprocessor_path)
        logger.info(f"Saved preprocessor at: {preprocessor_path}")

        # Train Linear Regression
        model = LinearRegression()
        model.fit(x_train, y_train)
        pred = model.predict(x_test)

        logger.info(f"Linear Regression R2 Score: {r2_score(y_test, pred)}")
        logger.info(f"Linear Regression MSE:      {mean_squared_error(y_test, pred)}")

        # Ridge
        rmodel = Ridge(alpha=0.01)
        rmodel.fit(x_train, y_train)
        rpred = rmodel.predict(x_test)
        logger.info(f"Ridge R2 Score: {r2_score(y_test, rpred)}")
        logger.info(f"Ridge MSE:      {mean_squared_error(y_test, rpred)}")

        # Lasso
        lmodel = Lasso(alpha=0.01)
        lmodel.fit(x_train, y_train)
        lpred = lmodel.predict(x_test)
        logger.info(f"Lasso R2 Score: {r2_score(y_test, lpred)}")
        logger.info(f"Lasso MSE:      {mean_squared_error(y_test, lpred)}")

        # Save final model
        model_path = save_dir / "final_model.pkl"
        joblib.dump(model, model_path)
        logger.info(f"Saved final model at: {model_path}")

        print("MODEL DEPLOYED SUCCESSFULLY")
