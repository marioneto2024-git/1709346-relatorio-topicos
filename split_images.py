from split_image import split_image
split_image("dataset_tp/IMG_3784.jpg", 10, 10, False, False, output_dir="./output/")
#split_image(image_path, rows, cols, should_square, should_cleanup, [output_dir])
# e.g. split_image("bridge.jpg", 2, 2, True, False)