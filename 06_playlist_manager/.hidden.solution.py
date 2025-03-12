def main():
    playlist = []
    
    print("Welcome to Playlist Manager!")
    print()
    print(f"Current playlist: {playlist}")
    print()
    
    print('Adding: "Bohemian Rhapsody" by Queen')
    playlist.append("Bohemian Rhapsody - Queen")
    print(f"Current playlist: {playlist}")
    print()
    s
    print('Adding: "Hotel California" by Eagles')
    playlist.append("Hotel California - Eagles")
    print(f"Current playlist: {playlist}")
    print()
  
    print('Adding: "Sweet Child O\'Mine" by Guns N\'Roses')
    playlist.append("Sweet Child O'Mine - Guns N'Roses")
    print(f"Current playlist: {playlist}")
    print()
    
    print('Adding: "Billie Jean" by Michael Jackson')
    playlist.append("Billie Jean - Michael Jackson")
    print(f"Current playlist: {playlist}")
    print()
    
    print('Adding: "Stairway to Heaven" by Led Zeppelin')
    playlist.append("Stairway to Heaven - Led Zeppelin")
    print(f"Current playlist: {playlist}")
    print()
    
    recent_songs = playlist[-3:]
    print(f"Recently added songs (last 3): {recent_songs}")
    print()
    
    print(f"First song: {playlist[0]}")
    print(f"Last song: {playlist[-1]}")
    print()

    print('Removing: "Hotel California" by Eagles')
    playlist.remove("Hotel California - Eagles")
    print(f"Current playlist: {playlist}")
    print()
    
    top_songs = playlist[:2]
    print(f"Top songs list: {top_songs}")

main()