# Google_API_speechtotext
Google_API_speechtotext
//=====================================================================
1. transfer the mp3 files in path: ./resource/audio_mp3 into flac file and
   save it into path: ./resource/audio_flac.
2. upload the flac file into google storage
3. translate speech to text
4. save the result of text into path: ./resource/text
//=====================================================================                                                         
to achieve this code you need to:
1. Make sure you create a google API lience in the current folder, Ex: MyProject-%%%%%%%%%%%%%%.json
2. Enter the following code:
$export GCLOUD_PROJECT= YOUR PROJECT NAME(EX: western-grid-%%%%%%%)
$gcloud auth activate-service-account --key-file=MyProject-%%%%%%%%%%%%%%.json
$gcloud auth application-default print-access-token
3. After that you should got your token, copy it into the upload.py 
