# Nature's Hidden Moments

This Docker image is for a Telegram bot that posts AI generated images of animals doing wild things to a channel every 12 hours. The images are generated using OpenAI's DALL-E 3 API, based on prompts created from a CSV file. Each image is overlaid with metadata before being posted to the Telegram channel.

## Features

- **Automatic Image Generation**: Uses OpenAI's DALL-E 3 API to generate images based on dynamic prompts.
- **Custom Overlay Text**: Adds a datestamp and random cardinal direction to each image.
- **Scheduled Posting**: Automatically posts to the specified Telegram channel every 12 hours.

## Setup

Before building and running the Docker image, ensure you have the following:

1. **OpenAI API Key**: Required for accessing the DALL-E 3 API.
2. **Telegram Bot Token**: Your Telegram bot's token.
3. **Telegram Channel ID**: The ID of the Telegram channel where images will be posted.

## Building & running the Docker image

To build the Docker image, use the following command, replacing img_name with the desired name for your Docker image:
```bash
docker build -t img_name .
```

To run the Docker container, use the following command:

```bash
docker run -d --env OPENAI_KEY=your_openai_key --env TELEGRAM_BOT_TOKEN=your_telegram_bot_token --env TELEGRAM_CHANNEL=@your_telegram_channel img_name
```

Replace the following:

- `your_openai_key` with your OpenAI API key.
- `your_telegram_bot_token` with your Telegram bot's token.
- `@your_telegram_channel` with the Telegram channel ID.
- `img_name` with the name of your Docker image.


**Notes:**
- Each row in these columns is randomly combined to create unique prompts for image generation. I have provided an example CSV with some data prefilled, feel free to change any that you desire. 
- Ensure the bot has administrative permissions in the Telegram channel for posting images. Customize the pixelify.ttf font path in the script if a different font is desired for the image overlay.

##Licenses
- Font: Obtained from https://github.com/eifetx/Pixelify-Sans with the SIL Open Font License available at https://github.com/eifetx/Pixelify-Sans/blob/main/OFL.txt
- This appliance: Available and distributable under an MIT license.