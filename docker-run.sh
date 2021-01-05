WORKSPACE=/workspace/app

docker run -v $(pwd):$WORKSPACE --name $IMG_NAME $IMG_NAME

# start project
# docker run -v $(pwd):$WORKSPACE $IMG_NAME
