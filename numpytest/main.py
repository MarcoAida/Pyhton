import numpy as np

a = np.zeros(10)

print(a)

print(a.shape)

print(a.ndim)

print(a.dtype)

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[10,11,12],[13,14,15]])

print(a)
print(a.shape)
print(b)
print(b.shape)

print(a + b)

c = 2 * a

print(c)

d = np.array([x for x in range(27)])

print(d)

print(d.shape)

d.reshape(3,3,3)

print(d)

i = np.eye(3)

print(i)

print(i.astype)

print(i.astype(bool))

np.hstack((a,b))

np.vstack((a,b))

print(b.T)

print(a@b.T)

print(np.matmul(a,b.T))

x = np.array([1,2,3,4,5])
y = np.array([1,3,2,4,5])
u =  np.where(x == y)

print(x)
print(y)

print(u)
