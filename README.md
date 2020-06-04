# apis
## TO RESGISTER NEW USER
url - 127.0.0.1:8000/api/v1/register/
request_type = Post
sample-request

{
"username":"username",
"Name":"Name",
"password":"password",
"gender":"male",
"phone_number":"7777123",
"dob":"02/09/1888",
"friends":"aman,nikky"
}
 
 sample response
 {
    "response": "user created successfully"
}

##username and phone number should be unique 
## phone number should contain integer only
## friends contain the username of already registered user

## LOGIN Using Token 

url - 127.0.0.1:8000/api/v1/auth/login/
request type = post

sample request
{
"username":"username",
"password":"password"
}

sample response
{
    "token": "1bb3889246300703e74c0794f2094677c9c6e979"
}

## list My profile details
url - 127.0.0.1:8000/api/v1/app/
request type = get

sample response
[
    {
        "id": 22,
        "username": "username",
        "Name": "Name",
        "gender": "male",
        "profile_pic": null,
        "city": null,
        "state": null,
        "phone_number": "7777123",
        "country": null,
        "friends": [
            "nikky",
            "aman"
        ]
    }
]

### change my profile details
url - 127.0.0.1:8000/api/v1/app/
request type = patch

sample request

{
"phone_number":"123456789"
}

sample response
{
    "id": 22,
    "username": "username",
    "Name": "Name",
    "gender": "male",
    "profile_pic": null,
    "city": null,
    "state": null,
    "phone_number": "123456789",
    "country": null,
    "friends": [
        "nikky",
        "aman"
    ]
}

## list details of other profile

url - 127.0.0.1:8000/api/v1/list/
request type - get

## add address
url = http://127.0.0.1:8000/api/v1/address/
request type - post

sample request

{
"Street_add":"streeaddress",
"city":"city",
"state":"usernamestate",
"pincode":"1234",
"country":"usernamecountry"
}
sample response
{
    "Street_add": "streeaddress",
    "city": "city",
    "state": "usernamestate",
    "pincode": "1234",
    "country": "usernamecountry"
}

## update address
url = http://127.0.0.1:8000/api/v1/address/
request type - patch 

sample request

{
"city":"username city"
}

sample response

{
    "id": 5,
    "Street_add": "streeaddress",
    "city": "username city",
    "state": "usernamestate",
    "pincode": "1234",
    "country": "usernamecountry"
}

## to list other profile and filter by gender

url - 127.0.0.1:8000/api/v1/list/?gender=female
request type - get



