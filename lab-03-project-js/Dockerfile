FROM node:20-alpine3.16 

WORKDIR /app

COPY package*.json ./

RUN npm i

COPY . .

EXPOSE 8080

CMD [ "node", "app.js" ]