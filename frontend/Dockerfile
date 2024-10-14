FROM node:lts AS builder

WORKDIR /app
COPY package.json .

RUN npm install
COPY . .
ENV VITE_API_URL=http://127.0.0.1:8123
RUN npm run build

FROM nginx:latest
WORKDIR /app
RUN rm -rf /usr/share/nginx/html/
COPY --from=builder /app/dist/ /usr/share/nginx/html/

EXPOSE 80
