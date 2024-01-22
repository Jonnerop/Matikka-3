import numpy as np
# a)
u = np.array([2, 3])
v = np.array([4, -7])
# b)
uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])
#vektorien normit
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)
norm_uu = np.linalg.norm(uu)
norm_vv = np.linalg.norm(vv)
#tulokset
print(f"Normi u:lle on {norm_u:.2f}")
print(f"Normi v:lle on {norm_v:.2f}")
print(f"Normi uu:lle on {norm_uu:.2f}")
print(f"Normi vv:lle on {norm_vv:.2f}")
