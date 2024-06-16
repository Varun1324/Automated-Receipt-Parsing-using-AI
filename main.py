import PIL.Image
import google.generativeai as genai

genai.configure(api_key="API_KEY")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
# Create the GenerativeModel instance
model = genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=generation_config,
    # You can adjust safety settings if needed
    # See https://ai.google.dev/gemini-api/docs/safety-settings
)


# response = model.generate_content("Hello Gemini")

# print(response.text)

def add_to_file(file_path,response_text):
  with open(file_path,'a') as file:
    file.write(response_text+'\n')
    file.write("--------------------------------------------------------------------------------"+'\n')


img = PIL.Image.open('invoice.png')
response = model.generate_content(["Extract item name, price, total amount from receipt. Display in tab-separated format with headings and date only once",img],stream=True)
response.resolve()
print(response.text)

file_path = 'data.txt'
add_to_file(file_path, response.text)