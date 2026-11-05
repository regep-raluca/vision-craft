import matplotlib.pyplot as plt

from image_processing import (
  load_image,
  convert_to_grayscale,
  apply_gaussian_blur,
  detect_edges,
  segment_image
)

def main():
  # Load the original image.
  image_path = r"C:\Users\raluc\OneDrive\Desktop\vision-craft\images\flowers-jar.jpg"
  image = load_image(image_path)

  # Apply image processing operations.
  grayscale = convert_to_grayscale(image)
  blurred = apply_gaussian_blur(grayscale)
  edges = detect_edges(image)
  segmented = segment_image(image, k=5)

  # Display all processing results in one figure.
  plt.figure(figsize=(15, 9))

  plt.subplot(2, 3, 1)
  plt.imshow(image)
  plt.title("Original Image")
  plt.axis("off")

  plt.subplot(2, 3, 2)
  plt.imshow(grayscale, cmap="gray")
  plt.title("Grayscale Image")
  plt.axis("off")

  plt.subplot(2, 3, 3)
  plt.imshow(blurred, cmap="gray")
  plt.title("Gaussian Blur")
  plt.axis("off")

  plt.subplot(2, 3, 4)
  plt.imshow(edges, cmap="gray")
  plt.title("Edge Detection (Canny)")
  plt.axis("off")

  plt.subplot(2, 3, 5)
  plt.imshow(segmented)
  plt.title("K-Means Segmentation")
  plt.axis("off")

  # Adjust spacing and display the figure.
  plt.tight_layout()
  plt.show()

if __name__ == "__main__":
  main()