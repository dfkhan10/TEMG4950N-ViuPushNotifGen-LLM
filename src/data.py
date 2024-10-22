import os
import pandas as pd

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

    #Let user to decide which series to promote
    print("List of series that involve " + cast)
    for idx, series in enumerate(meta.iloc[:]['GROUP_SERIES_NAME']):
        print(str(idx + 1) + ". " + series)
    series_idx = int(input("Please choose the index of the series to promote: ")) - 1
    series = meta.iloc[[series_idx]]

    #Get the row from description by series ID
    dess = content_des_df[
        (content_des_df['EXTERNAL_SERIES_ID'] == series.iloc[0]['EXTERNAL_SERIES_ID']) &
        (content_des_df['AREA_NME'] == 'Hong Kong') &
        (content_des_df['LANG_NME'] == 'English')
    ]

    #Group the data, ASSUME promote episode 1 in this case
    data = {
        "target_cast": cast,
        "target_cast_type": next((col for col in series.columns if series[col].str.contains(cast).any()), None),
        "series_name": series.iloc[0]['GROUP_SERIES_NAME'],
        "series_description": dess.iloc[0]["SRI_DES"],
        "series_wiki_url": series.iloc[0]['WIKI_EN_URL'],
        "episode_idx": dess.iloc[0]["EPS_NO"],
        "episode_name": dess.iloc[0]["EPS_SYP"],
        "episode_description": dess.iloc[0]["EPS_DES"],
    }
    
    return data