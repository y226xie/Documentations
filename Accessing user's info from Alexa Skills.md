# Accessing user's contact information, and location info from alexa skills

* Currently, Amazon’s official docs does not provide 1 endpoint which can give us all info we need. They kept them separately.

### According to Amazon’s docs, we need to call 4 or 5 different endpoints :
* URL for email endpoint: https://api.amazonalexa.com/v2/accounts/~current/settings/Profile.email
* URL for name endpoint: https://api.amazonalexa.com/v2/accounts/~current/settings/Profile.name
* URL for phone endpoint: https://api.amazonalexa.com/v2/accounts/~current/settings/Profile.mobileNumber

### Phone Endpoint
#### Example of phone 
Request: 
```python
phone_res = requests.get(phone_url, headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(apiAccessToken)})

```
Response: 
* 200 OK - Successfully retrieved the requested information.
* 204 No Content - The query did not return any results.
* 403 Unauthorized - The authentication token does not have access to the resource.
```
{
  "countryCode" : "+1",
  "phoneNumber" : "999-999-9999"
}
```
Notes: 
* apiAccessToken can be grabbed from `context.System.apiEndpoint`
```python
{
  "version": "1.0",
  "session": {},
  "context": {
    "System": {
      "application": {
        "applicationId": "amzn1.ask.skill.<skill-id>"
      },
      "user": {},
      "apiAccessToken": "AxThk...",
      "apiEndpoint": "https://api.amazonalexa.com"
    }
  },
  "request": {}
}
```
* for more information, please check: https://developer.amazon.com/en-US/docs/alexa/custom-skills/request-customer-contact-information-for-use-in-your-skill.html#how-to-request-customer-contact-information

### Location endpoint
URL for location endpoint: https://api.amazonalexa.com/v1/devices/{deviceId}/settings/address/countryAndPostalCode

#### Example

Request: 
```python
location_res = requests.get(location_url, headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(apiAccessToken)})
```

Response: 
* 200 OK - Successfully retrieved the requested information.
* 204 No Content - The query did not return any results.
* 403 Unauthorized - The authentication token does not have access to the resource.

```
Host: api.amazonalexa.com
X-Amzn-RequestId: xxxx-xxx-xxx
Content-Type: application/json
{
  "countryCode" : "US",
  "postalCode" : "98109"
}
```
Note:
Both `deviceId` and `apiAccessToken` can be access from `context` object from Amazon
```python
{
  "context": {
    "System": {
      "apiAccessToken": "AxThk...",
      "apiEndpoint": "https://api.amazonalexa.com",
      "device": {
        "deviceId": "string-identifying-the-device",
        "supportedInterfaces": {}
      },
      "application": {
        "applicationId": "string"
      },
      "user": {}
    }
  }
}
```
* for more information, please check: https://developer.amazon.com/en-US/docs/alexa/custom-skills/device-address-api.html

### location services

For information of location services: https://developer.amazon.com/en-US/docs/alexa/custom-skills/location-services-for-alexa-skills.html

* `Geolocation` is a part of `context` object, and it can be accessed by `context.Geolocation`
* IMPORTANT: `Geolocation` will only be avaiable if user granted the permission, otherwise, it would not show up. We can check that by access `context.System.device.supportedInterfaces` and to see if it has a `Geolocation` field

#### a sample payload will be like:
```json
     "Geolocation":{ 
        "locationServices": { 
            "access": "ENABLED",
            "status": "RUNNING",   
        },
        "timestamp": "2018-03-25T00:00:00Z+00:00",
        "coordinate": {
            "latitudeInDegrees": 38.2,
            "longitudeInDegrees": 28.3,
            "accuracyInMeters": 12.1 
        },
        "altitude": {
            "altitudeInMeters": 120.1,
            "accuracyInMeters": 30.1
        },
        "heading": { 
            "directionInDegrees": 180.0,
            "accuracyInDegrees": 5.0  
        },
        "speed": { 
            "speedInMetersPerSecond": 10.0,
            "accuracyInMetresPerSecond": 1.1
        }       
      }
   }
```



