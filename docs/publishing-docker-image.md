# Publishing Docker Image

## Build

```shell
docker build -t quay.io/data-dynamos/data_dynamos_exercise .
```

## Push

Docker Images are pushed to [quay repository](https://quay.io/repository/data-dynamos/data_dynamos_exercise). Make sure you have access to push to the quay repository.

```shell
docker login quay.io
docker push quay.io/data-dynamos/data_dynamos_exercise
```
