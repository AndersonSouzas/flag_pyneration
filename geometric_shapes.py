def paint_diagonally(img, color): ###just to understand how to paint using load()###
    canva = img.load()
    width, height = img.size
    
    a = (height - 1) / (width - 1)
    for i in range(width):
        for j in range(height):
            if a * i <= j:
                canva[i, j] = color
