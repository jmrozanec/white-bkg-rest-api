DIRECTORY="/Users/jorozanec/other/repo/private/rest-api"
curl -F "userid=1" -F "filecomment=This is an image file" -F "file=@$DIRECTORY/amazon-s3.png" localhost:80/upload
