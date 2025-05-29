def introduce_band_members():
    members=["Singer","guitarist","bassist","drumer"]
    for member in members:
        print(f"Meet the {member} of the band.")

def play_song(song_name):
    print(f"Now playing: {song_name}")


def create_band_poster(band_name, band_members, event_time, event_place):
    print("------------------Band Poster----------------")
    print(f"Band name: {band_name}")
    print("Band Members:")
    for member in band_members:
        print(f"- {member}")
    print(f"Event Time: {event_time}")
    print(f"Event Place: {event_place}")
    print("----------------------------------------------")

band_name= "Seventeen"
band_members = ["joshua", "jeonghan", "Cheol", "Jun"]
event_time= "7:00 PM"
event_place= "Seoul, South Korea"

create_band_poster(band_name, band_members, event_time, event_place)
introduce_band_members()
play_song("Rock with you")