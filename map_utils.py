def calculate_spn(object_size):
    scale_factor = 0.1
    spn_x = (object_size / 1000) * scale_factor
    spn_y = (object_size / 1000) * scale_factor
    return spn_x, spn_y
