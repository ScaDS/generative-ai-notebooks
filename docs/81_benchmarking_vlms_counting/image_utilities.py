def numpy_to_bytestream(data):
    """Turn a NumPy array into a bytestream"""
    import numpy as np
    from PIL import Image
    import io

    # Convert the NumPy array to a PIL Image
    image = Image.fromarray(data.astype(np.uint8)).convert("RGBA")

    # Create a BytesIO object
    bytes_io = io.BytesIO()

    # Save the PIL image to the BytesIO object as a PNG
    image.save(bytes_io, format='PNG')

    # return the beginning of the file as a bytestream
    bytes_io.seek(0)
    return bytes_io.read()


def images_from_url_responses(response, input_shape = None):
    """Turns a list of OpenAI's URL responses into numpy images"""
    from skimage.io import imread
    from skimage import transform
    import numpy as np
    images = [imread(item.url) for item in response.data]

    if input_shape is not None:
        # make sure the output images have the same size and type as the input image
        images = [transform.resize(image, input_shape, anti_aliasing=True, preserve_range=True).astype(image.dtype) for image in images]

        if len(input_shape) == 2 and len(images[0].shape) == 3:
            # we sent a grey-scale image and got RGB images back
            images = [image[:,:,0] for image in images]

    if len(images) == 1:
        # If only one image was requested, return a single image
        return images[0]
    else:
        # Otherwise return a list of images as numpy array / image stack
        return np.asarray(images)

def extract_json(text:str):
    import re

    # fix trailing ,
    text = re.sub(r",\s*]", "]", text)
    
    # Extract the JSON content using re.DOTALL to make '.' match newlines as well
    pattern = r"(?<=```json)(.*?)(?=```)"
    return re.findall(pattern, text, re.DOTALL)[0]

def generate_spots(n, image_size=256, sigma=10):
    """
    Generate n random 2D coordinates and a corresponding RGB image with blurry white spots.
    
    Parameters:
    -----------
    n : int
        Number of spots to generate
    image_size : int
        Size of the square image (default 512)
    sigma : float
        Standard deviation of the Gaussian kernel for blurring (default 5)
        
    Returns:
    --------
    tuple : (list of coordinates, RGB image)
    """
    import numpy as np
    from scipy.ndimage import gaussian_filter
    
    # Generate random coordinates
    coordinates = []
    for _ in range(n):
        x = np.random.randint(0, image_size)
        y = np.random.randint(0, image_size)
        coordinates.append((x, y))
    
    # Create a blank black image
    image = np.zeros((image_size, image_size), dtype=np.float32)
    
    # Add white spots at the coordinates
    for x, y in coordinates:
        if 0 <= x < image_size and 0 <= y < image_size:
            image[y, x] = 1.0
    
    # Apply Gaussian blur to make spots blurry
    blurred_image = gaussian_filter(image, sigma=sigma)
    
    image = (blurred_image / blurred_image.max() * 255).astype(np.uint8)
    
    return coordinates, image


