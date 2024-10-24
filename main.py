from dotenv import load_dotenv

load_dotenv(override=True)

cast = 'KIM Ha Neul'
viu_datasets = "Viu_datasets"

# from pipeline import castDrivenPipeline
# castDrivenPipeline(cast, viu_datasets)

from fastapi import FastAPI
from route.cast_driven import cast_driven_router
    
app = FastAPI()
app.include_router(cast_driven_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)