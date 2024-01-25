# Flet Template Marketplace

## Installation:

Clone this repository:

```
$ git clone https://github.com/ZeroCool940711/flet-template-marketplace.git
```

Install the dependencies:

```
$ pip install -r requirements.txt
```

Run the code:

```
# Run the main file using python
$ python main.py

# or with Flet using hot reloading. Better for development.
$ flet run main.py -d
```

## Troubleshooting

If the first time you run the code you get the following error:

```
page.title = options["app_title"]
                 ~~~~~~~^^^^^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

You must run the code without the `-d` flag or with python directly. This is because the first time you run the code, the database is created but Flet will reload as soon as any file for the db is created so it cant finish creating it properly. After the first run, you can use the `-d` flag to enable hot reloading.