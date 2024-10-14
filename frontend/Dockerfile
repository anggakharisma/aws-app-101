FROM node:lts AS builder

WORKDIR /app
COPY package.json .

RUN npm install
COPY . .
RUN npm run build

FROM nginx:latest
WORKDIR /app
RUN rm -rf /usr/share/nginx/html/
COPY --from=builder /app/dist/ /usr/share/nginx/html/

EXPOSE 80
