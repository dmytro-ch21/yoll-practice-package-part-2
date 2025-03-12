# 06_playlist_manager

## Description
In this exercise, you will create a simple playlist manager that allows users to manage a music playlist. The program will demonstrate various list operations including adding songs, removing songs, and displaying different views of the playlist.

## Instructions
1. Begin with an empty playlist (an empty list)
2. Add the following songs to the playlist (in this order):
   * "Bohemian Rhapsody" by Queen
   * "Hotel California" by Eagles
   * "Sweet Child O'Mine" by Guns N'Roses
   * "Billie Jean" by Michael Jackson
   * "Stairway to Heaven" by Led Zeppelin
   > Here pay attention that what you show you add to the list and what you actually add is different:
   > 
   > Adding: "Bohemian Rhapsody" by Queen - Here we use `""` for song name and `by` artist.
   > Current playlist: ['Bohemian Rhapsody - Queen'] - However, we add in the list the elements in this format `"song title - artist"`
3. Display the current playlist after each addition
4. Show the most recently added songs (last 3 songs)
5. Display the first and last songs in the playlist
6. Remove "Hotel California" from the playlist without using loops
7. Create a "top songs" list containing the first 2 songs from the updated playlist

## Implementation Notes
- Use the `.append()` method to add songs to the playlist
- Format each song as `"{title} - {artist}"` (e.g., "Bohemian Rhapsody - Queen"), with a space on each side of the hyphen
- When adding a song to the playlist, concatenate the title and artist with " - " between them
- Use list slicing (`playlist[-3:]`) to get the last 3 songs
- Use indexing (`playlist[0]` and `playlist[-1]`) to get the first and last songs
- Use the `.remove()` method to remove "Hotel California" from the playlist
- Use list slicing (`playlist[:2]`) to create the top songs list
- Print each step using f-strings to show the current state of the playlist

## Output Requirements
For each step, make sure your output includes:
- Welcome message and empty playlist at the start
- Clear announcement when adding each song
- Display of the playlist after each addition
- Label for "Recently added songs (last 3)"
- Clear labels for first and last song
- Announcement when removing "Hotel California"
- Display of the updated playlist after removal
- Label for the "Top songs list"

## Expected Output

```
Welcome to Playlist Manager!

Current playlist: []

Adding: "Bohemian Rhapsody" by Queen
Current playlist: ['Bohemian Rhapsody - Queen']

Adding: "Hotel California" by Eagles
Current playlist: ['Bohemian Rhapsody - Queen', 'Hotel California - Eagles']

Adding: "Sweet Child O'Mine" by Guns N'Roses
Current playlist: ['Bohemian Rhapsody - Queen', 'Hotel California - Eagles', 'Sweet Child O'Mine - Guns N'Roses']

Adding: "Billie Jean" by Michael Jackson
Current playlist: ['Bohemian Rhapsody - Queen', 'Hotel California - Eagles', 'Sweet Child O'Mine - Guns N'Roses', 'Billie Jean - Michael Jackson']

Adding: "Stairway to Heaven" by Led Zeppelin
Current playlist: ['Bohemian Rhapsody - Queen', 'Hotel California - Eagles', 'Sweet Child O'Mine - Guns N'Roses', 'Billie Jean - Michael Jackson', 'Stairway to Heaven - Led Zeppelin']

Recently added songs (last 3): ['Sweet Child O'Mine - Guns N'Roses', 'Billie Jean - Michael Jackson', 'Stairway to Heaven - Led Zeppelin']

First song: Bohemian Rhapsody - Queen
Last song: Stairway to Heaven - Led Zeppelin

Removing: "Hotel California" by Eagles
Current playlist: ['Bohemian Rhapsody - Queen', 'Sweet Child O'Mine - Guns N'Roses', 'Billie Jean - Michael Jackson', 'Stairway to Heaven - Led Zeppelin']

Top songs list: ['Bohemian Rhapsody - Queen', 'Sweet Child O'Mine - Guns N'Roses']
```

## Hints
* To add an item to a list, you can use the `.append()` method
* To get a slice of a list, use the slicing notation: `my_list[start:end]`
* To get the last items of a list, use negative indexing: `my_list[-3:]` for the last 3 items
* To remove a specific item from a list, use the `.remove()` method: `playlist.remove("Hotel California - Eagles")`
* Remember that strings can be combined using f-strings: `f"{title} - {artist}"` (ensure there's a space before and after the hyphen)
* Each song in the playlist should be stored in the format "Song Title - Artist Name"
* Use f-strings for printing: `print(f"Current playlist: {playlist}")`
* Make sure your output matches the expected format