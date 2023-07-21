# Publishing Docker Image

## Building and Testing

```shell
docker build -t quay.io/data-dynamos/data_dynamos_exercise .
docker run --rm -it quay.io/data-dynamos/data_dynamos_exercise bash
```

## Building and Publishing Images for Multiple Platforms

Docker Images are pushed to [quay repository](https://quay.io/repository/data-dynamos/data_dynamos_exercise). Make sure you have access to push to the quay repository.

```shell
# login using quay.io credentials
docker login quay.io

# creating a builder as default docker builder does not support building for multiple platforms
docker buildx create --use --platform=linux/arm64,linux/amd64 --name multi-platform-builder

# switch to and setup the created builder
docker buildx use multi-platform-builder
docker buildx inspect --bootstrap

# build the multi platform docker image and push to quay repository
docker buildx build --platform linux/arm64,linux/amd64 -t quay.io/data-dynamos/data_dynamos_exercise --push .
```
