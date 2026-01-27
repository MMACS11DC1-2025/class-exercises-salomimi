Theme: green vegetation in forest like images

The goal of this project is to analyze a set of images (10 images) and measure how much green vegtation appears in each one. The program processes the images and calculates a vegetation density score based on the number of pixels that match a green vegetation feature. The images are then sorted and analyzed using algorithms from units 5 and 6.

Visual Feature: The visual detected in the project is green vegetation. Vegetation is identified by analyzing the RGB values of each pixel in the image. 
A pixel is classified as green vegetation if:
-  the green value is significantly higher than the red value
-  the green value is significatly higher than the blue value. This makes the program to identify plants, grass and trees from non-vegation areas like the sky.

Feature Detection: Green vegetation typically reflects more green light compared to red and blue light. By checking whether the green part is at least 20 pixels higher than both the blue and red part, the program can reliably idetify pixels that are likely part of vegetation.

Image Processing: The program processes images using these steps:
- open each image and convert it to RGB format
- loops though each pixel in the image using nested loops 
- checks whether each pixel matches the green vegetation fetaure
- count th enumber of vegetation pixels 
- divide by the total number of pixels to calculet a vevgetation density

Algorythms:
- Slection sort:
    This algorythim is used to sort the images from highest to lowest vegetation density scor. After sorting, the program outputs the top 5 ikmages using list slicing.
- Binary Search:
    This algorythm is used to search the sorted lists for an mage with a specific target vegetation score. The algorythm kepss diving the search space in half until the target score is found or detemined to not exist.

Code Profiling: The program uses the time module to time how long pixel process takes. The elapsed time is printer in a readable format to 3 decimals.
example: Pixel processing completed in 2.112 seconds
The most timed part of the program is the nested pixel loops becays every pixel in every image is checked individually.

Testing & Validation: The program was tested by veifiying that all images load correctly. Then confirming that vegetation scores chnage based on image content. It checks that images are correctly sorted from highest to lowest score. It also tested the binary search with different target values. Ensures the program continues to run if an image fails to load.

Challenges Faced: One big challenge was loading the image file paths form the project directory. IT was fixed by fixing the file path so the program can find the image folder. Another challenge was making sure the function names matched throughout the entire code, because incorrect naming made the code to fail. Carefully inspecting the code helped fix this problem.