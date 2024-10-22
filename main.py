from dotenv import load_dotenv

load_dotenv(override=True)

cast = 'YEON Woo Jin'
area = 'Hong Kong'
language = 'English'
viu_datasets = "Viu_datasets"

from pipeline import castDrivenPipeline
castDrivenPipeline(cast, viu_datasets)