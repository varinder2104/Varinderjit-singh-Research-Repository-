def generate_band_name():
    return "Seventeen"


guest_list=["joshua", "jeonghan", "Cheol", "Jun"]
def send_email(member, band_name):
    message= f"""Dear {member},
    
We are thrilled to announce that our band, "band name,"
will be performing live on Saturday, 15 October 2023,
at the Grand Music Hall (123 Main Street, Your City).
The show will start at 8:00 PM.

Don't miss the chance to experience an unforgettable night of music and entertainment.
Invite your friends and family for an incredible musical journey!
See you at the show!

Best regards,
{band_name}
"""
    print(message)
    print("-"*90)

band_name= generate_band_name()

for member in guest_list:
    send_email(member, band_name)