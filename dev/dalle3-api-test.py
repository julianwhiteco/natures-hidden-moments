import openai
import requests


def generate_and_save_image(prompt):
    openai.api_key = input('your-api-key-here ')

    try:
        # Generate image URL from DALL-E 3
        response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']

        # Download and save the image as 'image.jpg', overwriting if it exists
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            filename = 'image.jpg'
            with open(filename, 'wb') as f:
                f.write(image_response.content)
            print(f"Image saved as {filename}")
            return True
        else:
            print("Failed to download the image")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
generate_and_save_image("a Flying squirrel unexpectedly captured Crafting pottery in the Arctic ice caps. The perspective is from a grainy, blurry trail camera, adding a sense of the animal being photographed doing something unusual and secretive. The {location} environment forms the backdrop of this candid scene.")
