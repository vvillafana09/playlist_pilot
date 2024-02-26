import pandas as pd
import numpy as np
import json
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

def recommend_songs(data, dataset_path="dataset.csv"):
    df = pd.read_csv(dataset_path)
    df = df.drop_duplicates(subset=["track_name", "artists"])
    df_copy = df.copy()
    df = df.drop(columns=['explicit'])
    df['track_genre'] = df['track_genre'].replace('r-n-b', 'r&b')
        
    user_df = pd.DataFrame(data)

    feature_cols=['duration_ms', 'danceability', 'energy', 'key', 'loudness', 'mode',
                'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence',
                'tempo', 'time_signature']


    data_cols=['duration_ms', 'danceability', 'energy', 'key', 'loudness', 'mode',
                'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence',
                'tempo', 'time_signature', 'popularity']

    scaler = MinMaxScaler()
    df[data_cols] = scaler.fit_transform(df[data_cols])

    user_df['genres'] = user_df['genres'].astype(str).str.replace("[\[\]',]", '', regex=True).str.strip()
    user_df_genres = user_df['genres'].str.get_dummies(sep=' ')
    user_df = pd.concat([user_df, user_df_genres], axis=1)

    user_genres = user_df_genres.columns.tolist()
    num_drop = len(user_genres)

    #one-hot encode genres for dataset and playlist
    dataset_genres = pd.get_dummies(df['track_genre'])
    dataset_genres = dataset_genres.astype(int)
    df = pd.concat([df, dataset_genres], axis=1)

    # Find missing columns
    missing_cols = [col for col in dataset_genres.columns if col not in user_df.columns]

    # Add missing columns to user_df and fill with 0
    user_df_updated = pd.concat([user_df, pd.DataFrame(0, index=user_df.index, columns=missing_cols)], axis=1)

    # Reorder the columns to match between user_df and dataset
    user_df_updated = user_df_updated[dataset_genres.columns]
    user_df = user_df.iloc[:, :-(num_drop)]

    # Concatenate user_df and user_df_updated to keep the original dataset
    final_user_df = pd.concat([user_df, user_df_updated], axis=1)

    scaler = MinMaxScaler()
    final_user_df[feature_cols] = scaler.fit_transform(final_user_df[feature_cols])

    popularity_col = 'popularity'
    popularity_scaler = MinMaxScaler()
    final_user_df[popularity_col] = popularity_scaler.fit_transform(final_user_df[[popularity_col]])

    user_profile = np.concatenate(([final_user_df['popularity'].mean()], final_user_df[feature_cols].mean().values, final_user_df.drop(columns=feature_cols).sum().values))
    user_profile = np.delete(user_profile, np.s_[14:17])
    # print(user_profile)
    # print(df.head())
    df = df.drop(columns=['track_id', 'artists', 'album_name', 'track_name'])
    df = df.drop(df.columns[0],axis=1)
    df = df.select_dtypes(include=[np.number])
    similarity_scores = cosine_similarity(user_profile.reshape(1, -1), df.values)
    # print(similarity_scores)

    # # Recommend top songs
    top_song_indices = similarity_scores.argsort()[0][-5:][::-1]  # Get indices of top 5 songs
    recommended_songs = df_copy.iloc[top_song_indices]  # Get top 5 songs from the dataset

    # Display recommended songs
    return recommended_songs