from s4cl.utils.common_enum import CommonEnum


class ExcludePartFlag(CommonEnum):
    BODYTYPE_NONE = 0
    BODYTYPE_HAT = 1 + 2**1
    BODYTYPE_HAIR = 1 + 2**2
    BODYTYPE_HEAD = 1 + 2**3
    BODYTYPE_FACE = 1 + 2**4
    BODYTYPE_FULLBODY = 1 + 2**5
    BODYTYPE_UPPERBODY = 1 + 2**6
    BODYTYPE_LOWERBODY = 1 + 2**7
    BODYTYPE_SHOES = 1 + 2**8
    BODYTYPE_ACCESSORIES = 1 + 2**9
    BODYTYPE_EARRINGS = 1 + 2**10
    BODYTYPE_GLASSES = 1 + 2**11
    BODYTYPE_NECKLACE = 1 + 2**12
    BODYTYPE_GLOVES = 1 + 2**13
    BODYTYPE_WRISTLEFT = 1 + 2**14
    BODYTYPE_WRISTRIGHT = 1 + 2**15
    BODYTYPE_LIPRINGLEFT = 1 + 2**16
    BODYTYPE_LIPRINGRIGHT = 1 + 2**17
    BODYTYPE_NOSERINGLEFT = 1 + 2**18
    BODYTYPE_NOSERINGRIGHT = 1 + 2**19
    BODYTYPE_BROWRINGLEFT = 1 + 2**20
    BODYTYPE_BROWRINGRIGHT = 1 + 2**21
    BODYTYPE_INDEXFINGERLEFT = 1 + 2**22
    BODYTYPE_INDEXFINGERRIGHT = 1 + 2**23
    BODYTYPE_RINGFINGERLEFT = 1 + 2**24
    BODYTYPE_RINGFINGERRIGHT = 1 + 2**25
    BODYTYPE_MIDDLEFINGERLEFT = 1 + 2**26
    BODYTYPE_MIDDLEFINGERRIGHT = 1 + 2**27
    BODYTYPE_FACIALHAIR = 1 + 2**28
    BODYTYPE_LIPSTICK = 1 + 2**29
    BODYTYPE_EYESHADOW = 1 + 2**30
    BODYTYPE_EYELINER = 1 + 2**31
    BODYTYPE_BLUSH = 1 + 2**32
    BODYTYPE_FACEPAINT = 1 + 2**33
    BODYTYPE_EYEBROWS = 1 + 2**34
    BODYTYPE_EYECOLOR = 1 + 2**35
    BODYTYPE_SOCKS = 1 + 2**36
    BODYTYPE_MASCARA = 1 + 2**37
    BODYTYPE_SKINDETAIL_CREASEFOREHEAD = 1 + 2**38
    BODYTYPE_SKINDETAIL_FRECKLES = 1 + 2**39
    BODYTYPE_SKINDETAIL_DIMPLELEFT = 1 + 2**40
    BODYTYPE_SKINDETAIL_DIMPLERIGHT = 1 + 2**41
    BODYTYPE_TIGHTS = 1 + 2**42
    BODYTYPE_SKINDETAIL_MOLELIPLEFT = 1 + 2**43
    BODYTYPE_SKINDETAIL_MOLELIPRIGHT = 1 + 2**44
    BODYTYPE_TATTOO_ARMLOWERLEFT = 1 + 2**45
    BODYTYPE_TATTOO_ARMUPPERLEFT = 1 + 2**46
    BODYTYPE_TATTOO_ARMLOWERRIGHT = 1 + 2**47
    BODYTYPE_TATTOO_ARMUPPERRIGHT = 1 + 2**48
    BODYTYPE_TATTOO_LEGLEFT = 1 + 2**49
    BODYTYPE_TATTOO_LEGRIGHT = 1 + 2**50
    BODYTYPE_TATTOO_TORSOBACKLOWER = 1 + 2**51
    BODYTYPE_TATTOO_TORSOBACKUPPER = 1 + 2**52
    BODYTYPE_TATTOO_TORSOFRONTLOWER = 1 + 2**53
    BODYTYPE_TATTOO_TORSOFRONTUPPER = 1 + 2**54
    BODYTYPE_SKINDETAIL_MOLECHEEKLEFT = 1 + 2**55
    BODYTYPE_SKINDETAIL_MOLECHEEKRIGHT = 1 + 2**56
    BODYTYPE_SKINDETAIL_CREASEMOUTH = 1 + 2**57
