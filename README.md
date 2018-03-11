First, get Cookiecutter. Trust me, it's awesome:

`$ pip install "cookiecutter>=1.4.0"`

Now run it against this repo:

`$ cookiecutter https://github.com/murarisumit/cookiecutter-chalice`

You'll be prompted for some values. Provide them, and you'll have aws lambda function file structure created.

* Test locally
    * `chalice local --port=8080`

* Create a new enviornment
    * `chalice deploy --stage prod`

* View url of various stage
    * `chalice url --stage dev`
    * `chalice url --stage prod`

* To see all deployed version.
    * `cat .chalice/deployed.json`

* Delete app
    * `chalice delete --stage dev`


TODO: 
    * Some sample code for api-key integration.
