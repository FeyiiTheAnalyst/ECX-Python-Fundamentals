# #StudentName:Olorode Feyisayomi
# #imports necessary libraries
# import spotipy
# import os
# from dotenv import load_dotenv
# from spotipy.oauth2 import SpotifyOAuth
# import json
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# scope ="playlist-modify-public"
# username ="315rubjatpah2r3gk5h3chws6qhm"
# #("spotify_env") 
# SPOTIFY_CLIENT_ID=""
# SPOTIFY_CLIENT_SECRET=""

# # username = os.getenv("USERNAME")
# token = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
#                      client_secret=SPOTIFY_CLIENT_SECRET,
#                      redirect_uri="http://localhost:8888/callback",
#                      scope=scope,
#                      username=username
#                     )
# spotifyobject = spotipy.Spotify(auth_manager=token)

# #Returns the artistid for an artist entered by the user and accounts for an artist with less than 10 tracks
# def get_artist_id(artist_name):
#     result = spotifyobject.search(q=artist_name,limit=10,type="artist")
#     if  not result['artists']['items']:
#         print("Artist not found!!!")
#         pass
#     else:
#         artist_id = result['artists']['items'][0]['id']
#         return artist_id
   
        
# #returns a list of the top 10 tracks for the artist above using the artist id      
# def get_top_10_tracks(artist_id,artist_name):
#     top_tracks=spotifyobject.artist_top_tracks(artist_id=artist_id,country="NG")
#     result = top_tracks['tracks']
#     if len(result) <10:
#         print("This artist has fewer than 10 tracks on Spotify.")        
#     else:
#         print(f"Top 10 tracks for {artist_name}:")

#         for i, songs in enumerate(result, start=1):
#             print(f"{i}. {songs['name']}")
#     return top_tracks

# #gets the trackid for each track in the top tracks
# def get_track_id(top_tracks):
    
#       if 'tracks' in top_tracks and top_tracks['tracks']:
#          return [track['id'] for track in top_tracks['tracks']]  # Extracts track IDs
#       print("No Tracks Found!!")
#       return[]


# '''Function to create playlist'''
# def create_playlist(playlist_name):
#     playlist_desc = input("Enter your playlist description: ")
#     playlist=spotifyobject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_desc)
#     print("playlist created sucessfully.....")            
#     playlist_id= playlist['id'] 
#     return playlist_id
# ''''''

# #add tracks to playlist created using the playlist and track id
# def add_tracks_to_playlist(playlist_id,track_id):
#     if not playlist_id or not track_id:  # Ensure playlist and tracks exist
#         print("Cannot add tracks. Playlist or track IDs are missing.")
#         return

#     spotifyobject.playlist_add_items(playlist_id=playlist_id, items=track_id, position=0)
#     print("Tracks added successfully.....")

# #Function to generate billboardtop100 for a particular day
# def chart_list():
#     format="%Y-%m-%d"
#     user_date = input("Enter a date (YYYY-MM-DD): ")
#     #Validates the date entered by user
#     try:
#         valid_date = datetime.strptime(user_date, format).strftime(format)  # Ensure proper format
#     except ValueError:
#         print("Invalid date format! Please enter in YYYY-MM-DD format.")
#         return  
#     #send a request to the billboard webpage
#     URL = f"https://www.billboard.com/charts/hot-100/{valid_date}/"
#     headers ={
#         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
#         }
#     response = requests.get(URL, headers=headers)
#     status_code=response.status_code
#     if status_code == 200:

#         soup = BeautifulSoup(response.text, "html.parser")

#         # Extract only track titles 
#         track_elements = soup.find_all("h3", class_= "c-title" )

#         # Clean track names and filter out unwanted texts
#         tracks = [
#             track.text.strip() 
#             for track in track_elements 
#             if all(keyword not in track.text for keyword in ["Songwriter", "Imprint/Promotion Label", "Additional Awards", "Producer"," Gains in Weekly Performance"])
#         ]
#         new_tracks = list(dict.fromkeys(tracks))  # Keeps only the first occurrence of each item
#         new_tracks =new_tracks[:100]
#         # Print the track list
#         for i, track in enumerate(new_tracks, start=1):
#             print(f"{i}. {track}")
#         return new_tracks

#     else:
#         print("Could Not Connect To Server!!")


        
# def search_billboard(top_tracks):
#     for track in top_tracks:
#         spotifyobject.search(q=top_tracks,limit=10,offset=0,type="track")
#     return ['tracks'] 
    






# def initialize():
#     artist_name = input("Enter an artist name: ")
#     artist_id =get_artist_id(artist_name)
#     top_tracks =get_top_10_tracks(artist_id,artist_name)
#     return top_tracks  
         





# def main_program():
#     print(f"Welcome to My Playlist Curator\nInfo:There are two options here\n"
#           "1: To Search for an artist and creates a playlist with the top ten tracks of that artist\n"
#           "Enter 1!\n"
#           "2: Enter the word billboard,it returns the BillboardTop100 songs for a date requested and creates a playlist")
#     try:
#         user_input=input(("Enter a Command:")).lower().strip()
        
#         if user_input == "1":
#                 artist_name = input("Enter an artist name: ")
#                 artist_id =get_artist_id(artist_name)
#                 top_tracks =get_top_10_tracks(artist_id,artist_name)
#                 if len(top_tracks) < 10:
#                      initialize()
                
               
#                 track_id =get_track_id(top_tracks)
#                 playlist_name = input("Enter your playlist name:  ")
#                 users_playlist=spotifyobject.user_playlists(user=username,limit=50,offset=0)
#                 playlist_id = create_playlist(playlist_name)
                
                
#         elif user_input == "billboard":
            
#             top_tracks =chart_list()
#             search_billboard(top_tracks)
#             track_id =get_track_id(top_tracks)
#             playlist_name = input("Enter your playlist name:  ")
#             users_playlist=spotifyobject.user_playlists(user=username,limit=50,offset=0)
#             playlist_id = create_playlist(playlist_name)
#         if playlist_id and track_id:
#                 add_tracks_to_playlist(playlist_id,track_id)
#         else:
#                  print("Failed to add tracks.")
#     except:
#          raise ValueError
#     pass

# if __name__ == "__main__":
#     main_program()
    

#StudentName:Olorode Feyisayomi
#imports necessary libraries
import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
scope ="playlist-modify-public"
username ="315rubjatpah2r3gk5h3chws6qhm"
#("spotify_env") 
SPOTIFY_CLIENT_ID="ff0746940f834ddabfc3a3ae501b4bae"
SPOTIFY_CLIENT_SECRET="73faf657fa2941f4ab3ce62f1d71ce70"

# username = os.getenv("USERNAME")
token = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                     client_secret=SPOTIFY_CLIENT_SECRET,
                     redirect_uri="http://localhost:8888/callback",
                     scope=scope,
                     username=username
                    )
spotifyobject = spotipy.Spotify(auth_manager=token)

#Returns the artistid for an artist entered by the user and accounts for an artist with less than 10 tracks
def get_artist_id(artist_name):
    result = spotifyobject.search(q=artist_name,limit=10,type="artist")
    if  not result['artists']['items']:
        print("Artist not found!!!")
        pass
    else:
        artist_id = result['artists']['items'][0]['id']
        return artist_id
   
        
#returns a list of the top 10 tracks for the artist above using the artist id      
def get_top_10_tracks(artist_id,artist_name):
    top_tracks=spotifyobject.artist_top_tracks(artist_id=artist_id,country="NG")
    result = top_tracks['tracks']
    if len(result) <10:
        print("This artist has fewer than 10 tracks on Spotify.")        
    else:
        print(f"Top 10 tracks for {artist_name}:")

        for i, songs in enumerate(result, start=1):
            print(f"{i}. {songs['name']}")
    return top_tracks

#gets the trackid for each track in the top tracks
def get_track_id(top_tracks):
    
      if 'tracks' in top_tracks and top_tracks['tracks']:
         return [track['id'] for track in top_tracks['tracks']]  # Extracts track IDs
      print("No Tracks Found!!")
      return[]


'''Function to create playlist'''
def create_playlist(playlist_name):
    playlist_desc = input("Enter your playlist description: ")
    playlist=spotifyobject.user_playlist_create(user=username,name=playlist_name,public=True,description=playlist_desc)
    print("playlist created sucessfully.....")            
    playlist_id= playlist['id'] 
    return playlist_id
''''''

#add tracks to playlist created using the playlist and track id
def add_tracks_to_playlist(playlist_id,track_id):
    if not playlist_id or not track_id:  # Ensure playlist and tracks exist
        print("Cannot add tracks. Playlist or track IDs are missing.")
        return

    spotifyobject.playlist_add_items(playlist_id=playlist_id, items=track_id, position=0)
    print("Tracks added successfully.....")

#Function to generate billboardtop100 for a particular day
def chart_list():
    format="%Y-%m-%d"
    user_date = input("Enter a date (YYYY-MM-DD): ")
    #Validates the date entered by user
    try:
        valid_date = datetime.strptime(user_date, format).strftime(format)  # Ensure proper format
    except ValueError:
        print("Invalid date format! Please enter in YYYY-MM-DD format.")
        return  
    #send a request to the billboard webpage
    URL = f"https://www.billboard.com/charts/hot-100/{valid_date}/"
    headers ={
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
        }
    response = requests.get(URL, headers=headers)
    status_code=response.status_code
    if status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract only track titles 
        track_elements = soup.find_all("h3", class_= "c-title" )

        # Clean track names and filter out unwanted texts
        tracks = [
            track.text.strip() 
            for track in track_elements 
            if all(keyword not in track.text for keyword in ["Songwriter", "Imprint/Promotion Label", "Additional Awards", "Producer"," Gains in Weekly Performance"])
        ]
        new_tracks = list(dict.fromkeys(tracks))  # Keeps only the first occurrence of each item
        new_tracks =new_tracks[:100]
        # Print the track list
        for i, track in enumerate(new_tracks, start=1):
            print(f"{i}. {track}")
        return new_tracks

    else:
        print("Could Not Connect To Server!!")


        
def search_billboard(top_tracks):
    for track in top_tracks:
        spotifyobject.search(q=top_tracks,limit=10,offset=0,type="track")
    return ['tracks'] 
    






def initialize():
    artist_name = input("Enter an artist name: ")
    artist_id =get_artist_id(artist_name)
    top_tracks =get_top_10_tracks(artist_id,artist_name)
    return top_tracks  
         





def main_program():
    print(f"Welcome to My Playlist Curator\nInfo:There are two options here\n"
          "1: To Search for an artist and creates a playlist with the top ten tracks of that artist\n"
          "Enter 1!\n"
          "2: Enter the word billboard,it returns the BillboardTop100 songs for a date requested and creates a playlist")
    try:
        user_input=input(("Enter a Command:")).lower().strip()
        
        if user_input == "1":
                artist_name = input("Enter an artist name: ")
                artist_id =get_artist_id(artist_name)
                top_tracks =get_top_10_tracks(artist_id,artist_name)
                if len(top_tracks) < 10:
                     initialize()

               
                track_id =get_track_id(top_tracks)
                playlist_name = input("Enter your playlist name:  ")
                users_playlist=spotifyobject.user_playlists(user=username,limit=50,offset=0)
                playlist_id = create_playlist(playlist_name)
                
                
        elif user_input == "billboard":
            
            top_tracks =chart_list()
            search_billboard(top_tracks)
            track_id =get_track_id(top_tracks)
            playlist_name = input("Enter your playlist name:  ")
            users_playlist=spotifyobject.user_playlists(user=username,limit=50,offset=0)
            playlist_id = create_playlist(playlist_name)
        if playlist_id and track_id:
                add_tracks_to_playlist(playlist_id,track_id)
        else:
                 print("Failed to add tracks.")
    except:
         raise ValueError
    pass

if __name__ == "__main__":
    main_program()

    
