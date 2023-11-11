import openai
import requests

def generate_and_save_image(prompt):
    openai.api_key = 'your-api-key-here'

    try:
        # Generate image URL from DALL-E 3
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']

        # Download and save the image
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            filename = f'image_{prompt.replace(" ", "_")}.png'
            with open(filename, 'wb') as f:
                f.write(image_response.content)
            print(f"Image saved as {filename}")
        else:
            print("Failed to download the image")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
generate_and_save_image("A futuristic cityscape at night")
