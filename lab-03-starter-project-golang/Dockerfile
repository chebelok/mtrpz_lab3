# build stage
FROM golang:1.20.4-alpine3.17 AS builder
 
WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY . /app

RUN go build -o build/fizzbuzz

# run stage
FROM gcr.io/distroless/base-debian11

WORKDIR /app

COPY --from=builder /app/build/fizzbuzz ./
COPY --from=builder /app/templates/index.html ./templates/

EXPOSE 8080


CMD ["./fizzbuzz", "serve"]