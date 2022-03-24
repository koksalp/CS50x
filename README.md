# CS50 Translate App
#### Video Demo: https://youtu.be/EvIMoxJny5U
#### Description:
A simple chrome extension for translating texts using an API.
Text based contents can be translated between two languages in short period of time.
There are bunch of other features that user can do such as switching between languages and setting a default language.
A notification shows up when user set a default language and after closing and re-entering the extension, default language is selected for user automatically.
The program makes API calls for getting all the supporting languages and translating text user enters.
This extension is inspired by google translate, thus features are similar .
User can only enter text to the input section, he can not enter anything to the translated text area.
Setting a default language is another useful feature that makes user's life easier.
Especially for someone who uses only a specific language to translate to can get benefit from this feature.
For example, a german person trying to learn english language only needs english language as target language because he may want  to know the meaning of a word or a text in english most of the times.
HTML, CSS and Javascript are used to implement this project.

In the project directory, there are number of images and files.

popup.html contains all the HTML for the project.

popup.css describes the styling of the elements in HTML file.
Some elements should change color when hover or need to be placed well enough to make whole extension look good.
Spaces between elements must be planned in such a way that it should not bother user.
This is a small extension that contains only one page so there are not so many things to consider.
popup.js file contains all the logic needed for the project.
It describes what should happen when a button is clicked or anything else related to user interaction.
API calls are used for several reasons.
One of them is for getting all the suported languages and the other one is for translating text.
It sends a GET request to get supported languages and place them into the dropdown list in HTML as option tags using Javascript.
When user enters a text and clicks on the translate button, a POST request is sent to the API route and the translation in response which is a JSON object is placed into translation field.

Since this is a chrome extension, a file named manifest.json exists.
It includes the necessary information that describes the characteristic of this extension and tells browser how it should behave when installed.

Image files with .png extension are use to increase the visuality.
The image named change.png is used for describing the button where user can switch between two languages.
All the other images are just different size of the same image. Both of them needs to be in manifesst.json for several reasons.
