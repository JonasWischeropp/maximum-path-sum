
type Triangle = list[list[int]]

def parse_triangle_file(file_name: str) -> Triangle:
    """"Assumes that the file content is a valid triangle."""
    layers: list[list[int]] = []
    with open(file_name) as file:
        for line in file:
            layers.append([int(number) for number in line.split(" ")])
    return layers

def calculate_maximum_path_sum(layers: Triangle) -> int:
    layer_iter = reversed(layers)
    try:
        # buffer to store intermediate results
        sums = next(layer_iter).copy()
    except StopIteration:
        return 0

    for layer in layer_iter:
        for i in range(len(layer)):
            sums[i] = layer[i] + max(sums[i], sums[i + 1])
    return sums[0]


if __name__ == "__main__":
    triangle = parse_triangle_file("triangle.txt")
    maximum = calculate_maximum_path_sum(triangle)
    print(f"Maximum sum: {maximum}")
