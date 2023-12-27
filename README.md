# 🗣️VIO-Chatbot

### ❓About
<p>
  This project uses <b>Python 3</b> and <b>Open AI API</b> to create a <b>Voice Input-Output</b> chatbot [thus, the name].<br><br>
  This is an attempt to create a chatbot similar to Jarvis (Yes, the one from Avengers), though, as one may expect, 
  the performance of this model is dependent on the performance of the API provided by OpenAI and the voice recognition function of the device on which it is run. Also, I
  have used the <b>text-davinci-003</b> engine as it gave faster responses at that time. This might change with time, so please note that one may refer to the 
  OpenAI API documentation. (I have not attached the link as the earlier link is broken since their website has changed).
</p>

### 👀 Expectations
<p>
  <h4>What can you expect from the chatbot?</h4>
  Basically, everything that Chat GPT can do can be practically done with this.
  You can further customise the code by giving input to the model beforehand so that it changes how you want it to work without needing to prompt every time. This is similar to giving custom instructions to ChatGPT.<br>
  Thus, the generality and the features of ChatGPT are still preserved in this model!<br>
  For example, you can make it mimic someone famous if you want as well. Then, the program will start working as if it is mimicking someone.
  You will add the following lines before the code enters the never-ending `while` loop.
</p>

```
requirement="Act as if you are Sachin Tendulkar and answer further questions in that manner". # Or any other valid command
generate_response=(requirement)
while(True)
# The code continues...
```

### ❗Requirement

<p>
  Before starting the chatbot, don't forget to replace the dummy key with your OpenAI key at line 7.
</p>

📝For getting your own OpenAI key, follow the following link :
<a href="https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/">Link to get API key</a>.
(If the link is broken, search the internet for how to create an OpenAI API key.)
