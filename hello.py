import numpy as np
tiny_image = np.array([[
                            [0.1, 0.2, 0.3],
                            [0.4, 0.5, 0.6],
                            [0.7, 0.8, 0.9]
                        ],
                       [
                            [0.11, 0.22, 0.33],
                            [0.44, 0.55, 0.66],
                            [0.77, 0.88, 0.99]
                        ],
                       [
                            [0.111, 0.222, 0.333],
                            [0.444, 0.555, 0.666],
                            [0.777, 0.888, 0.999]
                        ]
                       ])
print(tiny_image)
print(tiny_image.shape)
plot_one_image(tiny_image)