from bn256 import g1_hash_to_point

def hash(_hex):
    print("Input", _hex)
    curve_point = g1_hash_to_point(_hex)
    print("Output", hex(curve_point.x.value()), hex(curve_point.y.value()))


hash("0xabcd")
hash("0x01")
hash("0x5566")

# Input 0xabcd
# Output 0x11888685cb663158dee64de84a64eb6adb155921ad84644c6ac1f4fc11ebddcc 0x78230a2e120d21a4f4a8f1327ec853324e672de56847107432d7180bf1c404ac
# Input 0x01
# Output 0x397b9a5aeaa7cffdf1605fbca961bca2b0a33c1048fedcad12f1669ebcdea1ab 0x7f99d02cd84c03335b02ef8f65180cef3686f1332e8633d3d1579eb96f713c24
# Input 0x5566
# Output 0x5d336cf44236a8bd9c5e9ce5e7bedc0695eb3804e1cda2c5d22fb7692a75a8e0 0x4a03577360e40ed8f95c6cbd7a214f1e89d1a38b8fec048b76ea9be0efd65093