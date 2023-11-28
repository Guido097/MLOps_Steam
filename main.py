from fastapi import FastAPI
import pandas as pd
import numpy as np
from fastapi import FastAPI, Depends
from sklearn.metrics.pairwise import cosine_similarity
from typing import List


app = FastAPI()

df_userdata = pd.read_parquet('DataBases\items_final.parquet')
df_games = pd.read_parquet('DataBases\games.parquet')
df_reviews = pd.read_parquet('DataBases/reviews_final.parquet')

@app.get('/PlayTimeGenre/{genero}')
def PlayTimeGenre(genero: str):
    try:
        if genero not in df_userdata.columns:
            return {"mensaje": f"El género '{genero}' no se encuentra en los datos"}
        
        filtered_df = df_userdata[df_userdata[genero] == 1]

        if len(filtered_df) == 0:
            return {"mensaje": f"No se encontraron datos para el género '{genero}'"}

        año_mas_horas = filtered_df.groupby('release_year')['playtimeforever'].sum().idxmax()
        
        año_mas_horas = int(año_mas_horas)

        return {f"Año de lanzamiento con más horas jugadas para el género '{genero}'": año_mas_horas}
    except Exception as e:
        return {"error": str(e)}


@app.get('/UserForGenre/{genero}')
def UserForGenre(genero: str):
    try:
        if genero not in df_userdata.columns:
            return {"mensaje": f"El género '{genero}' no se encuentra en los datos"}

        filtered_df = df_userdata[df_userdata[genero] == 1]

        if len(filtered_df) == 0:
            return {"mensaje": f"No se encontraron datos para el género '{genero}'"}

        usuario_mas_horas = filtered_df.groupby('p_morehours')['user_hours'].sum().idxmax()
        
        return {
            f"Usuario con más horas jugadas para el género '{genero}'": usuario_mas_horas}
    except Exception as e:
        return {"error": str(e)}


@app.get('/UsersRecommend/{anio}')
def UsersRecommend(anio: int):
    try:
        
        df_filtered = df_reviews[df_reviews['year'] == anio]
        
        df_filtered = df_filtered[(df_filtered['recommend'] == True) & 
                                ((df_filtered['sentiment_analysis'] == 'Positivo') | 
                                (df_filtered['sentiment_analysis'] == 'Neutral'))]
        
        recommendations_count = df_filtered['app_name'].value_counts()
        
        top_3_games = recommendations_count.head(3)
        
        
        result = [{"Puesto {}: {}".format(i+1, game): count} for i, (game, count) in enumerate(top_3_games.iteritems())]
        
        return result
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/worst_developers/{year}", response_model=List[dict])
def worst_developers(year: int):
    try:
        
        filtered_reviews = df_reviews[(df_reviews['year'] == year) & (df_reviews['recommend'] == False) & (df_reviews['sentiment_analysis'] == 'Negativo')]

        developer_counts = filtered_reviews['developer'].value_counts()

        top3_developers = developer_counts.head(3)

        resultado = [{"Puesto {}: {}".format(i + 1, developer): count} for i, (developer, count) in enumerate(top3_developers.items())]

        return resultado
    except Exception as e:
        return {"error": str(e)}


@app.get('/SentimentAnalysis/{developer}')
def sentiment_analysis(developer: str):
    try:
        df_filtered = df_reviews[df_reviews['developer'] == developer]
        
        sentiment_counts = df_filtered['sentiment_analysis'].value_counts()
        
        sentiment_counts = sentiment_counts.to_dict()
        
        del df_filtered
        
        result = {
            'Negative': sentiment_counts.get('Negativo', 0),
            'Neutral': sentiment_counts.get('Neutral', 0),
            'Positive': sentiment_counts.get('Positivo', 0)
        }
        return result
    except Exception as e:
        return {"error": str(e)} 


@app.get("/recomendacion_juego/{id_producto}", response_model=List[dict])
def recomendacion_juego(id_producto: int):
    try:
        juego_actual = df_games[df_games['id'] == id_producto]
        if juego_actual.empty:
            return {"error": "Juego no encontrado"}

        developer_juego = juego_actual['developer'].iloc[0]

        juegos_similares = df_games[(df_games['developer'] == developer_juego) & (df_games['id'] != id_producto)].head(5)

        resultado = [{"Puesto {}: {}".format(i + 1, row['app_name']): row['id']} for i, row in juegos_similares.iterrows()]

        return resultado
    except Exception as e:
        return {"error": str(e)}