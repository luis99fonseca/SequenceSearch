def check_complementary(dir01, dir02):
    if not dir01 or not dir02:  # check if any vector is None
        return False
    return dir01[0] + dir02[0] == 0 and dir01[1] + dir02[1] == 0


def get_complementary(dir01):
    return dir01[0] * -1, dir01[1] * -1
