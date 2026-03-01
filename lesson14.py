import numpy as np
from PIL import Image


# ---------------- Task 1 ----------------
# Fahrenheit to Celsius with numpy.vectorize

def f_to_c(F):
    return (F - 32) * 5/9

temps = np.array([32, 68, 100, 212, 77])

vector_func = np.vectorize(f_to_c)

celsius = vector_func(temps)

print("Task 1 - Celsius:")
print(celsius)



# ---------------- Task 2 ----------------
# Power function with numpy.vectorize

def power_func(x, p):
    return x ** p

numbers = np.array([2,3,4,5])
powers = np.array([1,2,3,4])

vector_power = np.vectorize(power_func)

result_power = vector_power(numbers, powers)

print("\nTask 2 - Powers:")
print(result_power)



# ---------------- Task 3 ----------------
# Solve linear equations

A = np.array([
    [4,5,6],
    [3,-1,1],
    [2,1,-2]
])

b = np.array([7,4,5])

solution = np.linalg.solve(A,b)

print("\nTask 3 Solution (x,y,z):")
print(solution)



# ---------------- Task 4 ----------------
# Electrical circuit equations

A2 = np.array([
    [10,-2,3],
    [-2,8,-1],
    [3,-1,6]
])

b2 = np.array([12,-5,15])

currents = np.linalg.solve(A2,b2)

print("\nTask 4 Currents (I1,I2,I3):")
print(currents)



# ---------------- Image Manipulation ----------------

# Load image
image = Image.open("images/birds.jpg")

img_array = np.array(image)



# 1 Flip Image

def flip_image(img):

    horizontal = np.fliplr(img)

    vertical = np.flipud(img)

    return horizontal, vertical


h_flip, v_flip = flip_image(img_array)

Image.fromarray(h_flip).save("flip_horizontal.jpg")
Image.fromarray(v_flip).save("flip_vertical.jpg")



# 2 Add Noise

def add_noise(img):

    noise = np.random.randint(0,50,img.shape,dtype='uint8')

    noisy_img = img + noise

    noisy_img = np.clip(noisy_img,0,255)

    return noisy_img.astype('uint8')


noise_img = add_noise(img_array)

Image.fromarray(noise_img).save("noise.jpg")



# 3 Brighten Red Channel

def brighten_red(img,value=40):

    bright = img.copy()

    bright[:,:,0] = np.clip(bright[:,:,0] + value,0,255)

    return bright.astype('uint8')


bright_img = brighten_red(img_array)

Image.fromarray(bright_img).save("bright_red.jpg")



# 4 Apply Mask

def apply_mask(img):

    masked = img.copy()

    h,w,_ = masked.shape

    center_h = h//2
    center_w = w//2

    masked[
        center_h-50:center_h+50,
        center_w-50:center_w+50
    ] = [0,0,0]

    return masked.astype('uint8')


mask_img = apply_mask(img_array)

Image.fromarray(mask_img).save("masked.jpg")