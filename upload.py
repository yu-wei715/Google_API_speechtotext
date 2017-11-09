# Imports the Google Cloud client library
from google.cloud import storage
#convert liberary
import os, subprocess,re
import argparse
def upload_blob(bucket_name, source_file_name, destination_blob_name):
  """Uploads a file to the bucket."""
  # Instantiates a client
  storage_client = storage.Client()
  # get bucket
  bucket = storage_client.get_bucket(bucket_name)
  #output file name
  blob = bucket.blob(destination_blob_name)
  blob.upload_from_filename(source_file_name)

def delete_blob(bucket_name, blob_name):
  #Deletes a blob from the bucket.
  storage_client = storage.Client()
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.blob(blob_name)
  blob.delete()

def mp3toflac(filename):
  # convert to .wav
  f_file='./resource/audio_flac/'+filename + '.flac'
  m_file='./resource/audio_mp3/'+filename + '.mp3'
  cmd='ffmpeg -i '+ m_file+ ' -ac 1'+ '  ' +f_file
  #convert file
  os.system(cmd)

def writejson(try_nymber):
  with open('sync-request.json', 'r') as file :
    filedata = file.read()
  replaced = re.sub(r'[0-9]+\.flac',try_nymber,filedata)
  with open('sync-request.json', 'w') as file:
    file.write(replaced)

def gettranslate(txt_number):
  output = subprocess.check_output(["curl", "-s","-H","Content-Type: application/json",\
  "-H","Authorization: Bearer %/ENTER THE TOKEN/% ",\
  "https://speech.googleapis.com/v1/speech:recognize","-d","@sync-request.json"])
  out=str(output,'utf-8')
  a=out.split('"')[7]
  txt_name='./resource/text/'+txt_number+'.txt'
  file=open(txt_name, 'w')
  filedata = file.write(a)
  file.close()



if __name__ == "__main__":
  path = "./resource/audio_mp3"
  files = os.listdir( path )
  #find your mp3 file
  for file in files:
    f=file.split('.')[0]
    #transfer mp3 to flac
    mp3toflac(f)
    f_file='./resource/audio_flac/'+f + '.flac'
    flac_name=f+'.flac'
    #upload
    upload_blob('%/bucket_name/%',f_file,flac_name)
  for file in files:
    f=file.split('.')[0]
    flac_name=f+'.flac'
    #change the request fson
    writejson(flac_name)
    gettranslate(f)
  '''
  for file in files:
    f=file.split('.')[0]
    flac_name=f+'.flac'
    delete_blob('forspeech',flac_name)
  '''
