
The project requires Google Chrome and `chromedriver` in the PATH.


Build

``` shell
DOCKER_BUILDKIT=0 docker build --tag crawler:latest .
```

Run

``` shell
docker run -p 3000:3000 -it crawler:latest
```