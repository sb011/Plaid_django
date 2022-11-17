# Plaid_django

Plaid is an account aggregation service where users can login with their bank credentials and plaid fetches last two years of transaction and account balance data for their bank account. This project is its implementation using Django.

* Item, a set of credentials (map of key value pairs) associated with a financial institution and a user.
* Users can have multiple Items for multiple financial institutions.
* Each Item can have many associated accounts, which hold information such as balance, name, and account type

<img src="https://user-images.githubusercontent.com/75966962/202279334-7f94676b-e460-42de-af0a-2fe727118bc5.jpg">

## Django rest Apis for signup, login and logout

`api/signup/` - Create user using username, email and password

`api/login/` - Login using username and password

`api/logout/` - Logout using knox token


## Fetch and store data from Plaid Apis

`api/get_access_token/` - Exchange public token with access token

`api/get_transactions/` - Get transactions from plaid api

`api/identity/` - Retrieve Identity information on file with the bank.

`api/accounts/` - Retrieve high-level information about all accounts associated with an Item.

`api/balance/` - Gets all the information about balance of the Item.

`api/item/` - Retrieve information about an Item, like the institution, billed products, available products, and webhook information.


## Webhooks
    
`api/webhook/` - Transactions Webhook


## Description

Databse is SQLite

Start the rabbitmq server - `rabbitmq-server`

Async tasks handled by celery - `celery -A plaid_django worker -l info`

Localhost exposed using ngrox for webhooks - `./ngrox http 8000`

## Run Server
After setting up all the things you need to migrate the changes, create admin user and run the server:

    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
