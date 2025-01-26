import streamlit as st
songs = {
  "":"",
    "Shape of You": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "Blinding Lights": "https://www.youtube.com/watch?v=4NRXx6U8ABQ",
    "Levitating": "https://www.youtube.com/watch?v=kTtB0v3bxw0",
    "Peaches": "https://www.youtube.com/watch?v=tQ0yjYUFKAE",
    "Save Your Tears": "https://www.youtube.com/watch?v=XXYlFuWEuKI",
    "Girls Like You": "https://youtu.be/aJOTlE1K90k?si=kBuRguFXRn3FQxTp",
    "Faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
    "Akhar":"https://youtu.be/_7kgU0lyVhw?si=v5t-CFfinFDQ2ebP",
    "Baby":"https://youtu.be/kffacxfA7G4?si=r4nQj9smzcaiQ_9q",
    "Dusk Till Dawn":"https://youtu.be/tt2k8PGm-TI?si=LQGOpzMS910I82eG",

    "Bad Guy": "https://www.youtube.com/watch?v=DyDfgMOUjCI",
    "Old Town Road": "https://www.youtube.com/watch?v=r7qovpFAGrQ"
}


st.markdown("# AUDIO AND VIDEO PLAYER")
choosing=st.radio(
      'What you would like to hear?',
      ['Choose one','Video','Audio','Play developer Favorite'],
      index=0
)
if choosing=='Video':
 file_upload=st.file_uploader("Upload a file",type=["mp4", "avi", "mov", "mkv"])

 if file_upload:
    st.write("Thank you!")
    
    st.video(file_upload)
elif choosing=='Audio':
   file_upload=st.file_uploader("Upload a file",type=["mp3", "wav", "ogg"])

   if file_upload:
    st.write("Thank you!")
    
    st.audio(file_upload)
elif choosing=='Play developer Favorite':
  chooseee=st.selectbox(
    'Choose one',
    list(songs.keys()),
    index=0
  )
  if chooseee:
    url=songs[chooseee]
    play=st.video(url)
  
  
 
