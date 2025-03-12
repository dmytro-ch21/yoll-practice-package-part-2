import pytest
import sys
from io import StringIO

def capture_output():
    saved_stdout = sys.stdout
    
    try:
        sys.stdout = StringIO()
        
        exec(open("solution.py").read())
        
        return sys.stdout.getvalue()
    finally:
        sys.stdout = saved_stdout

def test_playlist_output():
    """Test that all required elements are present in the output"""
    output = capture_output()
    
    expected_elements = [
        "Welcome to Playlist Manager!",
        "Adding: \"Bohemian Rhapsody\" by Queen",
        "Adding: \"Hotel California\" by Eagles",
        "Adding: \"Sweet Child O'Mine\" by Guns N'Roses",
        "Adding: \"Billie Jean\" by Michael Jackson",
        "Adding: \"Stairway to Heaven\" by Led Zeppelin",
        "Recently added songs (last 3)",
        "First song: Bohemian Rhapsody - Queen",
        "Last song: Stairway to Heaven - Led Zeppelin",
        "Removing: \"Hotel California\" by Eagles",
        "Top songs list:"
    ]
    
    for element in expected_elements:
        assert element in output

def test_songs_added_correctly():
    """Test that all songs are added to the playlist in correct order"""
    output = capture_output()
    
    # Check that all songs are present in the correct order
    all_songs = [
        "Bohemian Rhapsody - Queen", 
        "Hotel California - Eagles", 
        "Sweet Child O'Mine - Guns N'Roses", 
        "Billie Jean - Michael Jackson", 
        "Stairway to Heaven - Led Zeppelin"
    ]
    
    # Just check that each song appears in the output in the correct order
    last_pos = -1
    for song in all_songs:
        pos = output.find(song)
        assert pos > last_pos, f"Song '{song}' not found or in wrong order"
        last_pos = pos

def test_hotel_california_removed():
    """Test that Hotel California is removed from the playlist"""
    output = capture_output()
    
    # Find the line after removal
    lines = output.split('\n')
    for i, line in enumerate(lines):
        if 'Removing: "Hotel California" by Eagles' in line:
            # Check that the next non-empty line has the updated playlist
            for j in range(i+1, len(lines)):
                if "Current playlist:" in lines[j]:
                    # Check that this playlist contains all songs except Hotel California
                    assert "Bohemian Rhapsody - Queen" in lines[j]
                    assert "Sweet Child O'Mine - Guns N'Roses" in lines[j]
                    assert "Billie Jean - Michael Jackson" in lines[j]
                    assert "Stairway to Heaven - Led Zeppelin" in lines[j]
                    assert "Hotel California - Eagles" not in lines[j]
                    return
    
    assert False, "Could not find updated playlist after removing Hotel California"

def test_recent_songs():
    """Test that the last 3 songs are shown correctly"""
    output = capture_output()
    
    # Check that recently added songs contains the last 3 songs
    recent_songs = [
        "Sweet Child O'Mine - Guns N'Roses",
        "Billie Jean - Michael Jackson",
        "Stairway to Heaven - Led Zeppelin"
    ]
    
    recent_line = ""
    for line in output.split('\n'):
        if "Recently added songs (last 3)" in line:
            recent_line = line
            break
    
    assert recent_line, "Could not find recently added songs line"
    
    # Check that all 3 recent songs are in the line
    for song in recent_songs:
        assert song in recent_line, f"Recent song '{song}' not found"

def test_top_songs():
    """Test that the top songs list contains the first 2 songs after removal"""
    output = capture_output()
    
    # Top songs should be the first 2 songs after removal
    top_songs = [
        "Bohemian Rhapsody - Queen",
        "Sweet Child O'Mine - Guns N'Roses"
    ]
    
    top_line = ""
    for line in output.split('\n'):
        if "Top songs list:" in line:
            top_line = line
            break
    
    assert top_line, "Could not find top songs line"
    
    # Check that both top songs are in the line
    for song in top_songs:
        assert song in top_line, f"Top song '{song}' not found"