import pika, json

import pika.spec

def upload(f, fs, channel, access):
  try:
    fid = fs.put(f)
  except Exception as err:
    print('err1: ', err, flush=True)
    return "Internal server error", 500
  
  message = {
    "video_fid": str(fid),
    "mp3_fid": None,
    "username": access["username"],
  }

  try:
    channel.basic_publish(
      exchange="",
      routing_key="video",
      body=json.dumps(message),
      properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
      )
    )
  except Exception as err:
    print('err2: ', err, flush=True)
    fs.delete(fid)
    return "Internal server error", 500