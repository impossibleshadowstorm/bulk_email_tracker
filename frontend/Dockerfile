FROM node:20.10.0

ADD . /app/

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

ENV NODE_PATH /app/node_modules

VOLUME ${NODE_PATH}

COPY package.json /app/package.json

RUN yarn install

CMD ["yarn", "run", "dev"]