import os

print(os.getcwd())

os.chdir("C:\sample")

print(os.getcwd())


print(os.listdir())

for path, dir, file in os.walk("C:\sample"):
    # print(path)
    # print(dir)
    print(file)


