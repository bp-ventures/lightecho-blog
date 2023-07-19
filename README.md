### Notes for blog maintainer/writer

You probably just need to worry about the `content` directory.

To add a new blog post:

1. Create a new `.md` file in `content/posts` directory
2. Add the headers (see the other `.md` files for reference)
3. Add the content
4. Either run `./generate.sh` (see below), or ask a developer to run it.
5. Server should automatically detect the changes and autodeploy to the blog.
6. If you're unsure if your changes have been automatically deployed, check
   the version file at `<blog url>/version.txt`. It contains the Git commit hash
   of the currently deployed version.

### Notes for developer

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
