def prompt_anthropic(prompt:str, image=None, model:str = "claude-3-7-sonnet-20250219"):
    from anthropic import Anthropic

    client = Anthropic()
    
    if image is None:
        user_message = {
                    "role": "user",
                    "content": prompt,
                }
    else:
        user_message = image_to_message_claude(image, prompt)

    response = client.messages.create(
        messages=[user_message],
        model=model,
        max_tokens=8092,
    )
    reply = response.content[0].text

    return reply


def image_to_message_claude(image, prompt):
    import base64
    from image_utilities import numpy_to_bytestream

    from stackview._image_widget import _img_to_rgb

    rgb_image = _img_to_rgb(image)
    byte_stream = numpy_to_bytestream(rgb_image)
    base64_image = base64.b64encode(byte_stream).decode('utf-8')

    return {
            "role": 'user',
            "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": base64_image}},
                {"type": "text", "text": prompt}
            ]
        }

def prompt_openai(prompt:str, image, model="gpt-4o", base_url=None, api_key=None):
    """A prompt helper function that sends a message to openAI
    and returns only the text response.
    """
    import openai
    import base64
    from image_utilities import numpy_to_bytestream
    from stackview._image_widget import _img_to_rgb

    rgb_image = _img_to_rgb(image)
    byte_stream = numpy_to_bytestream(rgb_image)
    base64_image = base64.b64encode(byte_stream).decode('utf-8')

    message = [{"role": "user", "content": [
        {"type": "text", "text": prompt},
        {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
        }
    }]}]
            
    # setup connection to the LLM
    client = openai.OpenAI()
    if base_url is not None:
        client.base_url = base_url

    if api_key is not None:
        client.api_key = api_key
    
    # submit prompt
    response = client.chat.completions.create(
        model=model,
        messages=message
    )
    
    # extract answer
    return response.choices[0].message.content