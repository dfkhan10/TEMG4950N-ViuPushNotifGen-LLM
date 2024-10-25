from dotenv import load_dotenv

load_dotenv(override=True)

cast = 'KIM Ha Neul'
viu_datasets = "Viu_datasets"

from pipeline import castDrivenPipeline
castDrivenPipeline(cast, push_number = 5)