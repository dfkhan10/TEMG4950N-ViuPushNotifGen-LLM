from dotenv import load_dotenv

load_dotenv(override=True)

cast = 'KIM Ha Neul'
viu_datasets = "Viu_datasets"

# from pipeline.pipeline import castDrivenPipeline
# castDrivenPipeline(cast, push_number = 5)

#from pipeline import genPush
#genPush.testingPipeline(cast, push_number = 5)

#from pipeline.pipeline import contentDrivenPipeline
#contentDrivenPipeline('Nothing Uncovered', push_number = 5)

#from pipeline import genPush
#genPush.testingContentPipeline('Nothing Uncovered', push_number = 5)

from pipeline import rerankingGen
rerankingGen.simplifiedCastPipe(cast, push_number = 1)