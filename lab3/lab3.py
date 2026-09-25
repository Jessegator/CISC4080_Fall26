"""
Lab 3: Sorting and Selection with Images
CISC 4080 Computer Algorithms

Complete ONLY the functions marked TODO:
    1. merge()
    2. merge_sort()
    3. partition()
    4. quick_sort()
    5. quick_select()

The remaining code is provided to load, convert, display, reshape,
mark, and save images.
"""

from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import random


# ============================================================
# Helper functions provided for you
# You do NOT need to modify this section.
# ============================================================

def show_image(img, title="Image"):
    """
    Display a Pillow image with Matplotlib.

    Matplotlib is useful in Jupyter/Colab because it displays the
    image directly inside the notebook/output area.
    """
    plt.figure()
    plt.imshow(img, cmap="gray" if img.mode == "L" else None)
    plt.title(title)
    plt.axis("off")
    plt.show()


def load_grayscale_image(path):
    """
    Load an image and convert it to grayscale.

    Pillow opens the image file.
    .convert("L") converts the image to 8-bit grayscale:
        0   = black
        255 = white

    np.array(img) converts the Pillow image into a 2-D NumPy array.
    If the image is H pixels tall and W pixels wide, its shape is (H, W).
    """
    img = Image.open(path).convert("L")
    pixels = np.array(img)

    height, width = pixels.shape

    print(f"Loaded grayscale image: {path}")
    print(f"Image size: {width} x {height}")
    print(f"NumPy array shape: {pixels.shape}")

    return img, pixels


def image_to_list(pixels):
    """
    Convert a 2-D image array into a normal 1-D Python list.

    Example:
        [[30, 10],
         [50, 20]]

    becomes:
        [30, 10, 50, 20]

    We flatten the image because the sorting algorithms in this lab
    operate on a one-dimensional list.
    """
    flat_array = pixels.flatten()

    # Convert NumPy's 1-D array into a regular Python list.
    pixel_list = flat_array.tolist()

    print(f"Total number of pixels: {len(pixel_list)}")
    return pixel_list


def save_grayscale_pixels(pixel_list, height, width, filename):
    """
    Turn a sorted 1-D pixel list back into an image.

    np.array(...) changes the Python list back into a NumPy array.
    reshape(...) restores the original H x W image dimensions.
    uint8 is the standard 0-255 integer representation used here.
    """
    pixel_array = np.array(pixel_list, dtype=np.uint8)
    image_array = pixel_array.reshape((height, width))

    # Convert the numerical matrix back into a Pillow image.
    result = Image.fromarray(image_array, mode="L")
    result.save(filename)

    print(f"Saved: {filename}")
    return result


# ============================================================
# PART I-A: MERGESORT
# ============================================================

def merge(left, right, ascend=True):
    """
    Merge two already-sorted lists into one sorted list.

    TODO:
        Implement the merge step of MergeSort.

    ascend=True  -> ascending order
    ascend=False -> descending order

    Do NOT use sorted() or list.sort().
    """
    # TODO: YOUR CODE HERE
    pass


def merge_sort(arr, ascend=True):
    """
    Return a NEW sorted list using MergeSort.

    TODO:
        1. Handle the base case.
        2. Divide the list into two halves.
        3. Recursively sort both halves.
        4. Merge the two sorted halves.

    Do NOT use sorted() or list.sort().
    """
    # TODO: YOUR CODE HERE
    pass


# ============================================================
# PART I-B: QUICKSORT
# ============================================================

def partition(arr, low, high, ascend=True):
    """
    Partition arr[low:high+1] around a pivot.

    TODO:
        Implement the partition operation used by QuickSort.

    You may choose a random pivot and move it to the end before
    performing the partition.

    After partitioning, return the FINAL INDEX of the pivot.

    ascend=True  -> smaller values should go toward the left
    ascend=False -> larger values should go toward the left

    Do NOT use sorted() or list.sort().
    """
    # TODO: YOUR CODE HERE
    pass


def quick_sort(arr, low, high, ascend=True):
    """
    Sort arr IN PLACE using QuickSort.

    TODO:
        1. Check the base case.
        2. Partition the current range.
        3. Recursively sort the left side.
        4. Recursively sort the right side.

    Do NOT use sorted() or list.sort().
    """
    # TODO: YOUR CODE HERE
    pass


# ============================================================
# PART II: QUICKSELECT
# ============================================================

def quick_select(arr, k):
    """
    Return the value that would appear at index k if arr were sorted
    in ascending order.

    TODO:
        Implement QuickSelect using partition().

    Important:
        QuickSelect should NOT completely sort the array.
        After each partition, continue only on the side containing k.

    Hint:
        You can call:
            partition(arr, low, high, ascend=True)

    Do NOT use sorted(), list.sort(), np.sort(), or np.partition().
    """
    # TODO: YOUR CODE HERE
    pass


# ============================================================
# PART I: SORT THE GRAYSCALE IMAGE
# You do NOT need to modify this section.
# ============================================================

def run_sorting_part():
    print("\n" + "=" * 60)
    print("PART I: SORTING A GRAYSCALE IMAGE")
    print("=" * 60)

    gray_path = "gray_image.png"

    # Load the file as a grayscale image and convert it to a 2-D
    # numerical matrix.
    gray_img, gray_pixels = load_grayscale_image(gray_path)

    # Save the original height and width. We need them later when we
    # reshape the sorted 1-D list back into an image.
    height, width = gray_pixels.shape

    # Convert the H x W matrix into a one-dimensional Python list.
    original_pixels = image_to_list(gray_pixels)

    show_image(gray_img, "Original Grayscale Image")

    # ---------------- MERGESORT: ASCENDING ----------------
    # .copy() is important: each algorithm should receive the same
    # original, unsorted pixel values.
    merge_ascending = merge_sort(original_pixels.copy(), ascend=True)

    result = save_grayscale_pixels(
        merge_ascending,
        height,
        width,
        "MergeSort_ascending_sorted_gray.png"
    )
    show_image(result, "MergeSort - Ascending")

    # ---------------- MERGESORT: DESCENDING ----------------
    merge_descending = merge_sort(original_pixels.copy(), ascend=False)

    result = save_grayscale_pixels(
        merge_descending,
        height,
        width,
        "MergeSort_descending_sorted_gray.png"
    )
    show_image(result, "MergeSort - Descending")

    # ---------------- QUICKSORT: ASCENDING ----------------
    quick_ascending = original_pixels.copy()

    # QuickSort modifies the list directly, so it does not need to
    # return a new list.
    quick_sort(
        quick_ascending,
        low=0,
        high=len(quick_ascending) - 1,
        ascend=True
    )

    result = save_grayscale_pixels(
        quick_ascending,
        height,
        width,
        "QuickSort_ascending_sorted_gray.png"
    )
    show_image(result, "QuickSort - Ascending")

    # ---------------- QUICKSORT: DESCENDING ----------------
    quick_descending = original_pixels.copy()

    quick_sort(
        quick_descending,
        low=0,
        high=len(quick_descending) - 1,
        ascend=False
    )

    result = save_grayscale_pixels(
        quick_descending,
        height,
        width,
        "QuickSort_descending_sorted_gray.png"
    )
    show_image(result, "QuickSort - Descending")


# ============================================================
# PART II: FIND A BRIGHTEST PIXEL
# You do NOT need to modify this section.
# ============================================================

def run_quickselect_part():
    print("\n" + "=" * 60)
    print("PART II: FIND A BRIGHTEST PIXEL WITH QUICKSELECT")
    print("=" * 60)

    color_path = "fordham.png"

    # Open the image and force RGB mode.
    # Every pixel now has three values: [R, G, B].
    img = Image.open(color_path).convert("RGB")

    # Convert the Pillow image into a NumPy array.
    # Its shape is (height, width, 3).
    pixels = np.array(img)
    height, width, channels = pixels.shape

    print(f"Loaded color image: {color_path}")
    print(f"Image size: {width} x {height}")
    print(f"Array shape: {pixels.shape}")
    print(f"Number of color channels: {channels}")

    show_image(img, "Original Color Image")

    # Separate the three color channels.
    # pixels[..., 0] means: take the red value from every pixel.
    # pixels[..., 1] means: take the green value from every pixel.
    # pixels[..., 2] means: take the blue value from every pixel.
    R = pixels[..., 0]
    G = pixels[..., 1]
    B = pixels[..., 2]

    # Convert the three RGB channels into ONE brightness channel.
    # Y is now a 2-D matrix with one brightness value per pixel.
    Y = 0.299 * R + 0.587 * G + 0.114 * B

    print(f"Brightness matrix shape: {Y.shape}")

    # QuickSelect works on a one-dimensional list, so flatten the
    # brightness matrix and convert it to a normal Python list.
    brightness_list = Y.flatten().tolist()

    # If the values were sorted in ascending order, index n - 1 would
    # contain the largest value. QuickSelect finds that value without
    # completely sorting the entire list.
    k = len(brightness_list) - 1

    brightest_value = quick_select(brightness_list.copy(), k)
    print(f"Brightest value found by QuickSelect: {brightest_value}")

    # Find coordinates in the ORIGINAL 2-D brightness matrix that have
    # the brightness returned by QuickSelect.
    #
    # There can be multiple pixels with the same maximum brightness.
    # We mark the first one.
    locations = np.argwhere(np.isclose(Y, brightest_value))

    if len(locations) == 0:
        raise ValueError("Could not locate the selected brightness in the image.")

    y, x = locations[0]

    # Pillow uses coordinates in (x, y) order:
    # x = horizontal position (column)
    # y = vertical position (row)
    x = int(x)
    y = int(y)

    print(f"Marked pixel coordinates: ({x}, {y})")

    # Draw a red circle and coordinate label around the selected pixel.
    marked_img = img.copy()
    draw = ImageDraw.Draw(marked_img)

    radius = 8
    draw.ellipse(
        (x - radius, y - radius, x + radius, y + radius),
        outline="red",
        width=3
    )
    draw.text((x + 10, y - 10), f"({x},{y})", fill="red")

    marked_img.save("fordham_marked.png")
    print("Saved: fordham_marked.png")

    show_image(marked_img, "A Brightest Pixel Found by QuickSelect")


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":
    # Run Part I.
    run_sorting_part()

    # Run Part II.
    run_quickselect_part()

    print("\nLab completed!")
