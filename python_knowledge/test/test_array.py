def _check_version_is_bigger(version, min_version):
    if version == min_version:
        return True

    version_nums = version.split(".")
    min_version_nums = min_version.split(".")

    if len(version_nums) > len(min_version_nums):
        return True
    elif len(version_nums) < len(min_version_nums):
        return False
    else:
        for index, number in enumerate(version_nums):
            if int(number) == int(min_version_nums[index]):
                continue
            elif int(number) >  int(min_version_nums[index]):
                return True
            elif int(number) <  int(min_version_nums[index]):
                return False

        return False


def get_is_paid_course(platform, version):
    # android >= 2.11.0
    # ipad >= 1.9.0
    # iphone >= 2.9.0
    # ipod >= 2.9.0

    min_andorid = "2.11.0"
    mini_ipad = "1.9.0"
    mini_iphone = "2.9.0"
    mini_ipod = "2.9.0"

    if platform.lower() == 'android':
        return _check_version_is_bigger(version, min_andorid)
    elif platform.lower() == 'ipad':
        return _check_version_is_bigger(version, mini_ipad)
    elif platform.lower() == 'iphone':
        return _check_version_is_bigger(version, mini_iphone)
    elif platform.lower() == 'ipod':
        return _check_version_is_bigger(version, mini_ipod)

    return False

if __name__ == '__main__':
    print (get_is_paid_course('iphone','2.11.0'))