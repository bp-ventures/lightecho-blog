To build the site:
```
poetry install

./generate.sh
```
Then, commit the changes, including the `output` directory.

To serve in production, use this Nginx config:
```
...
server_name blog.lightecho.io;
root /home/bp-blog/lightecho-blog/output;
index index.html;
location / {
    try_files $uri $uri/ =404;
}
...
```

To serve locally (for debug):
```
cd output
python -m http.server -d .
```
