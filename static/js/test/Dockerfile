FROM node

#Get the package.json into the container
ADD package.json /package.json
WORKDIR /
RUN npm install
VOLUME /test

#We assume that the source is mounted at /test (docker run -v /strava-yoy/static/js:/test strava-yoy:unit)
CMD diff /test/package.json /package.json && /test/test.sh