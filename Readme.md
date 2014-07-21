# the concept:

- the user signup on the website
- once he is logged he can download an app
- once the app is installed, the user launch
- at the first launch the app call a specific url of the website to open it in safari
- this endpoint retreive the session information and call back the app with an url scheme
- back in the app, this one retrive the session information by exploding the parameters from the URL

next idea : use a temporary token for the web to app communication and use this token from the app to call a webservice and retrieve the full session.

# About

Live version on heroku : [http://follow-web-to-app.herokuapp.com/](http://follow-web-to-app.herokuapp.com/)
a simple iOS client is available on this repo : (ios-client)[ios-client]

## Proof of concept

This is just a proof of concept/test for a web to app session workflow and also a first time for Flask and me.

### todo :
- web : templating + web mobile
- security : basic webform security
- security : sso token valid only for few minutes
- security : call the client app with the token + call a webservice with the token from the app to get the full session