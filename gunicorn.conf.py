# all available confirguations for a gunicorn server
### where do we want to host the application
# bind = "0.0.0.0:17875"
bind = "0.0.0.0:17888"

### how performant do we want the application to be; want to find a good
### balance of performance and server capacity
workers = 3
threads = 1

### assigning the ssl/https private and public key files
certfile = "./secret/cert.pem"
keyfile = "./secret/certificate.key"
