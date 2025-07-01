# Domain Scraping Script
You will find below a script that takes an URL and returns all the sub domains from this URL that are that page. 
You will find the Dockerfile & 2 Kubernetes YAML files to use this script on your instances.

**The Script** 
The `pyscript.py` script takes 2 arguments :
-u : the URL you want to extract URLs from (you can put as much as URLs you want but you have to put the -u argument before)
-o : the type of output you want (json or stdout) 
command line example : 
`./pyscript.py -u "https://www.google.com" -u "https://google.fr" -o json` => extracts all URLs from https://google.com & https://google.fr   

**Dockerfile** 
Build the Dockerfile if you want to use it as a Docker container :
`docker build -t pyscraper .`
Then use this command : (with the options you need)
`docker run --rm -it pyscraper -u https://google.com -o json`

**Kubernetes** 
You can modify the `static-scrapingjob.yaml` and modify the args with what you need or parse the args with the `flex-scrapingjob.yaml` file and this command line : 
`URL="https://news.ycombinator.com" OUTPUT="stdout" envsubst < flex-scrapingjob.yaml | kubectl apply -f -` (envsubst needed)

**CI/CD Integration**
If you want to implement this in a CI/CD pipeline, you will find the recommanded instructions in `cicd-deployment-steps.txt`

**Other**
You will find ways to extract a domain from different common ways to write a domain name. 
examples are in `input.txt` and you will find the 2 possible command line to execute in `waystoextracturls.txt`

**To go further**
This code sample is an introduction to web scraping and may be used to help you for web-mapping
