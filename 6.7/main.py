import time 
from PIL import Image 

# this function determines if a pixel is green vegetation based on RGB values of the piel
def is_target_feature(pixel):
    # returns True if a pixel represents green vegetation
    r, g, b, = pixel
    return g > r + 20 and g > b + 20

# Algorithms: looops through every pixel in the image, counts the pixels that atch the target feature, divide by total pixels to get a density score
def analyze_image(filename):
    # opens an image and calculates vegetation density
    image = Image.open("6.7/images/" + filename).convert("RGB")
    # gets image dimensions
    width, height = image.size
    pixels = image.load()

    vegetation_pixels = 0
    total_pixels =  width * height

    # Loops through every pixel in the image
    for x in range (width):
        for y in range(height):
            if is_target_feature(pixels[x, y]):
                vegetation_pixels += 1

# return vegetation density score
    return vegetation_pixels / total_pixels

# Algorithms: repeatedly find the image with the highest score, swpas it into the correct position
def selection_sort(results):
    # sorts(filename, score) pairs from highesr to lowest score
    for i in range(len(results)):
        max_index = i
        for j in range(i + 1, len(results)):
            if results[j][1] > results[max_index][1]:
                max_index = j

        # swaps current element with the highest remainig element
        results[i], results[max_index] = results[max_index], results[i]

    return results

# Algorithms: repeatedly divide the search space in half, compare mid score to target score
def binary_search(sorted_results, target):
    # searches for a target score using binary search 
    low = 0 
    high = len(sorted_results) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_score = sorted_results[mid][1]

        if abs(mid_score - target) < 0.0001:
            return sorted_results[mid]
        elif mid_score < target:
            high = mid - 1
        else:
            low = mid + 1
    
    return None

def main():
    # list of image filenames to analyze
    images = [
        "image_1.jpeg",
        "IMG_5804.jpeg",
        "IMG_5805.jpeg",
        "IMG_5806.jpeg",
        "IMG_5808.jpeg",
        "IMG_5809.jpeg",
        "IMG_5810.jpeg",
        "IMG_5811.jpeg",
        "IMG_5812.jpeg",
        "IMG_5813.jpeg"
    ]

    results = []

    # start timing pixels
    start_time = time.time()

    # analyze each image and store results
    for filename in images:
        try:
            score = analyze_image(filename)
            results.append((filename, score))
        except:
            # handles case if the image cant be process
            print("Could not process", filename)

    # ends timing
    end_time = time.time()
    elapsed = end_time - start_time

    # output the time it took to 3 decimal places
    print(f"Pixel processing completed in {elapsed:.3f} seconds")

    # sort images by vegetation density
    sorted_results = selection_sort(results)

    # output top 5 images
    print("Top 5 images by vegetation density:")
    for item in sorted_results[:5]:
        print(item)

    # binary search example
    target_score = 0.50
    found = binary_search(sorted_results, target_score)

    if found:
        print("Binary search result:", found)
    else:
        print("No image found near target score")

# runs the program
main()