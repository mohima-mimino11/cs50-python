# Even if you haven’t studied physics (recently or ever!), you might have heard that 𝐸 =𝑚⁢𝑐2
# , wherein 𝐸
# represents energy (measured in Joules), 𝑚
# represents mass (measured in kilograms), and 𝑐
# represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

# Take mass from User
m = int(input("m: "))
# speed of light
c = 300000000

# Returning energy (measured in Joules) in a function
def energy(m,c):
  E = m * c ** 2
  print(f"E: {E}")

energy(m,c)
