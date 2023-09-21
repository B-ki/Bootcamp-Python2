from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    img_array = ft_load("../animal.jpeg")
    print("Printing the array is the equivalent to print")
    print(f"[0][0] : {img_array[0][0]}")
    print(f"[0][1] : {img_array[0][1]}")
    print(f"[0][2] : {img_array[0][2]}")
    print("...")
    print(f"[767][1021] : {img_array[767][1021]}")
    print(f"[767][1022] : {img_array[767][1022]}")
    print(f"[767][1023] : {img_array[767][1023]}")
    print("So now want to find :")
    print(" - The image converted to red only")
    print(" - An array of 400 x 400 x 1")
    print(" - With [0][0] = 167, [0][1] = 180, [0][2] = 194")
    print("Possible start pixel :")
    red_image = img_array[:, :, 0]
    for i in range(red_image.shape[0]):
        for j in range(red_image.shape[1]):
            if (red_image[i][j] == 167
                    and j < 1022
                    and red_image[i][j+1] == 180
                    and red_image[i][j+2] == 194):
                print(f"[{i}][{j}]")
    new_array = red_image[100:500, 450:850]
    fig, ax = plt.subplots()
    ax.imshow(new_array, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
