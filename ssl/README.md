# 简单解释SSL的使用

编译环境: ubuntu

##创建证书和私钥
```
openssl genrsa -out privkey.pem 2048
openssl req -new -x509 -key privkey.pem -out cacert.pem -days 1095
```
###执行编译运行
```
gcc -g -o ssl_server ssl_server.c -lssl

gcc -g -o ssl_server ssl_server.c -lssl

./ssl_server 7838 1 127.0.0.1 cacert.pem privkey.pem

./ssl_client 127.0.0.1 7838
```
