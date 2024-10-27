import os
import pandas as pd
import random

def excelToPandas(datasets):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    datasets_path = os.path.join(script_dir, datasets)
    
    content_meta_df = pd.read_excel(datasets_path + '/content_metadata.xlsx',
                                usecols=["EXTERNAL_SERIES_ID", "GROUP_SERIES_NAME", "MAIN_CASTS", "SUPPORTING_CASTS", "CAMEO_CASTS", "HOST", "VO_TALENT", "WIKI_EN_URL"],
                                engine='openpyxl')

    content_des_df = pd.read_excel(datasets_path + '/content_description_multilang_mapping.xlsx',
                               usecols=["EXTERNAL_SERIES_ID", "AREA_NME", "LANG_NME", "SRI_DES", "EPS_NO", "EPS_SYP", "EPS_DES"],
                               engine='openpyxl')
    
    return content_meta_df, content_des_df

def getSeriesEpisodeMatch(serie_database, episode_database, language):
    
    serie_extrernal_id = set(serie_database["EXTERNAL_SERIES_ID"])
    episode_extrernal_id = set(episode_database["EXTERNAL_SERIES_ID"])

    common_id = serie_extrernal_id.intersection(episode_extrernal_id)  
    
    print(list(common_id))
    
    return list(common_id)  
    
def getCastDrivenData(cast, datasets):
    
    content_meta_df, content_des_df = excelToPandas(datasets)
    
    #Get the row from meta by cast
    meta = content_meta_df[
        (content_meta_df['MAIN_CASTS'].str.contains(cast)) |
        (content_meta_df['SUPPORTING_CASTS'].str.contains(cast)) |
        (content_meta_df['CAMEO_CASTS'].str.contains(cast)) |
        (content_meta_df['HOST'].str.contains(cast)) |
        (content_meta_df['VO_TALENT'].str.contains(cast))
    ]
    
    #Get the row from description by area
    dess = content_des_df[(content_des_df['AREA_NME'] == 'Malaysia')]
    
    common_id = getSeriesEpisodeMatch(meta, dess, "Malaysia")
    
    #choose a random series
    random_series_idx = random.randint(0, len(common_id) - 1)
    series = meta[(meta["EXTERNAL_SERIES_ID"] == common_id[random_series_idx])]
    episodes = dess[(dess["EXTERNAL_SERIES_ID"] == common_id[random_series_idx])]
    
    #choose a random episode
    random_episode_idx = random.randint(0, len(episodes) - 1)

    #Group the data, ASSUME promote episode 1 in this case
    data = {
        "target_cast": cast,
        "target_cast_type": next((col for col in series.columns if series[col].str.contains(cast).any()), None),
        "series_idx": series.iloc[0]['EXTERNAL_SERIES_ID'],
        "series_name": series.iloc[0]['GROUP_SERIES_NAME'],
        "series_description": episodes.iloc[random_episode_idx]["SRI_DES"],
        "series_wiki_url": series.iloc[0]['WIKI_EN_URL'],
        "episode_idx": episodes.iloc[random_episode_idx]["EPS_NO"],
        "episode_name": episodes.iloc[random_episode_idx]["EPS_SYP"],
        "episode_description": episodes.iloc[random_episode_idx]["EPS_DES"],
    }
    
    print(data)
    
    return data