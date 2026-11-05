import cv2
import numpy as np

def load_image(image_path):
  """Load an image and convert it to RGB."""
  image = cv2.imread(image_path)

  if image is None:
    raise FileNotFoundError(
      f"Could not load image: {image_path}"
    )

  # OpenCV loads images in BGR format.
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  return image

def convert_to_grayscale(image):
  """Convert an RGB image to grayscale."""
  grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

  return grayscale

def apply_gaussian_blur(image):
  """Reduce image noise using Gaussian blur."""
  blurred = cv2.GaussianBlur(image, (15, 15), 0)

  return blurred

def detect_edges(image):
  """Detect edges using the Canny algorithm."""
  grayscale = convert_to_grayscale(image)
  blurred = apply_gaussian_blur(grayscale)

  edges = cv2.Canny(blurred, threshold1=30, threshold2=100)
  
  return edges

def segment_image(image, k=5):
  """Segment an image into k color clusters."""
  small_image = cv2.resize(image, (200, 200))

  # Convert image pixels into a list of RGB values.
  pixels = small_image.reshape((-1, 3))
  pixels = np.float32(pixels)

  # Stop when the maximum number of iterations is reached or the accuracy threshold is met.
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

  # Group similar pixels using K-Means clustering.
  _, labels, centers = cv2.kmeans(
    pixels,
    k,
    None,
    criteria,
    10,
    cv2.KMEANS_RANDOM_CENTERS
  )

  centers = np.uint8(centers)

  segmented_pixels = centers[labels.flatten()]
  segmented_image = segmented_pixels.reshape(small_image.shape)

  # Restore the original image dimensions.
  segmented_image = cv2.resize(
    segmented_image,
    (image.shape[1], image.shape[0]),
    interpolation=cv2.INTER_NEAREST
  )

  return segmented_image






 

