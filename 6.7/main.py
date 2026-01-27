# selection sort

import time 
from PIL import Image 

def is_target_function(pixel):
    # returns True if a pixel represents green vegetation
    r, g, b, = pixel
    return g > r + 20 and g > b + 20

def analyze_image(filename):
    # opens an image and calculates vegetation density
    image = Image.open("images/" + filename).convert("RGB")
    width, height = image.size
    pixels = image.load()

    vegetation_pixels = 0
    total_pixels =  width * height

    # Loops through every pixel
    for x in range (width):
        for y in range(height):
            if is_target_feature(pixels[x, y]):
                vegetation_pixels += 1

    return vegetation_pixels / total_pixels

def selection_sort(results):
    # sorts(filename, score) pairs from highesr to lowest score
    for i in range(len(results)):
        max_index = i
        for j in range(i + 1, len(results)):
            if results[j][1] > results[max_index][1]:
                max_index = i

        results[i], results[max_index] = results[max_index], results[i]

    return results

def binary_search(sorted_results, target):
    # searches for a target scoren using binary search 
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
    # list of image filenames (add images later)
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

    start_time = time.time()

    for filename in image_files:
        try:
            score = analyze_image(filename)
            results.append((filename, score))
        except:
            print("Could not process {filename}")

    end_time = time.time()
    elapsed = end_time - start_time

    print("Pixel processing completed in {elapsed:.3} seconds")

    # sort results
    sorted_results = selection_sort(results)

    # output top 5 
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

main()








'''
scores = [39, 2, 103, 42, 50, 61]

for i in range(len(scores)):
    smallest_score = scores[i]
    smallest_index = i

    for j in range(i+1, len(scores)):
        if scores[j] < smallest_score:
            smallest_score = scores[j]
            smallest_index = j
    
    scores[smallest_index], scores[i] = scores[i],
        scores[smallest_index]

print(scores)
'''
