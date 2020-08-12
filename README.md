# blur-images
Program to blur images in python
Usage:

blur.py [arguments] <image_path>

-b --blur_factor : Set the how blurred you want your image. (Default: 2)

-o --output_path : Set the output path of the blurred image. (Default: output.jpg)

-p --progress    : Show progress in percentage. (Warning: Will slow down the process)

Sim, engenheiros, a ordem de complexidade dessa porcaria é O(n(2b-1)²), sendo 'n' o tamanho da imagem, e 'b' o blur factor.
Lide com isso.
